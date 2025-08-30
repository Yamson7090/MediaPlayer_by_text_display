import os
from ffmpeg_progress_yield import FfmpegProgress
from tqdm import tqdm
from pathlib import Path

#生成的总帧数不得大于999999
def video_to_frames(input_path, output_dir = "output", fps, width):
    """
    input_path: 输入视频路径
    output_dir: 输出目录
    fps: 每秒帧数 (默认5)
    width: 输出宽度 (默认40)
    return: 生成的图片序列路径列表
    """

    """
    # 获取路径
    input_path = input("请输入视频路径：")
    # 获取文件名生成文件夹名
    file_name = Path(input_path)
    output_dir = Path("output") / "jpgs" / file_name.stem
    """
    this_output_dir = Path(output_dir) / (Path(input_path).stem + "_fps=" + str(fps) + "_width=" + str(width))

    os.makedirs(this_output_dir, exist_ok=True)
    output_pattern = os.path.join(this_output_dir, "%06d.jpg")

    # 构建Ffmpeg命令
    cmd = [
        "ffmpeg",
        "-i", input_path,
        "-r", str(fps),
        "-vf", f"scale={width}:-2,",
        "-q:v", "2",  # 平衡质量和文件大小
        output_pattern
    ]

    # 执行带进度条的命令
    ff = FfmpegProgress(cmd)
    with tqdm(total=100, desc="视频处理进度", unit="%") as pbar:
        for progress in ff.run_command_with_progress():
            pbar.update(progress - pbar.n)

    # 生成图片序列
    frame_paths = sorted([os.path.join(this_output_dir, f)
                          for f in os.listdir(this_output_dir)
                          if f.endswith(".jpg")])

    """
    # 写入图片序列
    with open(this_output_dir / "frame_paths.txt", "w", encoding="utf-8") as f:
        f.write(str(frame_paths))
    """

    return frame_paths

"""
video_to_images(input_path,output_dir)
for a in video_to_images(input_path = input(),output_dir = "output",fps=5, width=40):
    print(a)
"""
#video_to_images(input_path = input(),output_dir = "output",fps=5, width=40)