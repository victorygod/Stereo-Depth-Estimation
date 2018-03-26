# Stereo-Depth-Estimation

Target: take as input a rectified stereo pair, and creates a depth map of the scene.

# Basic idea

Select suitable window and for each pixle in the left image as the center of the window for left, slide the window for right in the corresponding position of the right image. If we can find the position with the minimum error function of window for left and window for right, we find the corresponding points for one pixel.

The error function here is the SAD, which takes the absolute value of the difference of window for left and window for right.

As for the images pair is well rectified, so I only slide the window horizontally.

After finding the corresponding points, we can get the disparity of the two points and we can use the formular: 
            distance = camera_distance * focus_length / disparity 
to get the depth of every pixel.

This part of the code is in the [depth_basic.py](https://github.com/victorygod/Stereo-Depth-Estimation/blob/master/depth_basic.py)

# Result images

![left.png](https://github.com/victorygod/Stereo-Depth-Estimation/blob/master/left.png)
![right.png](https://github.com/victorygod/Stereo-Depth-Estimation/blob/master/right.png)
![ans_basic.jpg](https://github.com/victorygod/Stereo-Depth-Estimation/blob/master/ans_basic.jpg)
