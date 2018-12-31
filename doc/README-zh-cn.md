# 视频转字符动画

这是一个能将视频文件转换成字符动画的命令行工具，使用 pillow + moviepy 实现

## 安装

直接使用 pip 安装 video2chars:
```
# 使用清华镜像源加速下载
pip install video2chars -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 用法

>P.S. 第一次使用 `video2chars` 命令时，会自动下载 `ffmpeg`，该过程在国内可能比较慢。建议自己手动下载，然后配置好环境变量： `FFMPEG_BINARY`
具体参见 [moviepy 手动指定 ffmpeg 路径](https://github.com/Zulko/moviepy/blob/master/moviepy/config_defaults.py) 

```
video2chars --chars_width 120 --t_end 10 path_of_video_file
```
上面的命令表示，将指定路径的视频，转换成宽度为120字符的视频，只转换前十秒。
命令运行完毕后，会在当前目录下生成一个名为 `output.mp4` 的字符视频。

使用 `video2chars --help` 命令，获取更多信息。

>p.s. 注意性能，python 单核跑的，慢也没办法。。默认参数 width=100 fps=8。实在是慢的话，可以尝试调低一下这两个参数。

## 演示

[![【Python】字符动画 - 极乐净土](demostration.png)](https://www.bilibili.com/video/av30469888/)

## 旧版

shell 版 和 html 版 的效果图和代码见 [video2chars - v0.3](https://github.com/yuansuye/video2chars/tree/v0.3)

## 教程

shell 版的教程见[视频转字符动画-Python-60行代码](http://www.cnblogs.com/kirito-c/p/5971988.html)

