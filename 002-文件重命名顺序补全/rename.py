import os
import shutil

base_folder = "原文件夹"
aim_folder = "目标文件夹"

# 获取文件夹下所有文件和文件夹名称
base_filenames = os.listdir(base_folder)
 
# 打印所有文件名
for base_filename in base_filenames:
    [name,file_type] = base_filename.split(".")
    name_int = int(name)
    aim_name = "%03d"%name_int
    print(name,file_type,"=>",aim_name)
    new_aim_filename = "%s.%s"%(aim_name,file_type)

    source_path = "%s/%s"%(base_folder,base_filename)
    target_path = "%s/%s"%(aim_folder,base_filename)
    new_aim_filename = "%s/%s"%(aim_folder,new_aim_filename)

    shutil.copy(source_path, target_path)
    os.rename(target_path, new_aim_filename)
