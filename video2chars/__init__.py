# -*- coding:utf-8 -*-

import click

from .ffmpeg import extract_mp3_from_video, merge_video_and_audio
from .converter import Video2Chars


@click.command()
@click.option("--width", default=80, help='The width of the generated video, in characters, default to 80')
@click.option("--fps", default=8, help='frames per second, defaults to 8')
@click.option("--duration", default=0, help="Specify the length of time that the video needs to be converted")
@click.option("--output", default="output", help='output to a file with this name, default to "output"')
@click.argument("filename")
def convert(filename, width, fps, output, duration):
    time_interval = (0, duration) if duration else None
    video_converter = Video2Chars(video_path=filename, fps_for_chars=fps, time_interval=time_interval)
    video_converter.set_width(width)

    tmp_video_name = "tmp-e6e6.mp4"
    video_converter.write_to_file(tmp_video_name)

    tmp_mp3_name = extract_mp3_from_video(filename)
    merge_video_and_audio(tmp_video_name, tmp_mp3_name, f"{output}.mp4")

