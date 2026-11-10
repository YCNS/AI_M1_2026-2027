import numpy as np
import cv2
# Lecture d'une image
#img = cv2.imread('Images/compteur.jpg', )
img = cv2.imread('Images/flower.bmp', )

# Convertir l'image en niveau de gris
img_ng = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Lecture des dimensions de l'image en niveau de gris
height, width = img_ng.shape

#Pixels with intensity > 80 become 255 (white), others become 0 (black)

# Solution 1 sans numpy
(v , imgb1 )= cv2.threshold(img_ng, 80, 255,
cv2.THRESH_BINARY)

# Solution 2 avec numpy:  Créer une image BGR vide avec numpy
imgb2 = np.zeros((height, width))

for i in range(0, height):
    for j in range(0, width) :
        if img_ng[i,j]> 80 :
            imgb2[i,j] = 255

cv2.imshow('Image couleur', img)
cv2.imshow('Image en niveaux de gris', img_ng)
cv2.imshow('imgb1', imgb1)
cv2.imshow('imgb2', imgb2)
# Save the binary image
cv2.imwrite('Images/imgb1.jpg', imgb1)

cv2.waitKey(0)
cv2.destroyAllWindows()
