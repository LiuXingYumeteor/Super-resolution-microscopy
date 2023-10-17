# Abstract: 
&emsp;&emsp;In this study, we introduce an advanced super-resolution microscopy method. First, a quasi-periodic metallic patch array a quasi-periodic grating capable of converting evanescent waves into propagating waves is designed. The grating is positioned between the object under investigation and the objective lens, the high-frequency information carried by the evanescent waves in the near-field region of the object is transmitted to the far-field for imaging. Subsequently, we provide two deep learning models for image and video reconstructions, respectively, to achieve the reconstruction of far-field imaging for static and dynamic samples. Simulation results demonstrate the high feasibility of the proposed method, enabling rapid localization of sub-wavelength objects with structural features as small as λ/5. This technology can be directly applied to assist traditional bright-field microscopy without the need for extensive optical system design, and dynamic super-resolution imaging can also be achieved.
 
 # Super-resolution imaging of static samples
You can use transcoders for static images in the image format (256,256), of course, our transcoder includes image compression and supports images larger than (256,256).

## The following is a network structure diagram：

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;![image](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/blob/master/SHOW_Video/%E7%8E%B0%E5%9C%A8.png)

# Presentation

## Diffraction restoration of fluorescence spot array at a distance of 180 nm

### Degenerate image &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Transcode image
![untitled2](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/blob/master/SHOW_Video/180nm1%20(2).png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![untitled](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/blob/master/SHOW_Video/180nm1%20(1).png)


## Diffraction restoration of fluorescence spot array at a distance of 110 nm

### Degenerate image &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Transcode image
![untitled2](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/blob/master/SHOW_Video/110nm%20(2).png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![untitled](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/blob/master/SHOW_Video/110nm%20(1).png)


## Randomly arranged fluorescent particles (minimum spacing 100 nm)

### Degenerate image &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Transcode image
![cb3cf9a2a0ab4d0f9a49d31ca845f3e](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/blob/master/SHOW_Video/100(2).png)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![77d1a856b42c40d2eaa48c0f4b37b6b](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/blob/master/SHOW_Video/100.png)

# Super-resolution imaging of dynamic sample

The formats supported by the video transcoder are: resolution: (64, 64), frame rate: 20 frames, images can be processed using the provided image processing code.

## The following is a network structure diagram：

![image](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/blob/master/SHOW_Video/sudu.png)

# Presentation

## It should be noted that the display image is in GIF format, and the AVI format that meets the requirements can be found in the database of the project

## Diffraction restoration of fluorescence spot array at a distance of 160 nm
### Degenerate video &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Transcode video
![35 (2)](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/blob/master/SHOW_Video/35%20(2).gif)&emsp;&emsp;![35](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/blob/master/SHOW_Video/35.gif)

## Diffraction restoration of fluorescence spot array at a distance of 160 nm
### Degenerate video &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Transcode video
![138 (2)](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/blob/master/SHOW_Video/138%20(2).gif)
&emsp;&emsp;![138](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/blob/master/SHOW_Video/138.gif)

## Diffraction restoration of fluorescence spot array at a distance of 120 nm
### Degenerate video &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Transcode video
![267 (2)](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/blob/master/SHOW_Video/267%20(2).gif)
&emsp;&emsp;![267](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/blob/master/SHOW_Video/267.gif)


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Conclusions
&emsp;&emsp;In summery, this technique demonstrates the potential of combining the spatial-frequency shift method with the deep learning method to achieve super-resolution imaging. We first demonstrate that the grating designed in this work can transform evanescent waves into propagating waves. Then, we employ a deep conditional generative model to reconstruct the far-field intensity distribution of an object before it passes through the grating in free space. We can resolve an object structure with a spatial resolution of more than λ/5 in the far field and ensure that the structural similarity between far-field imaging (1.5um) and near-field imaging (5nm) is 0.89.
While our approach is promising, like other similar methods, it is not without limitations. A primary constraint is that the ability to recover features is ultimately bounded by the training set. Nonetheless, despite these limitations, this technique presents a significant potential for future applications. It can parse most super-resolution details below the system's resolution limit from far-field detected information in a single pass. Such capabilities make it viable for applications in biomedical imaging or as a novel optical characterization tool for rapid data acquisition and artificial intelligence.









