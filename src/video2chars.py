# -*- coding:utf-8 -*-
from pathlib import Path

import numpy as np
import pickle
import invoke
from threading import Thread

# 用于生成字符画的像素，越往后视觉上越明显。。这是我自己按感觉排的，你可以随意调整。写函数里效率太低，所以只好放全局了
pixels = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"


def video2imgs(video_name, size, seconds):
    """

    :param video_name: 字符串, 视频文件的路径
    :param size: 二元组，(宽, 高)，用于指定生成的字符画的尺寸
    :param seconds: 指定需要解码的时长（0-seconds）
    :return: 一个 img 对象的列表，img对象实际上就是 numpy.ndarray 数组
    """
    import cv2  # 导入 opencv，放这里是为了演示，建议放文件开头

    img_list = []

    # 从指定文件创建一个VideoCapture对象
    cap = cv2.VideoCapture(video_name)

    # 帧率
    fps = cap.get(cv2.CAP_PROP_FPS)
    # 需要提取的帧数
    frames_count = fps * seconds

    count = 0
    # cap.isOpened(): 如果cap对象已经初始化完成了，就返回true
    while cap.isOpened() and count < frames_count:
        # cap.read() 返回值介绍：
        #   ret 表示是否读取到图像
        #   frame 为图像矩阵，类型为 numpy.ndarry.
        ret, frame = cap.read()
        if ret:
            # 转换成灰度图，也可不做这一步，转换成彩色字符视频。
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # resize 图片，保证图片转换成字符画后，能完整地在命令行中显示。
            img = cv2.resize(gray, size, interpolation=cv2.INTER_AREA)

            # 分帧保存转换结果
            img_list.append(img)

            count += 1
        else:
            break

    # 结束时要释放空间
    cap.release()

    return img_list, fps


def img2chars(img):
    """

    :param img: numpy.ndarray, 图像矩阵
    :return: 字符串的列表：图像对应的字符画，其每一行对应图像的一行像素
    """
    res = []

    # 灰度是用8位表示的，最大值为255。
    # 这里将灰度转换到0-1之间
    percents = img / 255

    # 将灰度值进一步转换到 0 到 (len(pixels) - 1) 之间，这样就和 pixels 里的字符对应起来了
    indexes = (percents * (len(pixels) - 1)).astype(np.int)

    # 要注意这里的顺序和 之前的 size 刚好相反
    height, width = img.shape
    for row in range(height):
        line = ""
        for col in range(width):
            index = indexes[row][col]
            # 添加字符像素（最后面加一个空格，是因为命令行有行距却没几乎有字符间距，用空格当间距）
            line += pixels[index] + " "
        res.append(line)

    return res


def imgs2chars(imgs):
    video_chars = []
    for img in imgs:
        video_chars.append(img2chars(img))

    return video_chars


def play_video(video_chars, frames_rate):
    """
    播放字符视频，curses版
    :param video_chars: 字符画的列表，每个元素为一帧
    :param frames_rate: 帧率
    :return: None
    """
    # 导入需要的模块（放这里是为了演示，建议放文件开头）
    import time
    import curses

    # 获取字符画的尺寸
    width, height = len(video_chars[0][0]), len(video_chars[0])

    # 初始化curses，这个是必须的，直接抄就行
    stdscr = curses.initscr()
    curses.start_color()
    try:
        # 调整窗口大小，宽度最好略大于字符画宽度。另外注意curses的height和width的顺序
        stdscr.resize(height, width * 2)

        for pic_i in range(len(video_chars)):
            # 显示 pic_i，即第i帧字符画
            for line_i in range(height):
                # 将pic_i的第i行写入第i列。(line_i, 0)表示从第i行的开头开始写入。最后一个参数设置字符为白色
                stdscr.addstr(line_i, 0, video_chars[pic_i][line_i], curses.COLOR_WHITE)
            stdscr.refresh()  # 写入后需要refresh才会立即更新界面

            time.sleep(1 / frames_rate)  # 粗略地控制播放速度。
    finally:
        # curses 使用前要初始化，用完后无论有没有异常，都要关闭
        curses.endwin()
    return


# def play_video(video_chars, frames_rate):
#     """
#     播放字符视频，clear版
#     :param video_chars: 字符画的列表，每个元素为一帧
#     :param frames_rate: 帧率
#     :return: None
#     """
#     # 导入需要的模块（放这里是为了演示，建议移出去）
#     import time
#     import subprocess
#
#     # 获取字符画的尺寸
#     width, height = len(video_chars[0][0]), len(video_chars[0])
#
#     for pic_i in range(len(video_chars)):
#         # 显示 pic_i，即第i帧字符画
#         for line_i in range(height):
#             # 将pic_i的第i行写入第i列。
#             print(video_chars[pic_i][line_i])
#         time.sleep(1 / frames_rate)  # 粗略地控制播放速度。
#         subprocess.call("clear")


def dump(obj, file_name):
    """
    将指定对象，以file_nam为名，保存到本地
    """
    with open(file_name, 'wb') as f:
        pickle.dump(obj, f)
    return


def load(filename):
    """
    从当前文件夹的指定文件中load对象
    """
    with open(filename, 'rb') as f:
        return pickle.load(f)


def get_video_chars(video_path, size, seconds):
    """
    返回视频对应的字符视频
    """
    video_dump = Path(video_path).with_suffix(".pickle").name

    # 如果 video_dump 已经存在于当前文件夹，就可以直接读取进来了
    if Path(video_dump).exists():
        print("发现该视频的转换缓存，直接读取")
        video_chars, fps = load(video_dump)
    else:
        print("未发现缓存，开始字符视频转换")

        print("开始逐帧读取")
        # 视频转字符动画
        imgs, fps = video2imgs(video_path, size, seconds)

        print("视频已全部转换到图像， 开始逐帧转换为字符画")
        video_chars = imgs2chars(imgs)

        print("转换完成，开始缓存结果")
        # 把[video_chars, fps]保存下来
        dump([video_chars, fps], video_dump)
        print("缓存完毕")

    return video_chars, fps


def play_audio(video_path):
    def call():
        # 使用 invoke 库调用本地方法
        # 之所以不用 subprocess，是因为它没有 hide 属性，调用 mpv 时，即使将输出流重定向了，还是会影响字符画的播放。
        invoke.run(f"mpv --no-video {video_path}", hide=True, warn=True)

    # 这里创建子线程来执行音乐播放指令，因为 invoke.run() 是一个阻塞的方法，要同时播放字符画和音乐的话，就要用多线程/进程。
    p = Thread(target=call)
    p.setDaemon(True)
    p.start()


def main():
    # 宽，高
    size = (64, 48)
    # 视频路径，换成你自己的
    video_path = "resources/BadApple.mp4"
    seconds = 30  # 只转换三十秒
    video_chars, fps = get_video_chars(video_path, size, seconds)

    # 播放音轨
    play_audio(video_path)

    # 播放视频
    play_video(video_chars, fps)


if __name__ == "__main__":
    main()
