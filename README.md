# Video to chars

Convert video to character art animation.

[中文说明](/doc/README-zh-cn.md)

## Install

>p.s. Tested only on linux

First you need to make sure that you can use `ffmpeg` in shell. eg:
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
If it returns `error` or `not found` etc. install [ffmpeg](https://ffmpeg.org/) and add its `bin` directory to `PATH` first. 

then install video2chars:
```
pip install video2chars
```

## Usage

```
video2chars --duration 30 --width 120
```
you will see a file named `output.mp4` in your current path when it completes, have fun ~

>p.s. if it's a bit slow, turn down the width and duration, to speed up the conversion. 

check `video2chars --help` for more information.


## Demonstration

- [【Python】字符动画 - 极乐净土](https://www.bilibili.com/video/av30469888/)


## Older version

[video2chars - v0.3](https://github.com/yuansuye/video2chars/tree/v0.3)

## Article

Shell Version(in Chinese): [视频转字符动画-Python-60行代码](http://www.cnblogs.com/kirito-c/p/5971988.html)
