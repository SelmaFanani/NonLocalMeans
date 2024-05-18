import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim
"""
Cette fonctiont prend en argument deux images à comparer et renvoie les trois résultats de tests sur ces dernières
"""

def Tests(cheminImage1,cheminImage2):
    # Charger les images
    image_orig = cv2.imread(cheminImage1)
    image_debruitee = cv2.imread(cheminImage2)

    # Convertir l'image en niveaux de gris
    image_grayscale = cv2.cvtColor(image_orig, cv2.COLOR_BGR2GRAY)
    image_grayscale2 = cv2.cvtColor(image_debruitee, cv2.COLOR_BGR2GRAY)

    # Stocker les valeurs de pixels dans une matrice
    pixels_matrix = np.array(image_grayscale)
    pixels_matrix2= np.array(image_grayscale2)

    
    #Fonction de l'erreur quadratique moyenne
    def eQuad(image1, image2):
        # les deux images ont les mêmes dimensions
        assert image1.shape == image2.shape
        eQuad_value = np.mean((image1 - image2) ** 2)
        return eQuad_value

    #Fonction du test PSNR
    def psnr(image_orig, image_debruitee):
        mse = np.mean((image_orig - image_debruitee) ** 2)
        max_pixel = 255.0
        psnr_value = 10 * np.log10(max_pixel**2 / mse)
        return psnr_value

    #Affichage
    erreur_quadratique = eQuad(pixels_matrix, pixels_matrix2)
    return erreur_quadratique
    psnr_value = psnr(pixels_matrix, pixels_matrix2)
    return PSNR
    ssim_value, _ = ssim(pixels_matrix, pixels_matrix2, full=True)
    return SSIM

