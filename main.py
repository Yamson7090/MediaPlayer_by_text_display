from video_to_frames import video_to_frames
from video import video_rcon
from video import video_pipe
import subprocess
import os

change_language = 0
change_connect_mode = 0
change_work_mode = 0

# 加载配置文件
with open("config.txt", "r", encoding="utf-8") as f:
    config_txt = f.readlines()

"""
# 判断中文/英文并读取语言文件
language = config_txt[]
if language != "0\n" and language != "1\n":
    language = str(input("Please write down your language here(0 is English, 1 is Chinese):\n请输入语言（0是英文，1是中文）：\n")) + "\n"
    change_language = 1
if language != "0\n" and language != "1\n":
    print("Wrong language chose.")
    print("不存在的语言选项。")
else:
    if change_language :
        config_txt[] = language
        with open("config.txt", "w", encoding="utf-8") as f:
            f.writelines(config_txt)
    if language = "0\n" :
        with open(Path("language") / Path("en-us.txt"), "r", encoding="utf-8") as f:
            language_txt = f.readlines()
    else :
        with open(Path("language") / Path("zh-cn.txt"), "r", encoding="utf-8") as f:
            language_txt = f.readlines()
"""

# 判断rcon/pipe
connect_mode = config_txt[]
if connect_mode != "0\n" and connect_mode != "1\n":
    connect_mode = str(input("请输入链接模式（0是rcon，1是pipe）：\n")) + "\n"
    change_connect_mode = 1
if connect_mode != "0\n" and connect_mode != "1\n":
    print("不存在的工作模式。")
else:
    if change_connect_mode :
        config_txt[] = connect_mode
        with open("config.txt", "w", encoding="utf-8") as f:
            f.writelines(config_txt)

# 判断图片/视频
work_mode = config_txt[]
if work_mode != "0\n" and work_mode != "1\n":
    work_mode = str(input("请输入工作模式（0是视频，1是图片）：\n")) + "\n"



if  = "0\n":
