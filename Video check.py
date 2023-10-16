import os
import cv2

# Set the directory path
video_directory = r'E:\\Common files\\Video\\dataset64\\TUIHUA'

# Function to check video properties
def check_video_properties(video_path):
    try:
        # Open the video file
        cap = cv2.VideoCapture(video_path)

        # Get video properties
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Check if the video meets the criteria
        if frame_count == 20 and frame_width == 64 and frame_height == 64:
            return True
        else:
            return False
    except Exception as e:
        return False

# List all files in the directory
video_files = os.listdir(video_directory)

# Iterate through video files and check properties
for video_file in video_files:
    video_path = os.path.join(video_directory, video_file)
    if video_file.endswith(".avi") and not check_video_properties(video_path):
        print(f"Video '{video_file}' does not meet the criteria.")

print("Done checking videos.")
