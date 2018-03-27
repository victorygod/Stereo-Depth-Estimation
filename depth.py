import numpy as np
from scipy import misc


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def output_img(d_map):
	ans = d_map.copy()
	for x in range(img1.shape[0]):
		for y in range(img1.shape[1]):
			ans[x, y] = np.sqrt(1/(ans[x, y]+1))
	return ans

img1 = misc.imread("AS15_10325.Panorama_376x3638.tif")
img2 = misc.imread("AS15_10320.Panorama_376x3638.tif")

img1 = rgb2gray(img1)
img2 = rgb2gray(img2)

smooth_lambda = 20
window_size = 15
disparity_size = 50
disparity_map = np.zeros(img1.shape)

delta_img = np.zeros([img1.shape[0], img1.shape[1], disparity_size])

#====================SAD=============================
for d in range(1, disparity_size):
	for y in range(window_size//2+d, img1.shape[1]):
		delta_img[:,y,d] = np.abs(img1[:,y] - img2[:,y-d])
#====================================================



for x in range(window_size//2, img1.shape[0]-window_size//2):
	cost = np.zeros([img1.shape[1], disparity_size])
	p = np.zeros(cost.shape)
	for y in range(window_size//2+1, img1.shape[1]-window_size//2):
		
		sad = np.sum(delta_img[x-window_size//2:x+window_size//2, y-window_size//2:y+window_size//2, :], axis=(0,1))
		
		for d in range(1, min(y-window_size//2, disparity_size)):
			for d2 in range(1, min(y-1-window_size//2, disparity_size)):
				c = sad[d] + cost[y-1, d2] + 2000*abs(d-d2)**2/(abs(img1[x, y]-img1[x, y-1])+1)
				if cost[y, d]==0 or cost[y, d]>c:
					cost[y, d] = c
					p[y, d] = d2
		
	ans = 1
	for d in range(1, disparity_size):
		if cost[img1.shape[1]-window_size//2-1, d]<cost[img1.shape[1]-window_size//2, ans]:
			ans = d

	for y in range(window_size//2+1, img1.shape[1]-window_size//2)[::-1]:
		disparity_map[x, y] = ans
		ans = p[y, int(ans)]

	print(x)
	misc.imsave("ans.jpg", output_img(disparity_map))

	#camera_distance*foucs_length/d

misc.imsave("ans.jpg", output_img(disparity_map))
