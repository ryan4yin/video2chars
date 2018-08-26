# -*- coding:utf-8 -*-
import click

from ffmpeg import extract_mp3_from_video, merge_video_and_audio
from video2chars import *


@click.command()
@click.argument("file")
@click.option("--width", default=120, help='The width of the generated video, in characters, default to 120')
@click.option("--fps", default=10, help='frames per second, defaults to 10')
@click.option("--output", default="output", help='output to a file with this name, default to "output"')
def video2chars(file, width, fps, output):
    convertor = Video2Chars(video_path=file, fps_for_chars=fps)
    convertor.set_width(width)

    convertor.write_to_file("tmp-e6e6.mp4")

    mp3_path = extract_mp3_from_video(Path(file))
    merge_video_and_audio("test-e6e6.mp4", mp3_path, f"{output}.mp4")


if __name__ == '__main__':
    video2chars()

