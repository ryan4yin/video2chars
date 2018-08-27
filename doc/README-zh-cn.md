# 视频转字符动画

这个项目最初用 shell 方式实现，后来改用 html 做彩色字符画。目前的实现，大概也是最终的方案，是用 pillow + opencv + ffmpeg

shell 版的教程见[视频转字符动画-Python-60行代码](http://www.cnblogs.com/kirito-c/p/5971988.html)

## 安装
>p.s. 只在 linux 上测试过

首先你需要确保能够在 shell 中使用 `ffmpeg` 命令
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

