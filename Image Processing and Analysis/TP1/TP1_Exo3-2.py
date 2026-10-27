# The working code

import cv2

# Reading an image
img = cv2.imread('../Images/fruits.bmp')

# Load the image with its conversion to greyscale
gray_img = cv2.imread('fruits.bmp', cv2.IMREAD_GRAYSCALE)

# Reading image dimensions (greyscale: height, width)
height, width = gray_img.shape
print(f"Height: {height} pixels")
print(f"Width: {width} pixels")

# Fixed threshold
GL_C = 80

# Binarisation with the OpenCV function
ret, imgb1 = cv2.threshold(gray_img, GL_C, 255, cv2.THRESH_BINARY)

# Binarisation with our own code
imgb2 = gray_img.copy()
for i in range(0, height):
    for j in range(0, width):
        if gray_img[i, j] > GL_C:
            imgb2[i, j] = 255
        else:
            imgb2[i, j] = 0

# Saving imgb1
cv2.imwrite('../Images/imgb1.jpg', imgb1)

# Displaying the images
# cv2.imshow('Input Image', img)
# cv2.imshow('Image loaded in greyscale', gray_img)
# cv2.imshow('imgb1 (OpenCV)', imgb1)
cv2.imshow('imgb2', imgb2)
cv2.waitKey(0)
cv2.destroyAllWindows()