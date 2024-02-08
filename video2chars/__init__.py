# -*- coding:utf-8 -*-

import click

from video2chars.converter import Video2Chars


@click.command()
@click.option("--width", default=100, help='The width of the generated video, in characters, default to 80')
@click.option("--fps", default=8, help='frames per second, default to 10')
@click.option("--pixels", default=None, type=str, help='the chars sequence used to generate character animation')
@click.option("--start", default=0, help="the start time that the video needs to be converted(in seconds)")
@click.option("--end", default=None, type=int, help="the end time that the video needs to be converted(in seconds)")
@click.option("--output", default="output.mp4", help='output to a file with this name, default to "output.mp4"')
@click.argument("filename")
def convert(filename, width, fps, pixels, output, start, end):
    converter = Video2Chars(video_path=filename,
                            fps=fps,
                            chars_width=width,
                            t_start=start,
                            t_end=end,
                            pixels=pixels)

    clip = converter.generate_chars_video()
    clip.write_videofile(output)



