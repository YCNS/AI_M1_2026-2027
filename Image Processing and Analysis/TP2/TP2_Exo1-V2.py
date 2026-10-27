# From a class-mate
import cv2
import numpy as np

def sp_noise(image, prob):
    # Add salt and pepper noise to image prob: Probability of the noise

    output = image.copy()

    if len(image.shape) == 2:
        black = 0
        white = 255
    else:
        colorspace = image.shape[2]

        if colorspace == 3:  # RGB
            black = np.array([0, 0, 0], dtype='uint8')
            white = np.array([255, 255, 255], dtype='uint8')
        else:  # RGBA
            black = np.array([0, 0, 0, 255], dtype='uint8')
            white = np.array([255, 255, 255, 255], dtype='uint8')

    probs = np.random.random(output.shape[:2])
    output[probs < (prob / 2)] = black
    output[probs > 1 - (prob / 2)] = white

    return output


# Ouverture de l'image cameraman.bmp en niveaux de gris
im1 = cv2.imread('../Images/cameraman.bmp', cv2.IMREAD_GRAYSCALE)

#print(im1[0:4, 0:4])

print(im1.shape)  # taille : (lignes, colonnes)
print(im1.dtype)  # uint8 : entiers de 0 à 255


# Paramètres de bruit gaussien
# mean = 0, sigma = 30 Adjust this value to control noise intensity

# Créer le bruit Gaussien
gaussian_noise = np.zeros(im1.shape, np.float32)
cv2.randn(gaussian_noise, 0, 10)

# Convert image to float32 for accurate addition

# add noise image
noisy_img_float = cv2.add(im1.astype(np.float32), gaussian_noise)

# Clip values to the valid range (0-255 for 8-bit images)
im2 = np.clip(noisy_img_float, 0, 255).astype(np.uint8)


# Display the original and noisy images
cv2.imshow('Image originale', im1)
cv2.imshow('Bruit gaussien', im2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the noisy image
cv2.imwrite('../Images/cameraman_bruit_gauss_sigo_001.bmp', im2)


im3 = sp_noise(im1, 0.1)

# Display the original and noisy images
cv2.imshow('Image originale', im1)
cv2.imshow('Bruit sp', im3)
cv2.imshow('Bruit gaussien', im2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('../Images/cameraman_bruit_sel_poivre_p_10.bmp', im3)
