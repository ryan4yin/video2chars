# -*- coding:utf-8 -*-

from pkg_resources import resource_stream

import numpy as np
from moviepy.editor import *

from PIL import Image, ImageFont, ImageDraw


class Video2Chars:
    def __init__(self, video_path, fps, pixels, chars_width, t_start=0, t_end=None):
        """
        :param video_path: 字符串, 视频文件的路径
        :param fps: 生成的视频的帧率
        :param time_interval: 用于截取视频（开始时间，结束时间）单位秒
        """
        # 加载视频,并截取
        video_clip = VideoFileClip(video_path).subclip(t_start, t_end)

        self.fps = fps

        # 像素形状，因为颜色已经用rgb控制了，这里的pixels其实可以随意排
        self.pixels = pixels if pixels else \
            "$#@&%ZYXWVUTSRQPONMLKJIHGFEDCBA098765432?][}{/)(><zyxwvutsrqponmlkjihgfedcba*+1-."

        self.chars_width = chars_width
        self.chars_height = int(chars_width / video_clip.aspect_ratio)

        # resize 一下
        self.video_clip: VideoClip = video_clip.resize((self.chars_width, self.chars_height))

        # 字体相关
        font_fp = resource_stream("video2chars", "DroidSansMono.ttf")
        self.font = ImageFont.truetype(font_fp, size=14)  # 使用等宽字体
        self.font_width = sum(self.font.getsize("a")) // 2  # 为了保证像素宽高一致，均取宽高的平均值

        # 产生的视频的宽高（以像素记）
        self.video_size = int(self.chars_width * self.font_width), int(self.chars_height * self.font_width)

    def get_char_by_gray(self, gray):
        percent = gray / 255  # 转换到 0-1 之间
        index = int(percent * (len(self.pixels) - 1))  # 拿到index
        return self.pixels[index]

    def get_chars_frame(self, t):
        """将图片转换为字符画"""
        # 获取到图像
        img_np = self.video_clip.get_frame(t)
        img = Image.fromarray(img_np, "RGB")
        img_gray = img.convert(mode="L")

        # 新建画布
        img_chars = Image.new("RGB", self.video_size, color="white")
        brush = ImageDraw.Draw(img_chars)  # 画笔

        for y in range(self.chars_height):
            for x in range(self.chars_width):
                r, g, b = img_np[y][x]

                gray = img_gray.getpixel((x, y))
                char = self.get_char_by_gray(gray)

                position = x * self.font_width, y * self.font_width  # x 横坐标（宽），y纵坐标（高，而且向下为正）
                brush.text(position, char, fill=(r, g, b), font=self.font)

        return np.array(img_chars)

    def generate_chars_video(self):
        """生成字符视频对象"""
        clip = VideoClip(self.get_chars_frame, duration=self.video_clip.duration)

        return (clip.set_fps(self.fps)
                .set_audio(self.video_clip.audio))

