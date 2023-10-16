import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import os
import cv2
import numpy as np
from SSIM import SSIM

#1.Load Data
class VideoDataset(Dataset):
    def __init__(self, tuihua_folder, target_folder):
        self.tuihua_paths = sorted([os.path.join(tuihua_folder, fname) for fname in os.listdir(tuihua_folder)])
        self.target_paths = sorted([os.path.join(target_folder, fname) for fname in os.listdir(target_folder)])

    def __len__(self):
        return len(self.tuihua_paths)

    def __getitem__(self, idx):
        tuihua = cv2.VideoCapture(self.tuihua_paths[idx])
        target = cv2.VideoCapture(self.target_paths[idx])

        tuihua_frames = []
        target_frames = []

        for _ in range(20):  # Aim to get 20 frames
            ret_t, frame_t = tuihua.read()
            ret_g, frame_g = target.read()

            if ret_t and ret_g:
                tuihua_frames.append(frame_t)
                target_frames.append(frame_g)

        tuihua.release()
        target.release()

        # Pad frames if they are less than 20
        while len(tuihua_frames) < 20:
            tuihua_frames.append(tuihua_frames[-1])
        while len(target_frames) < 20:
            target_frames.append(target_frames[-1])

        # Convert frames to numpy arrays and stack them
        tuihua_frames_np = np.array(tuihua_frames, dtype=np.float32) / 255.0  # Normalize here
        target_frames_np = np.array(target_frames, dtype=np.float32) / 255.0

        # Convert to torch tensor and reshape
        tuihua_tensor = torch.tensor(tuihua_frames_np).permute(0, 3, 1, 2)  # Shape: [20, 3, 64, 64]
        target_tensor = torch.tensor(target_frames_np).permute(0, 3, 1, 2)  # Shape: [20, 3, 64, 64]

        return tuihua_tensor, target_tensor


#2.Model
class FurtherOptimizedVideoRestorationNet(nn.Module):
    def __init__(self):
        super(FurtherOptimizedVideoRestorationNet, self).__init__()

        # 3D convolutional layers with batch normalization and dropout
        self.conv3d_1 = nn.Conv3d(3, 64, kernel_size=(3,3,3), padding=(1,1,1))
        self.bn3d_1 = nn.BatchNorm3d(64)
        self.dropout3d_1 = nn.Dropout3d(0.2)

        self.conv3d_2 = nn.Conv3d(64, 128, kernel_size=(3,3,3), padding=(1,1,1))
        self.bn3d_2 = nn.BatchNorm3d(128)
        self.dropout3d_2 = nn.Dropout3d(0.3)

        self.conv3d_3 = nn.Conv3d(128, 256, kernel_size=(3,3,3), padding=(1,1,1))
        self.bn3d_3 = nn.BatchNorm3d(256)
        self.dropout3d_3 = nn.Dropout3d(0.4)

        self.pool3d = nn.MaxPool3d(kernel_size=(1, 2, 2), stride=(1, 2, 2))

        # Transposed convolutions
        self.deconv3d_1 = nn.ConvTranspose3d(256, 128, kernel_size=(1, 3, 3), stride=(1, 2, 2), padding=(0, 1, 1),output_padding=(0, 1, 1))
        self.bn_deconv3d_1 = nn.BatchNorm3d(128)

        self.deconv3d_2 = nn.ConvTranspose3d(128, 64, kernel_size=(1, 3, 3), stride=(1, 2, 2), padding=(0, 1, 1),output_padding=(0, 1, 1))
        self.bn_deconv3d_2 = nn.BatchNorm3d(64)

        self.deconv3d_3 = nn.ConvTranspose3d(64, 3, kernel_size=(1, 3, 3), stride=(1, 2, 2), padding=(0, 1, 1),output_padding=(0, 1, 1))

        # LSTM layers with dropout
        self.lstm = nn.LSTM(256 * 8 * 8, 1024, num_layers=2, batch_first=True, dropout=0.5)

        # Adding a fully connected layer after LSTM to transform its output
        self.fc = nn.Linear(1024, 256 * 8 * 8)

    def forward(self, x):
        # 3D convolutional layers
        x = x.permute(0, 2, 1, 3, 4)
        x = self.dropout3d_1(self.pool3d(torch.relu(self.bn3d_1(self.conv3d_1(x)))))
        x = self.dropout3d_2(self.pool3d(torch.relu(self.bn3d_2(self.conv3d_2(x)))))
        x = self.dropout3d_3(self.pool3d(torch.relu(self.bn3d_3(self.conv3d_3(x)))))

        # Reshape for LSTM
        x = x.permute(0, 2, 1, 3, 4)
        batch_size, time_steps, C, H, W = x.size()
        x = x.reshape(batch_size, time_steps, -1)

        # LSTM layers
        x, _ = self.lstm(x)
        # Pass through the fully connected layer
        x = self.fc(x)

        # Reshape for deconvolutions
        x = x.reshape(batch_size, time_steps, C, H, W).permute(0, 2, 1, 3, 4)  # <-- Here we rearrange dimensions
        # Transposed convolutions
        x = torch.relu(self.bn_deconv3d_1(self.deconv3d_1(x)))
        x = torch.relu(self.bn_deconv3d_2(self.deconv3d_2(x)))
        x = torch.sigmoid(self.deconv3d_3(x)) # Sigmoid for ensuring the output is in [0, 1] range
        x = x.permute(0, 2, 1, 3, 4)

        return x


