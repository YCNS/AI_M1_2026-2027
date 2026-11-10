import cv2
import numpy as np
import math

def calculate_psnr(original_image, degraded_image):
    # Convert images to float64 for PSNR calculation
    original_image = original_image.astype(np.float64)
    degraded_image = degraded_image.astype(np.float64)
    # Calculate Mean Squared Error (MSE)
    mse = np.mean((original_image - degraded_image) ** 2)
    # Handle the case of identical images
    if mse == 0:
        return 100.0 # PSNR is considered infinite or a very high value for identical images
    # Determine the maximum possible pixel value (e.g., 255 for 8-bit images)
    max_pixel_value = 255.0 # Assuming 8-bit images
    # Calculate PSNR
    psnr = 20 * math.log10(max_pixel_value / math.sqrt(mse))
    return psnr
#end of fonction calculate_psnr

# 2) propre fonction pour faire un filtre moyenne
def filtreMoyenne(image, taille_fenetre):
    """
    Applique un filtre moyenneur sur un tableau 2D.
    """
    if taille_fenetre % 2 == 0:
        raise ValueError("La taille de la fenêtre doit être impaire")
    h, w = image.shape;
    moitie_fenetre = taille_fenetre // 2
    # Créer une copie pour stocker le résultat
    resultat = np.copy(image)
    for y in range(moitie_fenetre, h - moitie_fenetre):
        for x in range(moitie_fenetre, w - moitie_fenetre):
            # Calculez la moyenne dans la fenêtre
            fenetre = image[y - moitie_fenetre: y + moitie_fenetre + 1,
                            x - moitie_fenetre: x + moitie_fenetre + 1]
            resultat[y, x] = np.mean(fenetre)
    return resultat

def filtreMoyenne_v2(image, taille_fenetre):
    """
    Applique un filtre moyenneur sur un tableau 2D.
    """
    if taille_fenetre % 2 == 0:
        raise ValueError("La taille de la fenêtre doit être impaire")
    h, w = image.shape
    moitie_fenetre = taille_fenetre // 2
    nbPix=taille_fenetre * taille_fenetre
    # Créez une copie pour stocker le résultat
    resultat = np.copy(image)
    for i in range(moitie_fenetre, h - moitie_fenetre):
        for j in range(moitie_fenetre, w - moitie_fenetre):
            # Calculez la moyenne dans la fenêtre
            s=0.0
            for k in range(-moitie_fenetre, moitie_fenetre+1):
                for l in range(-moitie_fenetre, moitie_fenetre+1):
                    s=s+ image[i+k,j+l]
            resultat[i, j] = s//nbPix
    return resultat

