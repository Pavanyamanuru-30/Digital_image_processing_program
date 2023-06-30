import cv2
import numpy as np
#read the image
img=cv2.imread('image.jpeg',cv2.IMREAD_GRAYSCALE)

#define the erosion and dilution kernels
kernel=np.ones((5,5),np.uint8)

#Apply erosion to the image
erosion=cv2.erode(img,kernel,iterations=1)

#subtract the erosion from the oe=riginal image
diff_erosion=cv2.absdiff(img,erosion)

#display the difference after erosion
cv2.imshow('Difference after erosion', diff_erosion)
cv2.waitKey(0)

#Apply dilation to the image
dilation=cv2.dilate(img,kernel,iterations=1)

#subtract the dilation from the original image
diff_dilation=cv2.absdiff(img,dilation)

#display the difference after dilation
cv2.imshow('Difference after dilation', diff_dilation)
cv2.waitKey(0)
