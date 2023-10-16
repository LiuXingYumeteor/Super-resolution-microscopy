import cv2
import os


def extract_frames(video_path, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 打开视频
    cap = cv2.VideoCapture(video_path)

    # 总帧数
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if total_frames > 20:  # 确保视频只有20帧
        print(f"Video {video_path} has more than 20 frames!")
        return

    # 为每一帧创建图片
    for i in range(total_frames):
        ret, frame = cap.read()
        if ret:  # 检查帧是否正确读取
            # 使用帧号命名图片
            frame_filename = os.path.join(output_folder, f"frame_{i + 1}.png")
            cv2.imwrite(frame_filename, frame)

    cap.release()


def main():
    video_folder = "E:\\Common files\\Video\\shipin\\xt"
    for video_file in os.listdir(video_folder):
        if video_file.endswith(('.mp4', '.avi', '.mov')):  # 可根据需要添加其他视频格式
            video_path = os.path.join(video_folder, video_file)

            # 为每个视频创建一个输出文件夹
            output_folder = os.path.join(video_folder, video_file.split('.')[0] + '_frames')
            extract_frames(video_path, output_folder)


if __name__ == "__main__":
    main()
