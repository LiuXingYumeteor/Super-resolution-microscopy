import cv2
import os

root_path = 'E:\\Common files\\LXY2H'


def gaussian_blur(image_path):
    # 读取图片
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # 对图片进行高斯滤波处理
    blurred_img = cv2.GaussianBlur(img, (5, 5), 0)  # 根据需要调整滤波器的大小

    # 保存处理后的图片，替换原始图片
    cv2.imwrite(image_path, blurred_img)


# 遍历root_path下的所有子文件夹a
for dir_a in os.listdir(root_path):
    path_a = os.path.join(root_path, dir_a)
    if os.path.isdir(path_a):  # 确认是文件夹
        # 遍历子文件夹a中的所有子文件夹b
        for dir_b in os.listdir(path_a):
            path_b = os.path.join(path_a, dir_b)
            if os.path.isdir(path_b):  # 确认是文件夹
                # 遍历子文件夹b中的所有图片并进行处理
                for image_file in os.listdir(path_b):
                    if image_file.endswith('.png'):
                        image_path = os.path.join(path_b, image_file)
                        gaussian_blur(image_path)