# Filtre médian perso
def filtreMedian(image, taille_fenetre):
    if taille_fenetre % 2 == 0:
        raise ValueError("La taille de la fenêtre doit être impaire")
    h, w = image.shape
    padded_image = np.pad(image, taille_fenetre // 2, mode='edge') # Pad with edge values
    filtered_image = np.zeros_like(image, dtype=image.dtype)
    for r in range(h):
        for c in range(w):
            # Extract the neighborhood
            neighborhood = padded_image[r:r+taille_fenetre, c:c+taille_fenetre]
            # Calculate the median and assign to the output image
            filtered_image[r, c] = np.median(neighborhood)
    return filtered_image
#
def gauss(sigma, x) :
    return math.exp(-(1.0*x * x) // (2.0 * sigma * sigma))

def filtrebilateral(image, taille_fenetre, sigma_s, sigma_r):
    if taille_fenetre % 2 == 0:
        raise ValueError("La taille de la fenêtre doit être impaire")
    h, w = image.shape
    radius = taille_fenetre // 2
    nbPix=taille_fenetre * taille_fenetre
    # Créez une copie pour stocker le résultat
    resultat = np.copy(image)
    for i in range(radius, h - radius):
        for j in range(radius, w - radius):
            sum_weights = 0.0
            sum_weighted_values = 0.0
            for k in range(-radius, radius+1):
                neighbor_i = i+k
                for l in range(-radius, radius+1):
                    neighbor_j = j + l
                    spatial_dist = math.sqrt(k * k + l * l)
                    color_dist =abs(image[i,j].astype(int)-image[neighbor_i, neighbor_j].astype(int))
                    spatial_weight = gauss(sigma_s, spatial_dist)
                    color_weight = gauss(sigma_r, color_dist)
                    total_weight = spatial_weight * color_weight
                    #Cumul des poids et des valeurs
                    sum_weights += total_weight
                    sum_weighted_values += total_weight * image[neighbor_i,neighbor_j]
            #Calcul du pixel filtré
            if sum_weights > 0 :
                resultat[i,j] = sum_weighted_values / sum_weights
            else :
                resultat[i,j] = image[i, j]
    return resultat

# Début de programme principal
# 1) Lecture des trois images, image originale et les deux images bruitées
im1 = cv2.imread('Images/cameraman.bmp', cv2.IMREAD_GRAYSCALE)
im2 = cv2.imread('Images/cameraman_bruit_gauss_sig0_001.bmp', cv2.IMREAD_GRAYSCALE)
im3 = cv2.imread('Images/cameraman_bruit_sel_poivre_p_10.bmp', cv2.IMREAD_GRAYSCALE)

#2) Filtre moyenne opencv
#cv2.blur(img, (3, 3)) : fait une moyenne dans un voisinage 3 x 3 (matrice de convolution avec tous les coefficients identiques et leur somme qui vaut 1) et renvoie l'image résultat.
imf2=cv2.blur(im2, (3, 3))
# Filtre moyenne personnel
imfp2=filtreMoyenne_v2(im2,3)

# 3.c) Appliquer le filtre median
imf3=cv2.medianBlur(im3, 3)
imfm2=cv2.medianBlur(im2, 3)
imfmp=filtreMedian(im3,3)

#3.b) sigma = 0.5 donne une meilleure amélioration
imf4=cv2.GaussianBlur(im2, (3, 3), 0.5)

#3.d filtre bélatéral donne
imfb2 = cv2.bilateralFilter(im2, 7, 40, 40)
imfb3 = cv2.bilateralFilter(im3, 9, 75, 75)

# Filtre bilateral
imfb4=filtrebilateral(im2, 5, 2,30)

#Affichage des images résultantes
cv2.imshow('Image originale', im1)
cv2.imshow('Bruit add gaussien', im2)
cv2.imshow('Filtre moyenne opencv', imf2)
cv2.imshow('Filtre moyenne perso', imfp2)
cv2.imshow('Bruit impulsionnel', im3)
cv2.imshow('Filtre Median im3', imf3)
cv2.imshow('Filtre Median im2', imfm2)
cv2.imshow('Filtre Median perso im3', imfmp)
cv2.imshow('Filtre gaussien im4', imf4)
cv2.imshow('Filtre Bilatéral imfb2', imfb2)
cv2.imshow('Filtre Bilatéral imfb3', imfb3)
cv2.imshow('Filtre Bilatéral perso imfb4', imfb4)
cv2.waitKey(0)
cv2.destroyAllWindows()

#4) PSNR et estimation de la qualité de filtrage
psnr1 = cv2.PSNR(im1,im2)
psnr2=calculate_psnr(im1,imf2)
psnr3 = cv2.PSNR(im1,im3)
psnr4=calculate_psnr(im1,imf3)
psnr5=calculate_psnr(im1,imfp2)
psnr6=calculate_psnr(im1,imf4)
psnr7=calculate_psnr(im1,imfb2)
psnr8=calculate_psnr(im1,imfb3)

print("psnr im1, im2 bruit gauss add: ", psnr1)
print("psnr im1, imf2 moyenne im2: ", psnr2)
print("psnr im1, im3 bruit imp : ", psnr3)
print("psnr im1, imf3 median im3 : ", psnr4)
print("psnr im1, imfm2 median im2 : ", psnr5)
print("psnr im1, imf4 Gaussien : ", psnr6)
print("psnr im1, imfb2 bilatéral : ", psnr7)
print("psnr im1, imfb3 bilatéral : ", psnr8)
