import cv2
# 1)Lire l’image im1
im1 = cv2.imread('Images/pepper.bmp')
# 2)    Lire la taille de l’image im1 dans h et w
(h, w) = im1.shape[:2]
print("heuteur = ", h,", Largeur = ", w)

#3) Redimensionner l'image im1 en divisant sa taille sur 2, stoker le résultat dans l’image im2
im2 = cv2.resize(im1, (int (h/2), int (w/2)))

#4) Cropper dans im3 la région de l’image im1 délimitée par le rectangle: Y1, Y2, X1, X2[30:150,200:400].
im3=im1[30:150, 200:400]

#5) Copier im1 dans im4, dessiner dans im4 un rectangle
# bleu dans la zone [y_start=30:y_end =150,x_start=200:x_end =400],
# puis saisir sur im4 le texte suivant :« Mon rectangle »
# en couleur verte à la position [x=200, y=20].
im4=im1.copy()
cv2.rectangle(im4, (200,30), (400, 150), (255, 0, 0),3)
cv2.putText(im4, 'Mon rectangle', (200, 20),
cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#6) Appliquer une rotation de l’image im1 de 90°,charger le résultat dans im5
# centre de l'image
center = (w // 2, h // 2)
# Rotation matrix
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
# Rotation 90°
im5 = cv2.warpAffine(im1, matrix, (w, h))
#7) Appliquer un flou Gaussien à l’image im1, stoker le résultat dans im6,
im6 = cv2.GaussianBlur(im1, (15, 15), 0)

#8) Afficher toutes les images créées
cv2.imshow('im1', im1)
cv2.imshow('im2', im2)
cv2.imshow('im3', im3)
cv2.imshow('im4', im4)
cv2.imshow('im5', im5)
cv2.imshow('im6', im6)

kernel_1d = cv2.getGaussianKernel(15, 0)
kernel_2d = kernel_1d @ kernel_1d.T
print(kernel_2d)
cv2.waitKey(0)
cv2.destroyAllWindows()
