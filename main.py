from video_to_frames import video_to_frames
from video_mcfunction import video_mcfunction
from image import image_mcfunction
from video import video_rcon
from pathlib import Path
from image import image
import os.path
import shutil
#import os

change_language = 0
change_connect_mode = 0
change_work_mode = 0
output = "output"

# 加载配置文件
with open("config.txt", "r", encoding="utf-8") as f:
    config_txt = f.readlines()

"""
# 判断中文/英文并读取语言文件
language = config_txt[3]
if language != "0\n" and language != "1\n":
    language = str(input("Please write down your language here(0 is English, 1 is Chinese):\n请输入语言（0是英文，1是中文）：\n")) + "\n"
    change_language = 1
if language != "0\n" and language != "1\n":
    print("Wrong language chose.")
    print("不存在的语言选项。")
else:
    if change_language :
        config_txt[3] = language
        with open("config.txt", "w", encoding="utf-8") as f:
            f.writelines(config_txt)
    if language = "0\n" :
        with open(Path("language") / Path("en-us.txt"), "r", encoding="utf-8") as f:
            language_txt = f.readlines()
    else :
        with open(Path("language") / Path("zh-cn.txt"), "r", encoding="utf-8") as f:
            language_txt = f.readlines()
"""

# 判断纯rcon/rcon+mcfunction
connect_mode = config_txt[5]
if connect_mode != "0\n" and connect_mode != "1\n":
    connect_mode = str(input("请输入链接模式（0是仅rcon，1是启用mcfunction）：\n")) + "\n"
    change_connect_mode = 1
if connect_mode != "0\n" and connect_mode != "1\n":
    print("不存在的工作模式。")
else:
    if change_connect_mode :
        config_txt[5] = connect_mode
        with open("config.txt", "w", encoding="utf-8") as f:
            f.writelines(config_txt)

# 读取配置，若不存在则写入
if config_txt[21] == "\n":
    config_txt[21] = str(input("请输入您的服务器IP：\nPlease write down your server IP here:")) + "\n"
    with open("config.txt", "w", encoding="utf-8") as f:
        f.writelines(config_txt)
host = str(config_txt[21].strip())
if config_txt[23] == "\n":
    config_txt[23] = str(input("请输入您的Rcon端口：\nPlease write down your Rcon port here:")) + "\n"
    with open("config.txt", "w", encoding="utf-8") as f:
        f.writelines(config_txt)
port = int(config_txt[23].strip())
if config_txt[25] == "\n":
    config_txt[25] = str(input("请输入您的Rcon密码：\nPlease write down your Rcon password here:")) + "\n"
    with open("config.txt", "w", encoding="utf-8") as f:
        f.writelines(config_txt)
password = str(config_txt[25].strip())

# 填写mc服务器根目录
#server_path = config_txt[39].strip()
if connect_mode == "1\n" and (config_txt[39] == "\n" or os.path.isdir(config_txt[39].strip()) == False):
    config_txt[39] = input("请输入服务器根目录地址：\n")
    with open("config.txt", "w", encoding="utf-8") as f:
        f.writelines(config_txt)
    shutil.copytree("mcpack_for_mcfunction/MP", Path(config_txt[39].strip()) / "world" / "datapacks" / "MP")

# 判断图片/视频
work_mode = config_txt[7]
if work_mode != "0\n" and work_mode != "1\n":
    work_mode = str(input("请输入工作模式（0是视频，1是图片）：\n")) + "\n"

# x, y, z
if config_txt[9] == "1\n":
    x = config_txt[13]
    y = config_txt[15]
    z = config_txt[17]
else:
    x = int(input("请输入x坐标：\n"))
    y = int(input("请输入y坐标：\n"))
    z = int(input("请输入z坐标：\n"))

if work_mode == "0\n" :
    fps_in = config_txt[33].strip()
    width_in = config_txt[35].strip()
    video_path = input("输入视频路径：")
    #获取frame_paths
    if os.path.isdir(Path(output) / (Path(video_path).stem + "_fps=" + str(fps_in) + "_width=" + str(width_in))) and os.path.isfile(Path(output) / (Path(video_path).stem + "_fps=" + str(fps_in) + "_width=" + str(width_in)) / "000001.jpg"):
        frame_path_s = sorted([os.path.join(Path(output) / (Path(video_path).stem + "_fps=" + str(fps_in) + "_width=" + str(width_in)), f)
                              for f in os.listdir(Path(output) / (Path(video_path).stem + "_fps=" + str(fps_in) + "_width=" + str(width_in)))
                              if f.endswith(".jpg")])
    else :
        frame_path_s = video_to_frames(input_path=video_path, fps = int(fps_in), width = int(width_in), output_dir = output)

    if connect_mode == "0\n" :
        video_rcon(frame_paths=frame_path_s, config = config_txt, xx = x, yy = y, zz = z)
    elif connect_mode == "1\n" :
        shutil.copytree("mcpack_for_mcfunction/MP", Path(config_txt[39].strip()) / "world" / "datapacks" / "MP", dirs_exist_ok = True)
        video_mcfunction(frame_paths=frame_path_s, config = config_txt, xx = x, yy = y, zz = z)

elif work_mode == "1\n" :
    if connect_mode == "0\n" :
        image(image_path=input("请先处理原图使其宽度缩小！\n请输入图片路径："), base_x=x, base_y=y, base_z=z)
        image_mcfunction(image_path=input("请先处理原图使其宽度缩小！\n请输入图片路径："), server_path =config_txt[39].strip(), base_x=x, base_y=y, base_z=z)
