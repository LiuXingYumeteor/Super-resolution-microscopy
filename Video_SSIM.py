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
    return ssim_values.mean(dim=1)
