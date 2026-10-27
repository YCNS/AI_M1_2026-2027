import cv2

# Question 1
image1 = cv2.imread('../Images/fruits.bmp')

# Question 2
height, width, BGR = image1.shape

# Question 3
image2 = cv2.resize(image1, (width//2, height//2))
cv2.imshow('image2', image2)

# Question 4
image3 = image1[30: 150, 200: 400]
cv2.imshow('image3', image3)

# Question 5
image4 = image1.copy()

# Tracer un rectangle
cv2.rectangle(image4, (30,50), (200,400), (255,200,20), 1)

# Put text
cv2.putText(image4, 'image 4 rectangle', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,200,20), 2)
cv2.imshow('image4', image4)

# Question 6
# Rotation
centre = (width//2, height//2)
matrice = cv2.getRotationMatrix2D(centre, 90, 1)
image5 = cv2.warpAffine(image1, matrice, (width, height))
print(matrice)
cv2.imshow('image5', image5)

# Better alternative to rotate
#centre = (width//2, height//2)
#image_rotate_alternative = cv2.rotate(image1, cv2.ROTATE_90_COUNTERCLOCKWISE)
#cv2.imshow('rotate_alternative', image_rotate_alternative)

# Question 7
image6 = cv2.GaussianBlur(image1, (35, 35), 0)
cv2.imshow('image6', image6)

# Question 8 (Already done to each question related created images)
# cv2.imshow('image2', image2)
# cv2.imshow('image3', image3)
# cv2.imshow('image4', image4)
# cv2.imshow('image5', image5)
# cv2.imshow('image6', image6)

# Never forget those commandes
cv2.waitKey(0)
cv2.destroyAllWindows()