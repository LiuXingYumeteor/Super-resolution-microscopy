import os
import shutil

root_path = 'E:\\Common files\\VIDEOtuihuaH'
output_path = 'E:\\Common files\\Video\\dataset64\\TUIHUA'
if not os.path.exists(output_path):
    os.mkdir(output_path)

counter = 74

# 遍历root_path下的所有子文件夹a
for dir_a in sorted(os.listdir(root_path)):
    path_a = os.path.join(root_path, dir_a)
    if os.path.isdir(path_a):
        # 遍历子文件夹a中的所有子文件夹b
        for dir_b in sorted(os.listdir(path_a)):
            path_b = os.path.join(path_a, dir_b)
            if os.path.isdir(path_b):
                # 遍历子文件夹b中的所有.avi视频并重命名并移动
                for video_file in sorted(os.listdir(path_b)):
                    if video_file.endswith('.avi'):
                        old_video_path = os.path.join(path_b, video_file)
                        new_video_path = os.path.join(output_path, f"{counter}.avi")
                        shutil.move(old_video_path, new_video_path)
                        counter += 1
