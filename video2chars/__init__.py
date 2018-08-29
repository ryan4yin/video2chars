# -*- coding:utf-8 -*-

import click

from video2chars.converter import Video2Chars


@click.command()
@click.option("--chars_width", default=80, help='The width of the generated video, in characters, default to 80')
@click.option("--fps", default=10, help='frames per second, defaults to 10')
@click.option("--pixels", default=None, type=str, help='the chars sequence used to generate character animation')
@click.option("--t_start", default=0, help="the start time that the video needs to be converted(in seconds)")
@click.option("--t_end", default=None, type=int, help="the end time that the video needs to be converted(in seconds)")
@click.option("--output", default="output.mp4", help='output to a file with this name, default to "output.mp4"')
@click.argument("filename")
def convert(filename, chars_width, fps, pixels, output, t_start, t_end):
    converter = Video2Chars(video_path=filename,
                            fps=fps,
                            chars_width=chars_width,
                            t_start=t_start,
                            t_end=t_end,
                            pixels=pixels)

    clip = converter.generate_chars_video()
    clip.write_videofile(output)



