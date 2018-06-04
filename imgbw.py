
import cv2
import numpy as np
def img2bw(img,th):

    h,w = img.shape[0:2]
    img2 = img
    segimg = np.zeros([h,w],'uint8');
    for rows in range(0,h):
        for cols in range(0,w):
           if img2[rows][cols] > th:
                segimg[rows][cols]= 0
           else:
               segimg[rows][cols]= 255
    return segimg
