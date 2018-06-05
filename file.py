# import opencv library
import cv2
# thresholding function that helps keep only the top circles
import imgbw
# import numpy
import numpy as np
# Reads the Image
image = cv2.imread('/home/eric/Desktop/untitled1/imgss/b.jpg')
# image copy for display
imagec = image.copy()
#converts to gray
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# thresholding the Image to get rid of diagonal circles
thresh = imgbw.img2bw(gray,200)
# detecting circles
circles = cv2.HoughCircles(thresh,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=10,minRadius=10,maxRadius=30)
# removing negative values and rounding up numbers
circles = np.uint16(np.around(circles))
#setting a the circle count
count = 0
for i in circles[0,:]:
    # draw the outer circle on the original image
    cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)
    count = count + 1
# casting of interger to String.
t = str(count)
# Concatenation of the converted interger and some custom text
ftext = t + " Dice detected"
cv2.putText(image,ftext,(10,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
cv2.putText(thresh,"Preprocessed to keep only bird view circles",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('detected circles',image)
cv2.imshow('preprocessed Image',thresh)
cv2.imshow('Original Image',imagec)
cv2.waitKey(0)
cv2.destroyAllWindows()