# 3. Loss and Optimizer
model = FurtherOptimizedVideoRestorationNet().cuda()
ssim_module = SSIM(window_size=11, size_average=True)
criterion = nn.MSELoss()  # Mean Squared Error Loss
optimizer = optim.Adam(model.parameters(), lr=0.001)
#TODO:损失函数
def video_ssim(video1, video2, ssim_module):
    """
    Compute SSIM over all frames in a video.

    Parameters:
    - video1, video2: 5D tensors of shape (batch_size, time_steps, channels, height, width)
    - ssim_module: An instance of the SSIM module

    Returns:
    - Average SSIM over all frames
    """
    batch_size, time_steps, channels, height, width = video1.shape

    # Initialize SSIM values to 0
    ssim_values = torch.zeros((batch_size, time_steps)).to(video1.device)

    # Compute SSIM for each frame
    for t in range(time_steps):
        ssim_values[:, t] = ssim_module(video1[:, t], video2[:, t])

    # Average SSIM over all frames
    return ssim_values.mean()
'''
# 4. Train the model
def train_model(model, dataloader, criterion, optimizer, num_epochs=1000, save_interval=50):
    for epoch in range(num_epochs):
        for degraded_videos, target_videos in dataloader:
            degraded_videos, target_videos = degraded_videos.cuda(), target_videos.cuda()  # Move data to GPU

            optimizer.zero_grad()
            outputs = model(degraded_videos)
            loss = 1- video_ssim (outputs, target_videos,ssim_module)
            loss.backward()
            optimizer.step()             

        print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item()}")

        if (epoch + 1) % save_interval == 0:
            torch.save(model.state_dict(), f'video_restoration_model_epoch_{epoch + 1}.pth')

# 5. Train the model
dataset_path = "D:\\xyl\\dataset64"
train_dataset = VideoDataset(
    tuihua_folder=os.path.join(dataset_path, "TUIHUA"),
    target_folder=os.path.join(dataset_path, "TARGET")
)
train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)  # Adjust batch_size if necessary
train_model(model, train_loader, criterion, optimizer)
'''

# 6. 部署模型
model_path = 'D:\\xyl\\dataset64\\video_restoration_model_epoch_1000.pth'
model = FurtherOptimizedVideoRestorationNet()
model.load_state_dict(torch.load(model_path))
model.eval().cuda()


def restore_video(input_path, output_path):
    # 使用OpenCV加载整个视频为张量
    cap = cv2.VideoCapture(input_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # 初始化张量
    video_tensor = torch.zeros((1, total_frames, 3, height, width), dtype=torch.float32).cuda()

    for i in range(total_frames):
        ret, frame = cap.read()
        frame_normalized = np.array(frame, dtype=np.float32) / 255.0
        frame_tensor = torch.tensor(frame_normalized).permute(2, 0, 1).cuda()
        video_tensor[0, i] = frame_tensor

    # 使用模型推断
    with torch.no_grad():
        restored_video_tensor = model(video_tensor)

    # 将输出张量转换为视频格式
    for i in range(total_frames):
        restored_frame_tensor = restored_video_tensor[0, i]
        restored_frame_np = (restored_frame_tensor.permute(1, 2, 0).cpu().numpy() * 255).astype(np.uint8)
        out.write(restored_frame_np)

    cap.release()
    out.release()



# 调用函数来恢复视频
input_video_path = "D:\\xyl\\dataset64\\ceshi\\137 (2).avi"  # 请替换为实际的输入视频路径
output_video_path = "D:\\xyl\\dataset64\\chakan\\restored_video3.avi"
restore_video(input_video_path, output_video_path)
