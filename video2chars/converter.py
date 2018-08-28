# -*- coding:utf-8 -*-

from time import time
from pathlib import Path

import cv2
import numpy as np

from PIL import Image, ImageFont, ImageDraw


class Video2Chars:
    # 像素形状，因为颜色已经用rgb控制了，这里的pixels其实可以随意排
    pixels = "$#@&%ZYXWVUTSRQPONMLKJIHGFEDCBA098765432?][}{/)(><zyxwvutsrqponmlkjihgfedcba*+1-."

    def __init__(self, video_path, fps_for_chars=10, time_interval=None):
        """

        :param video_path: 字符串, 视频文件的路径
        :param fps_for_chars: 生成的html的帧率
        :param time_interval: 用于截取视频（开始时间，结束时间）单位秒
        """
        self.video_path = Path(video_path)

        # 从指定文件创建一个VideoCapture对象
        self.cap = cv2.VideoCapture(video_path)

        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.frames_count_all = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)

        # 产生的视频的宽高（以字符记）
        self.chars_width = self.width
        self.chars_height = self.height
        self.frames_count = 0

        self.fps_for_chars = fps_for_chars
        self.time_interval = time_interval

        # 字体相关
        self.font = ImageFont.truetype("DroidSansMono.ttf", size=14)  # 使用等宽字体
        self.font_size = sum(self.font.getsize("a"))//2  # 为了保证像素宽高一致，均取宽高的平均值

        # 产生的视频的宽高（以像素记）
        self.img_chars_size = int(self.chars_width * self.font_size), int(self.chars_height * self.font_size)

    def set_width(self, width):
        """只能缩小，而且始终保持长宽比"""
        if width >= self.width:
            return False
        else:
            self.chars_width = width
            self.chars_height = int(self.height * (width / self.width))
            self.img_chars_size = int(self.chars_width * self.font_size), int(self.chars_height * self.font_size)
            return True

    def set_height(self, height):
        """只能缩小，而且始终保持长宽比"""
        if height >= self.height:
            return False
        else:
            self.chars_height = height
            self.chars_width = int(self.width * (height / self.height))
            self.img_chars_size = int(self.chars_width * self.font_size), int(self.chars_height * self.font_size)
            return True

    def resize(self, img):
        """
        将img转换成需要的大小
        原则：只缩小，不放大。
        """
        # 没指定就不需resize了
        if self.chars_width == self.width or self.chars_height == self.height:
            return img
        else:
            size = (self.chars_width, self.chars_height)
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
        step = self.fps / self.fps_for_chars

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
                print("read failed，stop get_imgs()")
                break

            yield frame  # 惰性求值

        # 结束时要释放空间
        self.cap.release()

    def get_char(self, gray):
        percent = gray / 255  # 转换到 0-1 之间
        index = int(percent * (len(self.pixels) - 1))  # 拿到index
        return self.pixels[index]

    def get_chars_img(self, img):
        """将图片转换为字符画"""

        # 先调整大小
        img = self.resize(img)

        # 新建画布
        img_chars = Image.new("RGB", self.img_chars_size, color="white")
        brush = ImageDraw.Draw(img_chars)  # 画笔

        # 转换成灰度图，用来选择合适的字符
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        for y in range(self.chars_height):
            for x in range(self.chars_width):
                b, g, r = img[y][x]  # 注意是bgr，不是rgb
                gray = img_gray[y][x]
                char = self.get_char(gray)

                position = x * self.font_size, y * self.font_size  # x 横坐标（宽），y纵坐标（高，而且向下为正）
                brush.text(position, char, fill=(r, g, b), font=self.font)

        return cv2.cvtColor(np.array(img_chars), cv2.COLOR_RGB2BGR)  # 转换色彩空间

    def write_to_file(self, filename: str):
        """写入文件"""
        videowriter = cv2.VideoWriter(filename=filename,
                                      apiPreference=cv2.CAP_ANY,
                                      fourcc=cv2.VideoWriter_fourcc(*"mp4v"),  # 4字符的 编解码器代码. (mjpg 可用于 mp4)
                                      fps=self.fps_for_chars,
                                      frameSize=self.img_chars_size)

        if not videowriter.isOpened():
            print("error, cannot open videowriter!")

        i = 0
        time_start = time()
        for img in self.get_imgs():
            img_chars = self.get_chars_img(img)
            videowriter.write(img_chars)

            if i % 50:
                print(f"Progress：{i/self.frames_count * 100:.2f}%, Used time：{time() - time_start:.2f}")

            i += 1
        videowriter.release()
