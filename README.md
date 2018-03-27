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


# Extension

For images that have large blank regions, I try to use global optimization to cope with the blank regions. The idea is to minimize the energy function E = E_match + lambda * E_smooth. E_match is the original SAD error function. E_smooth here I use is: E_smooth = (disparity1-disparity2)^2/(|pixel1-pixel2|+1). It is base on the idea that the more close the color of the two pixels are, the more possible they are in the same depth.

To optimize this energy function is NP-hard problem. But we could use Dynamic Programming to get a closer solution. Here is the code [depth.py](https://github.com/victorygod/Stereo-Depth-Estimation/blob/master/depth.py)

Here is the result for the Luna images.

![left.png](https://github.com/victorygod/Stereo-Depth-Estimation/blob/master/AS15_10325.Panorama_376x3638.tif)
![right.png](https://github.com/victorygod/Stereo-Depth-Estimation/blob/master/AS15_10320.Panorama_376x3638.tif)
![ans.jpg](https://github.com/victorygod/Stereo-Depth-Estimation/blob/master/ans.jpg)

You can see the result provide more information comparing with the result without global optimization:

![ans_basic.jpg](https://github.com/victorygod/Stereo-Depth-Estimation/blob/master/ans_basic_luna.jpg)
