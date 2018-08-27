# Video to chars

Convert video to character art animation.

[中文说明](/doc/README-zh-cn.md)

## Install

>p.s. Tested only on linux

First you need to make sure that you can use `ffmpeg` in shell.
Typical desktop linux distributions come with it. If not, install ffmpeg first.

then install video2chars:
```
pip install video2chars
```

## Usage

eg: 
```
video2chars --duration 30 --width 120
```
you will see a file named `output.mp4` in your current path when it completes, have fun ~

>p.s. if it's a bit slow, turn down the width and duration, to speed up the conversion. 

check `video2chars --help` for more information.


## Demonstration

- [【Python】字符动画 - 极乐净土](https://www.bilibili.com/video/av30469888/)


# Older version

[video2chars - v0.3](https://github.com/yuansuye/video2chars/tree/v0.3)

## Article

Shell Version(in Chinese): [视频转字符动画-Python-60行代码](http://www.cnblogs.com/kirito-c/p/5971988.html)