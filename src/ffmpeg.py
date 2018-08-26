# -*- coding:utf-8 -*-
import subprocess


def extract_mp3_from_video(video_path):
    """调用ffmpeg获取mp3音频文件"""
    mp3_path = "tmp-e6e6.mp3"
    subprocess.call(f'ffmpeg -i {video_path} -f mp3 {mp3_path} -y', shell=True)

    return mp3_path


def merge_video_and_audio(video_path, audio_path, output_name):
    """合成视频，并删除中间文件"""
    subprocess.call(f'ffmpeg -i {video_path} -i mp3 {audio_path} -strict -2 -f mp4 {output_name} -y', shell=True)
    print("音频合成完毕，开始删除中间文件")

    subprocess.call(f"rm -rf {video_path} {audio_path}")
    print("完成！")
