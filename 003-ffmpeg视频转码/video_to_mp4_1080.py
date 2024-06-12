import os
input_folder = "/Volumes/WD 4T/电视剧/神雕侠侣95版/"
input_files = [
# "01.mkv",
# "02.mkv",
"03.mkv",
# "04.mkv",
# "05.mkv",
# "06.mkv",
# "07.mkv",
# "08.mkv",
# "09.mkv",
# "10.mkv",
# "11.mkv",
# "12.mkv",
# "13.mkv",
# "14.mkv",
# "15.mkv",
# "16.mkv",
# "17.mkv",
# "18.mkv",
# "19.mkv",
# "20.mkv",
# "21.mkv",
# "22.mkv",
# "23.mkv",
# "24.mkv",
# "25.mkv",
# "26.mkv",
# "27.mkv",
# "28.mkv",
# "29.mkv",
# "30.mkv",
# "31.mkv",
# "32.mkv",
]
base_filenames = os.listdir(input_folder)
ffmpeg_files = []
for base_filename in base_filenames:
    if base_filename in input_files:
        print(base_filename)
        file_path = os.path.join(input_folder,base_filename)
        print(file_path)
        ffmpeg_files.append(file_path)
print(ffmpeg_files)
import subprocess

for ffmpeg_file in ffmpeg_files[0:]:
    input_file = ffmpeg_file
    output_file = input_file+".mp4"
    ffmpeg_command = [
        'ffmpeg',  # 调用ffmpeg程序
        '-hwaccel','videotoolbox',
        # '-thread_queue_size', '1024',
        '-i', input_file,  # 输入文件
        '-c:v', 'libx264',  # 使用libx264编解码器
        '-crf', '26',
        '-preset', 'ultrafast',  # 编码速度和质量的平衡，slow表示质量更好
        '-c:a', 'aac',
        '-vf', 'scale=1920:1080',
        # '-vf', 'scale=1280:720',
        # '-b:a', '128k',
        output_file  # 输出文件
        # '-hide_banner'
    ]
    print(ffmpeg_command)
    try:
        # 使用subprocess.run来执行命令
        result = subprocess.run(ffmpeg_command, check=True, text=True, capture_output=False)
        print("命令执行成功，输出信息：", result.stdout)
    except subprocess.CalledProcessError as e:
        print("命令执行失败，错误信息：", e.stderr)

# ffmpeg -i input.mp4 -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k output.mp4
# ffmpeg -i input_file -vf scale=1920:1080 output_file -hide_banner # 1080p
