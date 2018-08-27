# -*- coding:utf-8 -*-
import subprocess


def extract_mp3_from_video(video_path):
    """调用ffmpeg获取mp3音频文件"""
    mp3_name = "tmp-e6e6.mp3"
    subprocess.call(f'ffmpeg -i {str(video_path)} -f mp3 {mp3_name} -y', shell=True)

    return mp3_name


def merge_video_and_audio(video_path, audio_path, output_name):
    """合成视频，并删除中间文件"""
    subprocess.call(f'ffmpeg -i {str(video_path)} -i {str(audio_path)} -strict -2 -f mp4 {str(output_name)} -y', shell=True)
    print("finish merge!")

    subprocess.call(["rm", str(video_path), str(audio_path)])
    print(f"clean cache! complete conversion! your character art animation: {output_name}, have fun~")
