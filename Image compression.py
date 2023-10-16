import cv2
import os

root_path = 'E:\\Common files\\VIDEOtuihua'


def resize_256x256(image_path):
    # 读取图片
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # 将图片压缩为256x256
    resized_img = cv2.resize(img, (64, 64))

    # 保存压缩后的图片
    cv2.imwrite(image_path, resized_img)


# 遍历root_path下的所有子文件夹a
for dir_a in os.listdir(root_path):
    path_a = os.path.join(root_path, dir_a)
    if os.path.isdir(path_a):  # 确认是文件夹
        # 遍历子文件夹a中的所有子文件夹b
        for dir_b in os.listdir(path_a):
            path_b = os.path.join(path_a, dir_b)
            if os.path.isdir(path_b):  # 确认是文件夹
                # 遍历子文件夹b中的所有图片并进行压缩
                for image_file in os.listdir(path_b):
                    if image_file.endswith('.png'):
                        image_path = os.path.join(path_b, image_file)
                        resize_256x256(image_path)
