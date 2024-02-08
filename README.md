# Video to Chars

[![Build Status](https://travis-ci.org/ryan4yin/video2chars.svg?branch=master)](https://travis-ci.org/ryan4yin/video2chars)
[![PYPI Version](https://img.shields.io/pypi/v/video2chars.svg)](https://pypi.org/project/video2chars/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/07055fe560ba40af83ec09d413d93f4c)](https://app.codacy.com/app/xiaoyin_c/video2chars?utm_source=github.com&utm_medium=referral&utm_content=ryan4yin/video2chars&utm_campaign=Badge_Grade_Dashboard)
[![Python 3.6+](https://img.shields.io/pypi/pyversions/video2chars.svg?style=flat)](https://www.python.org/)

Convert video to character art animation.

[中文说明](/doc/README-zh-cn.md)

## Install


Install video2chars:
```
pip install video2chars
```

If you're using an old version of `pip`, maybe you should add `--prefer-binary` to make things go right(or upgrade your pip first):

```shell
pip install video2chars --prefer-binary
```

This tool relies on `imageio-ffmpeg`, but only the binary version of `imageio-ffmpeg` contains the `ffmpeg` binary.
if pip choose the source version, problem will occurs. 

## Usage

```
video2chars --width 120 --end 10 path/of/video_file
```
The command shows that the specified video will be converted to an ascii art animation with the width of 120, and only convert the first 10 seconds. 
you'll see a file named `output.mp4` in your current directory when completes, have fun ~

>p.s. it's a bit slow, turn down the width and fps, to speed up the conversion. 

Check `video2chars --help` for more information.


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

## Related Projects

- [Video2ASCII.jl(Julia Version)](https://github.com/ryan4yin/Video2ASCII.jl): simple implementation in julia.
- [video2ascii-rs(rust version)](https://github.com/ryan4yin/video2ascii-rs): simple implementation in rust.

## Stargazers over time

[![Stargazers over time](https://starchart.cc/ryan4yin/video2chars.svg)](https://starchart.cc/ryan4yin/video2chars)
