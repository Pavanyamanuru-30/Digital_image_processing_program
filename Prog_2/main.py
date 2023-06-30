import cv2
import numpy as np

image = cv2.imread("image.jpeg")
angle = 45
scale = 1.5

#get the height and width of the image
height, width = image.shape[:2]

#get the center of the image
center = (width//2, height//2)

#get the rotation matrix
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

#apply the rotation to the image
rotated_image = cv2.warpAffine(image, rotation_matrix, (width,height))

#define the translation factors
tx = 50
ty = 100

#get the translation matrix
translation_matrix = np.float32([[1,0,tx],[0,1,ty]])

#apply the translation to the image
translated_image = cv2.warpAffine(rotated_image, translation_matrix, (width,height))

#display the original and modified images
cv2.imshow("Original",image)

#Rotated image
cv2.imshow("Rotated Image", rotated_image)

#Translated image
cv2.imshow("Translated Image", translated_image)

cv2.imshow("Roated, Scaled and Translated", translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
