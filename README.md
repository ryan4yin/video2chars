# Video to chars

[![Build Status](https://travis-ci.org/ryan4yin/video2chars.svg?branch=master)](https://travis-ci.org/ryan4yin/video2chars)
[![PYPI Version](https://img.shields.io/pypi/v/video2chars.svg)](https://pypi.org/project/video2chars/)
[![Python 3.6+](https://img.shields.io/pypi/pyversions/video2chars.svg?style=flat)](https://www.python.org/)

Convert video to character art animation.

[中文说明](/doc/README-zh-cn.md)

## Install


install video2chars:
```
pip install video2chars
```

if you are using a old `pip`, maybe you should add `--prefer-binary` to make things go right(or upgrade your pip first):

```shell
pip install video2chars --prefer-binary
```

Because this tool relies on `imageio-ffmpeg`, but only the binary version of `imageio-ffmpeg` contains the `ffmpeg` binary.
if pip choose the source version, problem will occurs. 

## Usage

```
video2chars --chars_width 120 --t_end 10 path/of/video_file
```
The above command shows that the path of the specified video will be converted to a ascii video with a width of 120, and only convert the first 10 seconds. 
you'll see a file named `output.mp4` in your current directory when it completes, have fun ~

>p.s. if it's a bit slow, turn down the width and fps, to speed up the conversion. 

check `video2chars --help` for more information.


## Demonstration

[![【Python】字符动画 - 极乐净土](doc/demostration.png)](https://www.bilibili.com/video/av30469888/)



## Old version

[video2chars - v0.3](https://github.com/yuansuye/video2chars/tree/v0.3)

1. shell version demo：
![bad-apple-chars-gif](doc/bad-apple-chars.gif)

2.  html version demo：
![bad-apple-html-gif](doc/bad-apple-html.gif)

## Article

Shell Version(in Chinese): [视频转字符动画-Python-60行代码](http://www.cnblogs.com/kirito-c/p/5971988.html)
