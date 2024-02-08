# -*- coding:utf-8 -*-

import unittest
from pathlib import Path

from video2chars import Video2Chars


class TestConvert(unittest.TestCase):
    current_path = Path(__file__).absolute().parent
    video_path = current_path / Path("BadApple.mp4")
    output_path = Path("output.mp4")

    def setUp(self):
        pass

    def test_convert(self):
        converter = Video2Chars(video_path=str(self.video_path),
                                fps=5,
                                chars_width=35,
                                t_start=1,
                                t_end=5,
                                pixels=None)

        clip = converter.generate_chars_video()
        clip.write_videofile(str(self.output_path))
