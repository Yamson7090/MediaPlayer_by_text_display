from image_to_minecraft_commands import image_to_minecraft_commands
from video_to_images import video_to_images
from pathlib import Path
import time
import mcrcon

def images_to_minecraft_commands(frame_pathes, host, port, password):
    """
    :param frame_pathes:
    :param host:
    :param port:
    :param password:
    :return:
    """
    #skip = 0
    last = 0
    this = 0

    # 用循环一帧一帧处理
    with mcrcon.MCRcon(host = host, port = port, password = password) as rcon:
        # 开始计时
        start_time = time.time()
        for frame_path in frame_pathes:

            # 开始计时
            #frame_start_time = time.time()

            #print(Path("output") / video_name / frame_name)

            if time.time() - start_time <= 0.2 * int(Path(frame_path).stem) - 0.15:
                # 生成本帧指令并发送
                #rcon.command("kill @e[type=text_display]")
                for x in image_to_minecraft_commands(image_path = frame_path, before_last = last):
                    rcon.command(x)

                last = this
                this = int(Path(frame_path).stem)

        rcon.command("kill @e[type=text_display]")


            # 计算下一帧前的等待时间
            #elapsed = time.time() - frame_start_time
            #if (time.time() - frame_start_time) < 0.2 :
            #    delay = 0.2 - (time.time() - frame_start_time) # 5fps = 0.2秒/帧
            #    time.sleep(delay)
            #else :
            #    skip=1

"""
#test
video_name = "2"
frame = "3" + ".jpg"
print(Path("output") / video_name / frame)
"""

# 读取配置，若不存在则写入
with open("config.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
if lines[2] == "\n":
    lines[2] = str(input("请输入您的服务器IP：\nPlease write down your server IP here:")) + "\n"
    with open("config.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)
host = str(lines[2].strip())
if lines[4] == "\n":
    lines[4] = str(input("请输入您的Rcon端口：\nPlease write down your Rcon port here:")) + "\n"
    with open("config.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)
port = int(lines[4].strip())
if lines[6] == "\n":
    lines[6] = str(input("请输入您的Rcon密码：\nPlease write down your Rcon password here:")) + "\n"
    with open("config.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)
password = str(lines[6].strip())

# 输入路径
video_path = input("输入视频路径：")
this_output_dir = Path("output") / Path(video_path)
frame_pathes = video_to_images(input_path = video_path)

images_to_minecraft_commands(frame_pathes = frame_pathes, host = host, port = port, password = password)
