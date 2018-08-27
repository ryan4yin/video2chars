# 视频转字符动画

这是一个能将视频文件转换成字符动画的命令行工具，使用 pillow + opencv + ffmpeg 实现。

## 安装
>p.s. 只在 linux 上测试过

首先你需要确保能够在 shell 中使用 `ffmpeg` 命令。一般的桌面linux发行版都自带的，如果没有，请先安装好 ffmpeg.
然后使用 pip 安装 video2chars:
```
pip install video2chars
```

## 用法

eg: 
```
video2chars --duration 30 --width 120
```

使用 `video2chars --help` 命令，获取更多信息。

## 演示

- [【Python】字符动画 - 极乐净土](https://www.bilibili.com/video/av30469888/)

## 旧版

shell 版 和 html 版 的效果图和代码见 [video2chars - v0.3](https://github.com/yuansuye/video2chars/tree/v0.3)

## 教程

shell 版的教程见[视频转字符动画-Python-60行代码](http://www.cnblogs.com/kirito-c/p/5971988.html)

