# -*- coding:utf-8 -*-
import json
import os
import subprocess
from pathlib import Path

import cv2
import numpy as np

from time import time

import webbrowser

play_chars_js = '''
let i = 0;
window.setInterval(function(){
    let img = frames[i++];
    let html = ""
    for(let line of img){
        for(let char of line){
            let [[r,g,b], ch] = char;
            html += '<span style="color:rgb(' + r + ', ' + g + ', '+ b + ');">'+ ch + '</span>'
            // html += '<span style="background-color:rgb(' + r + ', ' + g + ', '+ b + ');">'+ ch + '</span>'
        }
        html += "<br>"
    }
    
    document.getElementsByClassName("video-panel")[0].innerHTML = html
}, 1000/fps);

document.getElementsByTagName("audio")[0].play();
'''


class VideoToHtml:
    # 像素形状，因为颜色已经用rgb控制了，这里的pixels其实可以随意排
    pixels = "$#@&%ZYXWVUTSRQPONMLKJIHGFEDCBA098765432?][}{/)(><zyxwvutsrqponmlkjihgfedcba*+1-."

    def __init__(self, video_path, fps_for_html=8, time_interval=None):
        """

        :param video_path: 字符串, 视频文件的路径
        :param fps_for_html: 生成的html的帧率
        :param time_interval: 用于截取视频（开始时间，结束时间）单位秒
        """
        self.video_path = Path(video_path)

        # 从指定文件创建一个VideoCapture对象
        self.cap = cv2.VideoCapture(video_path)

        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.frames_count_all = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)

        self.resize_width = None
        self.resize_height = None
        self.frames_count = 0

        self.fps_for_html = fps_for_html
        self.time_interval = time_interval

    def video2mp3(self):
        """#调用ffmpeg获取mp3音频文件"""
        mp3_path = self.video_path.with_suffix('.mp3')
        subprocess.call('ffmpeg -i ' + str(self.video_path) + ' -f mp3 ' + str(mp3_path), shell=True)

        return mp3_path

    def set_width(self, width):
        """只能缩小，而且始终保持长宽比"""
        if width >= self.width:
            return False
        else:
            self.resize_width = width
            self.resize_height = int(self.height * (width / self.width))
            return True

    def set_height(self, height):
        """只能缩小，而且始终保持长宽比"""
        if height >= self.height:
            return False
        else:
            self.resize_height = height
            self.resize_width = int(self.width * (height / self.height))
            return True

    def resize(self, img):
        """
        将img转换成需要的大小
        原则：只缩小，不放大。
        """
        # 没指定就不需resize了
        if not self.resize_width or not self.resize_height:
            return img
        else:
            size = (self.resize_width, self.resize_height)
            return cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)

    def get_img_by_pos(self, pos):
        """获取到指定位置的帧"""
        # 把指针移动到指定帧的位置
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, pos)

        # cap.read() 返回值介绍：
        #   ret 布尔值，表示是否读取到图像
        #   frame 为图像矩阵，类型为 numpy.ndarray.
        ret, frame = self.cap.read()

        return ret, frame

    def get_frame_pos(self):
        """生成需要获取的帧的位置，使用了惰性求值"""
        step = self.fps / self.fps_for_html

        # 如果未指定
        if not self.time_interval:
            self.frames_count = int(self.frames_count_all / step)  # 更新count
            return (int(step * i) for i in range(self.frames_count))

        # 如果指定了
        start, end = self.time_interval

        pos_start = int(self.fps * start)
        pos_end = int(self.fps * end)

        self.frames_count = int((pos_end - pos_start) / step)  # 更新count

        return (pos_start + int(step * i) for i in range(self.frames_count))

    def get_imgs(self):
        assert self.cap.isOpened()

        for i in self.get_frame_pos():
            ret, frame = self.get_img_by_pos(i)
            if not ret:
                print("读取失败，跳出循环")
                break

            yield self.resize(frame)  # 惰性求值

        # 结束时要释放空间
        self.cap.release()

    def get_char(self, gray):
        percent = gray / 255  # 转换到 0-1 之间
        index = int(percent * (len(self.pixels) - 1))  # 拿到index
        return self.pixels[index]

    def get_json_pic(self, img):
        """测试阶段，不实用"""

        json_pic = []

        # 宽高刚好和size相反，要注意。（这是numpy的特性。。）
        height, width, channel = img.shape

        # 转换成灰度图，用来选择合适的字符
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        for y in range(height):
            line = []
            for x in range(width):
                r, g, b = img[y][x]
                gray = img_gray[y][x]
                char = self.get_char(gray)

                line.append([[int(r), int(g), int(b)], char])

            json_pic.append(line)

        return json.dumps(json_pic)

    def write_html_with_json(self, file_name):
        """测试阶段，不实用"""
        mp3_path = self.video2mp3()

        time_start = time()

        with open(file_name, 'w') as html:
            # 要记得设置monospace等宽字体，不然没法玩
            html.write('<!DOCTYPE html>'
                       '<html>'
                       '<body style="font-family: monospace; font-size: small; font-weight: bold; text-align: center; line-height: 0.8;">'
                       '<div class="video-panel"></div>'
                       f'<audio src="{mp3_path.name}" autoplay controls></audio>'
                       '</body>'
                       '<script>'
                       'var frames=[\n')

            try:
                i = 0
                for img in self.get_imgs():
                    json_pic = self.get_json_pic(img)
                    html.write(f"{json_pic},")

                    if i % 20:
                        print(f"进度：{i/self.frames_count * 100:.2f}%, 已用时：{time() - time_start:.2f}")

                    i += 1
            finally:
                html.write('\n];\n'
                           f'let fps={self.fps_for_html};\n'
                           f'{play_chars_js}'
                           '</script>\n'
                           '</html>')


def main():
    # 视频路径，换成你自己的
    video_path = "resources/happy.mp4"

    video2html = VideoToHtml(video_path, fps_for_html=8)
    video2html.set_width(120)

    html_name = Path(video_path).with_suffix(".html").name
    video2html.write_html_with_json(html_name)


if __name__ == "__main__":
    main()

