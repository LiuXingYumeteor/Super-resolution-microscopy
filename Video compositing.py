import cv2
import os

root_path = 'E:\\Common files\\VIDEOtuihuaH'


def generate_video_from_images(image_folder):
    video_name = os.path.join(image_folder, '1.avi')

    # 获取文件夹内的所有png图片并排序
    images = sorted([img for img in os.listdir(image_folder) if img.endswith(".png")])
    if not images:  # 如果文件夹中没有png图片，则直接返回
        return

    # 读取第一张图片以确定视频尺寸
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    size = (width, height)

    # 使用opencv创建视频写入对象，帧率设置为10
    out = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'DIVX'), 10, size)

    # 逐帧写入视频
    for image in images:
        video_frame = cv2.imread(os.path.join(image_folder, image))
        out.write(video_frame)

    out.release()


# 遍历root_path下的所有子文件夹a
for dir_a in os.listdir(root_path):
    path_a = os.path.join(root_path, dir_a)
    if os.path.isdir(path_a):  # 确认是文件夹
        # 遍历子文件夹a中的所有子文件夹b
        for dir_b in os.listdir(path_a):
            path_b = os.path.join(path_a, dir_b)
            if os.path.isdir(path_b):  # 确认是文件夹
                generate_video_from_images(path_b)

