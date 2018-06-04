import cv2
import numpy as np
import imgbw
image = cv2.imread("/home/eric/Desktop/White-Six-Sided-Dice.jpg")
output = image.copy()
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
#thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
thresh = imgbw.img2bw(image,200 )
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(thresh,kernel,iterations = 6)

# detect circles in the image
#circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, 1.2, 100)
circles = cv2.HoughCircles(thresh,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
# ensure at least some circles were found
if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")

    # loop over the (x, y) coordinates and radius of the circles
for (x, y, r) in circles:

    # draw the circle in the output image, then draw a rectangle
    # corresponding to the center of the circle
    cv2.circle(output, (x, y), r, (0, 255, 0), 4)
    cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

# show the output image
cv2.imshow("output", np.hstack([image, output]))

cv2.namedWindow("Image")
cv2.imshow("Image",thresh)
cv2.namedWindow("Imag")
cv2.imshow("Imag",erosion)
cv2.waitKey(0)