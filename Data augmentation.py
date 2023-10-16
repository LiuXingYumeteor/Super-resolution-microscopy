import os
import cv2

dataset_path = 'E:\\Common files\\Video\\dataset64\\TUIHUA'
start_counter = 147


def rotate_video(video_path, save_path, angle):
    # 打开视频
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # 获取视频的基本参数
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    out = cv2.VideoWriter(save_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 获取旋转后的图像
        M = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
        rotated_frame = cv2.warpAffine(frame, M, (width, height))

        out.write(rotated_frame)

    cap.release()
    out.release()


# 获取视频名并按数字顺序排序
video_files = [f for f in os.listdir(dataset_path) if f.endswith('.avi')]
video_files_sorted = sorted(video_files, key=lambda x: int(x.split('.')[0]))

# 按排序后的顺序遍历视频文件
for video_file in video_files_sorted:
    video_path = os.path.join(dataset_path, video_file)
    save_path = os.path.join(dataset_path, f'{start_counter}.avi')
    rotate_video(video_path, save_path, 90)  # 旋转90度
    start_counter += 1
