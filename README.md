# Video to chars

Convert video to character art animation.

[中文说明](/doc/README-zh-cn.md)

## Install

>p.s. Tested only on linux

install video2chars:
```
pip install video2chars
```

## Usage

>P.S. `video2chars` depends on `moviepy`, and `moviepy` depends on the software `FFMPEG` for video reading and writing. You don’t need to worry about that, 
as `FFMPEG` should be automatically downloaded/installed by `ImageIO` during your first use of `video2chars`.
If you want to use a specific version of `FFMPEG`, you can set the `FFMPEG_BINARY` environment variable.
 See [moviepy/config_defaults.py](https://github.com/Zulko/moviepy/blob/master/moviepy/config_defaults.py) for details.

```
video2chars --chars_width 120 --t_end 10 path_of_video_file
```
The above command shows that the path of the specified video will be converted to a width of 120 characters of video, only 10 seconds before the conversion. 
you'll see a file named `output.mp4` in your current directory when it completes, have fun ~

>p.s. if it's a bit slow, turn down the width and fps, to speed up the conversion. 

check `video2chars --help` for more information.


## Demonstration

- [【Python】字符动画 - 极乐净土](https://www.bilibili.com/video/av30469888/)


## Older version

[video2chars - v0.3](https://github.com/yuansuye/video2chars/tree/v0.3)

## Article

Shell Version(in Chinese): [视频转字符动画-Python-60行代码](http://www.cnblogs.com/kirito-c/p/5971988.html)
