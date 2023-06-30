import cv2
import numpy as np
#Read the image
img=cv2.imread("image.jpeg")

#convert the image to grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Apply a Gaussian blur to the image to reduce noise
blurred=cv2.GaussianBlur(gray,(3,3),0)

#use the canny edge detection algorithm to find edges in the image
edges=cv2.Canny(blurred,50,150)

#use the sobel operator to find the gradient magnitude of the image
sobelx=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
sobely=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)
sobel_magnitude=np.sqrt(np.square(sobelx))
np.square(sobely)
sobel_magnitude=np.uint8(sobel_magnitude)

#use a laplacian filter to detect the texture of the image
laplacian=cv2.Laplacian(gray,cv2.CV_64F)
laplacian=np.uint8(np.absolute(laplacian))

#show the original image, the edge image, and the texture image
cv2.imshow("Original", img)
cv2.imshow("Edges",edges)
cv2.imshow("Texture",laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
