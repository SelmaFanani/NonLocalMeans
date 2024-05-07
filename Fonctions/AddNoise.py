#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:16:26 2024

@author: selmafanani
"""

import numpy as np
import cv2

def getImage(index, grayscale = False, scale = 0.5):
  '''
  Helper function that returns images given a certain image index
  '''
  if grayscale:
    grayscale = 0
  else:
    grayscale = 1
  gt = cv2.imread('/Users/selmafanani/Downloads/Dossier_MI/Images/Image' + str(index) + '.png', grayscale)
  gt = cv2.resize(gt, (0,0), fx = scale, fy = scale)
  return gt


def addNoise(image, noiseType, p = 0.001, mean = 0,  sigma = 0.3):
  ''' 
  This function takes an image and returns an image that has been noised with the given input parameters.
  p - Probability threshold of salt and pepper noise.
  noisetype - 
  '''
  
  if noiseType == 'GAUSSIAN':
    sigma *= 255 #Since the image itself is not normalized
    noise = np.zeros_like(image)
    noise = cv2.randn(noise, mean, sigma)
    ret = cv2.add(image, noise) #generate and add gaussian noise
    return ret

  elif noiseType == 'SALTNPEPPER':
    output = image.copy()
    # Calcule le nombre de pixels à altérer
    num_salt = np.ceil(p * image.size * 0.5).astype(int)
    num_pepper = np.ceil(p * image.size * 0.5).astype(int)

    # Ajouter le bruit sel
    coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    output[coords[0], coords[1]] = 1

    # Ajouter le bruit poivre
    coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    output[coords[0], coords[1]] = 0
    return output

  elif noiseType == 'RICIAN' :
    # Génère du bruit gaussien pour les composantes X et Y
    noise_x = np.random.normal(0, sigma, image.shape)
    noise_y = np.random.normal(0, sigma, image.shape)
    # Calcule l'image bruitée
    noisy_image = np.sqrt((image + noise_x)**2 + noise_y**2)
    return noisy_image
