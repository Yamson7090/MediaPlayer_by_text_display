from PIL import Image
from pathlib import Path
#import mcrcon

"""

def rcon_host():
    # 加载配置文件
    with open("config.txt", "r", encoding="utf-8") as f:
        config = f.readlines()
        
    # 读取配置，若不存在则写入
    if config[21] == "\n":
        config[21] = str(input("请输入您的服务器IP：\nPlease write down your server IP here:")) + "\n"
        with open("config.txt", "w", encoding="utf-8") as f:
            f.writelines(config)
    return str(config[21].strip())
    
def rcon_pot():
    # 加载配置文件
    with open("config.txt", "r", encoding="utf-8") as f:
        config = f.readlines()
        
    # 读取配置，若不存在则写入
    if config[23] == "\n":
        config[23] = str(input("请输入您的Rcon端口：\nPlease write down your Rcon port here:")) + "\n"
        with open("config.txt", "w", encoding="utf-8") as f:
            f.writelines(config)
    return int(config[23].strip())
    
def rcon_password():
    # 加载配置文件
    with open("config.txt", "r", encoding="utf-8") as f:
        config = f.readlines()
        
    # 读取配置，若不存在则写入
    if config[25] == "\n":
        config[25] = str(input("请输入您的Rcon密码：\nPlease write down your Rcon password here:")) + "\n"
        with open("config.txt", "w", encoding="utf-8") as f:
            f.writelines(config)
    return str(config[25].strip())
"""

#最大宽度为44，若调整了指令生成，可能变动
def image(image_path, base_x=100, base_y=100, base_z=100):
    """
    将图片转换为Minecraft文本展示实体指令（每行像素生成一个实体）
    image_path: 图片路径
    base_x/y/z: 生成实体的基准坐标
    """

    img = Image.open(image_path)
    pixels = img.load()
    commands = []

    # 遍历每一行像素
    for y in range(img.height):
        #text_components = []
        text_components = ""
        # 遍历当前行的每个像素
        for x in range(img.width):
            r, g, b, *_ = pixels[x, y] + (0, 0, 0)  # 兼容RGBA/RGB
            hex_color = f"#{r:02x}{g:02x}{b:02x}"

            #添加带颜色的■符号（每个像素一个）
            #text_components.append(f"{{text:'■',color:{hex_color}}}")
            if x < img.width - 1 :
                text_components = f"{text_components}{{text:'■',color:'{hex_color}'}},"
            else :
                text_components = f"{text_components}{{text:'■',color:'{hex_color}'}}"

        # 构建整行指令
        command = (
            f"summon text_display "
            f"{base_x} {base_y + 0.14*(img.height - y)} {base_z} "
            f"{{"
            f"CustomName:image,"
            f"line_width:{img.width * 6},"#根据像素数动态计算行宽
            f"background:-16777216,"#纯黑背景
            f"brightness:{{block:12,sky:12}},"#亮度
            f"text:[{text_components}]"
            f"}}"
        )
        commands.append(command)

    return commands


def image_mcfunction(image_path, server_path, base_x=100, base_y=100, base_z=100):
    """
    将图片转换为Minecraft文本展示实体指令（每行像素生成一个实体）
    image_path: 图片路径
    base_x/y/z: 生成实体的基准坐标
    """

    img = Image.open(image_path)
    pixels = img.load()
    commands = []

    # 遍历每一行像素
    for y in range(img.height):
        #text_components = []
        text_components = ""
        # 遍历当前行的每个像素
        for x in range(img.width):
            r, g, b, *_ = pixels[x, y] + (0, 0, 0)  # 兼容RGBA/RGB
            hex_color = f"#{r:02x}{g:02x}{b:02x}"

            #添加带颜色的■符号（每个像素一个）
            #text_components.append(f"{{text:'■',color:{hex_color}}}")
            if x < img.width - 1 :
                text_components = f"{text_components}{{text:'■',color:'{hex_color}'}},"
            else :
                text_components = f"{text_components}{{text:'■',color:'{hex_color}'}}"

        # 构建整行指令
        command = (
            f"summon text_display "
            f"{base_x} {base_y + 0.14*(img.height - y)} {base_z} "
            f"{{"
            f"CustomName:image,"
            f"line_width:{img.width * 6},"#根据像素数动态计算行宽
            f"background:-16777216,"#纯黑背景
            f"brightness:{{block:12,sky:12}},"#亮度
            f"text:[{text_components}]"
            f"}}\n"
        )
        commands.append(command)

    with open(Path(server_path) / "world" / "datapacks" / "MP" / "data" / "image" / "function" / "image.mcfunction", "w", encoding="utf-8") as f:
        f.writelines(commands)
    return ["reload","function image:image"]

#print(image_to_minecraft_commands(image_path = input(":")))

#with open("a.mcfunction", "w", encoding="utf-8") as f:
#    f.writelines(image_mcfunction(image_path = input(":"))