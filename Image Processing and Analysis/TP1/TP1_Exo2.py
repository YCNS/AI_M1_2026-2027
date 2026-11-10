import cv2
# Lecture d'une image
img = cv2.imread('Images/BoatsColor.bmp')

# Charger une image couleur avec sa conversion en niveaux de gris
gray_img = cv2.imread('Images/BoatsColor.bmp', cv2.IMREAD_GRAYSCALE)
# Transformer une image couleurs en une image en niveaux de gris
gray_img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Affichage d'une image
cv2.imshow('Input Image', img)
cv2.imshow(' Image chargée en niveau de gris', gray_img)
cv2.imshow(' Image tranformée en niveau de gris', gray_img2)
cv2.waitKey(0)

# Lecture des couleurs d'un pixel à la position at (100, 150)
pixel = img[100, 150]
print(f"Les valeurs BGR de Pixel à (100, 150) sont : {pixel}")

""" Lecture des dimensions des images : dimensions = img.shape
Pour une image couleur, dimensions contient trois valeurs :
(hauteur, largeur, canaux). hauteur : nombre de lignes de
pixels dans l'image. largeur : nombre de colonnes de pixels
dans l'image. canaux : nombre de canaux de couleur (par
exemple, 3 pour RGB, 1 pour les niveaux de gris). Pour une
image en niveaux de gris, dimensions contient deux valeurs :
(hauteur, largeur)"""

height, width, channels = img.shape
print(f"Height: {height} pixels")
print(f"Width: {width} pixels")
print(f"Channels: {channels}")

#Modification des couleurs de pixel de la ligne de centre vers une couleur rouge
for i in range(0, width):
    img[int (height/2), i] = [0, 0, 255] # [B,G,R] modifier en rouge
cv2.imshow('Image modifiée', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
