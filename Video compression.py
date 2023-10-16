import cv2
import os

def resize_video(input_path, dimensions=(64, 64)):
    # Capture the input video
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"Error opening video: {input_path}")
        return

    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))

    # Create a temporary video writer for output video
    temp_output_path = input_path + "_temp.avi"
    out = cv2.VideoWriter(temp_output_path, fourcc, fps, dimensions)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame
        resized_frame = cv2.resize(frame, dimensions)

        # Write the frame to the output video
        out.write(resized_frame)

    # Release the video objects and delete the original video
    cap.release()
    out.release()
    os.remove(input_path)
    os.rename(temp_output_path, input_path)

# Specify the directory
directory = "E:\\Common files\\Video\\dataset64\\TUIHUA"

# Iterate through all files in the directory
for filename in os.listdir(directory):
    # Check if the file has .avi extension
    if filename.endswith(".avi"):
        input_path = os.path.join(directory, filename)
        resize_video(input_path)
        print(f"Resized: {filename}")

print("All videos resized!")
