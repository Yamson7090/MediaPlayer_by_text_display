from PIL import Image
#import mcrcon

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

def image_mcfunction(image_path, base_x=100, base_y=100, base_z=100):
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

    return commands

#print(image_to_minecraft_commands(image_path = input(":")))

#with open("a.mcfunction", "w", encoding="utf-8") as f:
#    f.writelines(image_mcfunction(image_path = input(":"))