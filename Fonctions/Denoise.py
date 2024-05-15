#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:17:55 2024

@author: selmafanani
"""
import cv2
import AddNoise.python3
import NLMeans.python3



def denoise(index, verbose = True, gaussian = False, salted = True, rician = False):
  '''
  Helper function that:
  - takes an index
  - gets the images
  - adds noise
  - Denoises with various filters 
  - Saves all images
    Dont forget to : 
  - Create two directories: Noised and Denoised to save the images before executing the code below and change the path 
  
  '''
  print('DENOISING IMAGE', index)
  
  grayscale = False
  scale = 2 #Scale factor of the image
  gtImg =getImage(index, grayscale = grayscale, scale = scale)

  # Noise parameters
  sigma = 0.05 #Gaussian sigma
  p = 0.09 #Threshold for SNP noise
  sigma1 = 0.2 #Rician sigma

  gNoised = addNoise(gtImg, 'GAUSSIAN', sigma = sigma) 
  saltNoised = addNoise(gtImg, 'SALTNPEPPER', p = p)
  ricianNoised = addNoise(gtImg, 'RICIAN', sigma = sigma1)

  
  if gaussian:
      #NLM filter parameters  
      gParams = {
          'bigWindow' : 20,
          'smallWindow':6,
          'h':16,
          'scale':scale,
        }

      if grayscale : 
         #perform NLM filtering
        nlmFilteredGNoised_Grayscale = nonLocalMeans_Grayscale(gNoised, params = (gParams['bigWindow'], gParams['smallWindow'],gParams['h']), verbose = verbose)
        #write images to file
        cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/Noised/Image' + str(index) + '-GNOISE-GRAYSCALE.png', gNoised)
        cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/Denoised/Image' + str(index) + '-NLM-Gauss-GRAYSCALE.png', nlmFilteredGNoised_Grayscale)
      else :
         #perform NLM filtering
        nlmFilteredGNoised_RGB = nonLocalMeans_RGB(gNoised, params = (gParams['bigWindow'], gParams['smallWindow'],gParams['h']), verbose = verbose)
        #write images to file
        cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/Noised/Image' + str(index) + '-GNOISE-RGB.png', gNoised)
        cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/Denoised/Image' + str(index) + '-NLM-Gauss-RGB.png', nlmFilteredGNoised_RGB)
    
      
  if salted:
      #NLM filter parameters
      saltParams = {
          'bigWindow' : 30,
          'smallWindow':6,
          'h':29,
          'scale':scale,
        }
        
      if grayscale : 
        #perform NLM filtering
        nlmFilteredSalted_Grayscale = nonLocalMeans_Grayscale(saltNoised, params = (saltParams['bigWindow'], saltParams['smallWindow'],saltParams['h']), verbose = verbose)    
        #write images to file
        cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/Noised/Image' + str(index) + '-SPNOISE-GRAYSCALE.png', saltNoised)
        cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/Denoised/Image' + str(index) + '-NLM-Salted-GRAYSCALE.png', nlmFilteredSalted_Grayscale)
      else :
        #perform NLM filtering
        nlmFilteredSalted_RGB = nonLocalMeans_RGB(saltNoised, params = (saltParams['bigWindow'], saltParams['smallWindow'],saltParams['h']), verbose = verbose)
        #write images to file
        cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/Noised/Image' + str(index) + '-SPNOISE-RGB.png', saltNoised)
        cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/Denoised/Image' + str(index) + '-NLM-Salted-RGB.png', nlmFilteredSalted_RGB)
        
  if rician:
    # Paramètres du filtre NLM adaptés pour le bruit Ricien
    rParams = {
        'bigWindow': 20,
        'smallWindow': 6,
        'h': 10,  # Paramètre de similarité (h) ajusté pour le bruit Ricien
        'scale': scale,
    }
    
    #perform NLM filtering
    nlmFilteredRNoised = nonLocalMeans_Grayscale(ricianNoised, params = (rParams['bigWindow'], rParams['smallWindow'],rParams['h']), verbose = verbose)
    
    #write images to file
    cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/Noised/Image' + str(index) + '-RNOISE.png', ricianNoised)
    cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/Denoised/Image' + str(index) + '-NLM-Rician.png', nlmFilteredRNoised)

  print("--------COMPLETED IMAGE", index, '-----------')
