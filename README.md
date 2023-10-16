# Abstract: 
&emsp;&emsp;In this study, we introduce an advanced super-resolution microscopy method. First, a quasi-periodic metallic patch array a quasi-periodic grating capable of converting evanescent waves into propagating waves is designed. The grating is positioned between the object under investigation and the objective lens, the high-frequency information carried by the evanescent waves in the near-field region of the object is transmitted to the far-field for imaging. Subsequently, we provide two deep learning models for image and video reconstructions, respectively, to achieve the reconstruction of far-field imaging for static and dynamic samples. Simulation results demonstrate the high feasibility of the proposed method, enabling rapid localization of sub-wavelength objects with structural features as small as λ/5. This technology can be directly applied to assist traditional bright-field microscopy without the need for extensive optical system design, and dynamic super-resolution imaging can also be achieved.
 
 # Super-resolution imaging of static samples
You can use transcoders for static images in the image format (256,256), of course, our transcoder includes image compression and supports images larger than (256,256).

## The following is a network structure diagram：

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;![image](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/assets/125789189/9d9d3598-3baf-4514-87a6-1b6407a93053)

# Presentation

## Diffraction restoration of fluorescence spot array at a distance of 300 nm

### Degenerate image &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Transcode image
![untitled2](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/assets/125789189/b1750b8f-a968-4001-bef0-dd24860d4a26)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![untitled](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/assets/125789189/8891dbef-bde2-4d70-bfee-1109827522c7)


## Diffraction restoration of fluorescence spot array at a distance of 180 nm

### Degenerate image &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Transcode image
![untitled2](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/assets/125789189/a1238cea-e972-4ec1-ba45-127659eb4e7f)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![untitled](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/assets/125789189/f4bd32bb-d954-4d08-8daa-ef7e356a21df)


## Randomly arranged fluorescent particles (minimum spacing 100 nm)

### Degenerate image &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Transcode image
![cb3cf9a2a0ab4d0f9a49d31ca845f3e](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/assets/125789189/ca1ca0db-b616-43d3-b2d6-fd6774e61755)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![77d1a856b42c40d2eaa48c0f4b37b6b](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/assets/125789189/d78f93b1-bb62-476b-a393-9c823ca05048)

# Super-resolution imaging of dynamic sample

The formats supported by the video transcoder are: resolution: (64, 64), frame rate: 20 frames, images can be processed using the provided image processing code.

## The following is a network structure diagram：

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;![image](https://github.com/LiuXingYumeteor/Super-resolution-microscopy/assets/125789189/5b50aaf3-3aef-4264-b7ac-c4f6aa5ead5e)





