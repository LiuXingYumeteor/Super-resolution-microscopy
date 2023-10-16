import cv2
import os

root_path = 'E:\\Common files\\LXY2H'

def process_image(image_path):
    # 读取图片
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # 转换为灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 将灰度图像转换为热图
    colormap = cv2.COLORMAP_JET
    heatmap = cv2.applyColorMap(gray, colormap)

    # 保存处理后的图片
    cv2.imwrite(image_path, heatmap)

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
                    if image_file.endswith(('.png', '.jpg', '.jpeg')):  # 可以根据需要添加其他图片格式
                        image_path = os.path.join(path_b, image_file)
                        process_image(image_path)
