# 视频转字符动画

这是一个能将视频文件转换成字符动画的命令行工具，使用 pillow + opencv + ffmpeg 实现。

## 安装
>p.s. 只在 linux 上测试过

首先你需要确保能够在 shell/powershell 中使用 `ffmpeg` 命令。示例：
```
PS C:\> ffmpeg
ffmpeg version N-91693-g3aacb0d196 Copyright (c) 2000-2018 the FFmpeg developers
  built with gcc 8.2.1 (GCC) 20180813
  configuration: --enable-gpl --enable-version3 --enable-sdl2 --enable-fontconfig --enable-gnutls --enable-iconv --enable-libass --enable-libbluray --enable-libfreetype --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libtheora --enable-libtwolame --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libzimg --enable-lzma --enable-zlib --enable-gmp --enable-libvidstab --enable-libvorbis --enable-libvo-amrwbenc --enable-libmysofa --enable-libspeex --enable-libxvid --enable-libaom --enable-libmfx --enable-amf --enable-ffnvcodec --enable-cuvid --enable-d3d11va --enable-nvenc --enable-nvdec --enable-dxva2 --enable-avisynth
  libavutil      56. 19.100 / 56. 19.100
  libavcodec     58. 25.100 / 58. 25.100
  libavformat    58. 17.103 / 58. 17.103
  libavdevice    58.  4.101 / 58.  4.101
  libavfilter     7. 26.100 /  7. 26.100
  libswscale      5.  2.100 /  5.  2.100
  libswresample   3.  2.100 /  3.  2.100
  libpostproc    55.  2.100 / 55.  2.100
Hyper fast Audio and Video encoder
usage: ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...
```
如果 powershell 输出 `无法将“ffmpeg”项识别为 cmdlet、函数、脚本文件或可运行程序的名称。`，或者 shell 输出 `command not found`，说明你没有安装 ffmpeg. 请先安装好 [ffmpeg](https://ffmpeg.org/), 并将其 bin 目录添加进 PATH. 

然后使用 pip 安装 video2chars:
```
# 使用清华镜像源加速下载
pip install video2chars -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 用法

```
video2chars --duration 30 --width 120 path_of_video_file
```
命令运行完毕后，会在当前目录下生成一个名为 `outpu.mp4` 的字符视频。

使用 `video2chars --help` 命令，获取更多信息。

>p.s. 注意性能，python 单核跑的，慢也没办法。。默认参数 width=80 fps=8。实在是慢的话，可以尝试调低一下这两个参数。

## 演示

- [【Python】字符动画 - 极乐净土](https://www.bilibili.com/video/av30469888/)

## 旧版

shell 版 和 html 版 的效果图和代码见 [video2chars - v0.3](https://github.com/yuansuye/video2chars/tree/v0.3)

## 教程

shell 版的教程见[视频转字符动画-Python-60行代码](http://www.cnblogs.com/kirito-c/p/5971988.html)

