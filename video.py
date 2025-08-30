from frame_to_minecraft_commands import frame_to_minecraft_commands
from video_to_frames import video_to_frames
from pathlib import Path
import time
import mcrcon

def video_rcon(frame_paths, config):

    # 读取配置，若不存在则写入
    if config[2] == "\n":
        config[2] = str(input("请输入您的服务器IP：\nPlease write down your server IP here:")) + "\n"
        with open("config.txt", "w", encoding="utf-8") as f:
            f.writelines(config)
    host = str(config[2].strip())
    if config[4] == "\n":
        config[4] = str(input("请输入您的Rcon端口：\nPlease write down your Rcon port here:")) + "\n"
        with open("config.txt", "w", encoding="utf-8") as f:
            f.writelines(config)
    port = int(config[4].strip())
    if config[6] == "\n":
        config[6] = str(input("请输入您的Rcon密码：\nPlease write down your Rcon password here:")) + "\n"
        with open("config.txt", "w", encoding="utf-8") as f:
            f.writelines(config)
    password = str(config[6].strip())

    #skip = 0
    # 上一帧序号
    last = 0
    # 本帧序号
    this = 0

    # 用循环一帧一帧处理
    with mcrcon.MCRcon(host = host, port = port, password = password) as rcon:
        # 开始计时
        start_time = time.time()
        for frame_path in frame_paths:

            # 开始计时
            #frame_start_time = time.time()

            #print(Path("output") / video_name / frame_name)

            if time.time() - start_time <= 0.2 * int(Path(frame_path).stem) - 0.15:
                # 生成本帧指令并发送
                #rcon.command("kill @e[type=text_display]")
                for x in frame_to_minecraft_commands(image_path = frame_path, before_last = last):
                    rcon.command(x)

                last = this
                this = int(Path(frame_path).stem)

        rcon.command("kill @e[type=text_display,name=!image]")


            # 计算下一帧前的等待时间
            #elapsed = time.time() - frame_start_time
            #if (time.time() - frame_start_time) < 0.2 :
            #    delay = 0.2 - (time.time() - frame_start_time) # 5fps = 0.2秒/帧
            #    time.sleep(delay)
            #else :
            #    skip=1

def video_pipe():


"""
#test
video_name = "2"
frame = "3" + ".jpg"
print(Path("output") / video_name / frame)
"""

"""
# 输入原视频路径并获取生成的每帧的路径
video_path = input("输入视频路径：")
frame_path_s = video_to_frames(input_path=video_path)

video_rcon(frame_paths = frame_path_s)
"""