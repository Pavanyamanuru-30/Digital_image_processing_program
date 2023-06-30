import cv2

image = cv2.imread("image2.jpeg")
height, width = image.shape[:2]          #the height and width of the original image are determined using the 'shape' method
mid_height = height//2                   #mid points of the height and width are calculated using integer division
mid_width = width//2                     #the midpoints are used to divide the image  into 4 parts
up = image[:mid_height, :mid_width]
down = image[mid_height:, :mid_width]
right = image[:mid_height, mid_width:]
left = image[mid_height:, mid_width:]

cv2.imwrite("up.jpg",up)                   #the 4 parts are saved as separate images using the 'imwrite' method
cv2.imwrite("down.jpg",down)
cv2.imwrite("right.jpg",right)
cv2.imwrite("left.jpg",left)