import cv2
# Reading an image
img = cv2.imread('crystal.jpg')

# Load a colour image with its conversion to greyscale
gray_img = cv2.imread('crystal.jpg', cv2.IMREAD_GRAYSCALE)
# Converting a colour image to a greyscale image
gray_img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Displaying an image
cv2.imshow('Input Image', img)
cv2.imshow(' Image loaded in greyscale ', gray_img)
cv2.imshow(' Image converted to greyscale ', gray_img2)
cv2.waitKey(0)

# Reading the colours of a pixel at position (100, 150)
pixel = img[100, 150]
print(f" The RGB values of Pixel at (100, 150) are: {pixel}")

""" Reading image dimensions: dimensions = img.shape
For a colour image, dimensions contains three values:
(height, width, channels). height: number of rows of pixels in the image.
width: number of columns of pixels in the image. channels: number of colour
channels (e.g. 3 for RGB, 1 for greyscale). For a greyscale image,
dimensions contains two values: (height, width """

height, width, channels = img.shape
print(f"Height: {height} pixels")
print(f"Width: {width} pixels")
print(f"Channels: {channels}")

#Changing the pixel colours of the centre line to red
for i in range(0, width):
    img[int(height/2), i] = [0, 0, 255] # [B,G,R] modified to red
cv2.imshow('Converted Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
