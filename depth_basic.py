import numpy as np
from scipy import misc


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def output_img(d_map):
	ans = d_map.copy()
	for x in range(window_size//2, img1.shape[0]-window_size//2):
		for y in range(window_size//2+1, img1.shape[1]-window_size//2):
			ans[x, y] = np.sqrt(1/ans[x, y])
	return ans

img1 = misc.imread("left.png")
img2 = misc.imread("right.png")

img1 = rgb2gray(img1)
img2 = rgb2gray(img2)

smooth_lambda = 20
window_size = 15
disparity_size = 50
disparity_map = np.zeros(img1.shape)


def smooth_cost(x, y, dd):
	cost = 0
	for dx in range(-2, 3):
		for dy in range(-2, 3):
			if (x+dx>=0 and x+dx<img1.shape[0] and y+dy>window_size//2 and y+dy<img1.shape[1]-window_size//2):
				cost+=(disparity_map[x, y] + dd - disparity_map[x+dx, y+dy])**2
	return smooth_lambda*cost

delta_img = np.zeros([img1.shape[0], img1.shape[1], disparity_size])

for d in range(1, disparity_size):
	for y in range(window_size//2+d, img1.shape[1]):
		delta_img[:,y,d] = np.abs(img1[:,y] - img2[:,y-d])

for x in range(window_size//2, img1.shape[0]-window_size//2):
	for y in range(window_size//2+1, img1.shape[1]-window_size//2):
		
		delta = np.sum(delta_img[x-window_size//2:x+window_size//2, y-window_size//2:y+window_size//2, :], axis=(0,1))
		
		d = 1+np.argmin(delta[1: min(y-window_size//2, disparity_size+1)+1])
		
		disparity_map[x, y] = d #camera_distance*foucs_length/d

misc.imsave("ans.jpg", output_img(disparity_map))
