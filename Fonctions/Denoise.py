#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:17:55 2024

@author: selmafanani
"""
import Log.python3
import cv2
import os
import AddNoise.python3
import NLMeans.python3



def denoise(index, verbose = True, gaussian = False, salted = True, rician = False):
  '''
  Helper function that:
  - takes an index
  - gets the images
  - adds noise
  - Denoises with various filters and logs the output
  - Saves all images

  '''
  print('DENOISING IMAGE', index)

  #For logistical purposes
  f = open('/Users/selmafanani/Downloads' +str(index)+'-LOG.csv','w')
  f.close()
  
  grayscale = False
  scale = 2 #Scale factor of the image
  gtImg = AddNoise.getImage(index, grayscale = grayscale, scale = scale)

  # Noise parameters
  sigma = 0.05 #Gaussian sigma
  p = 0.09 #Threshold for SNP noise
  sigma1 = 0.2 #Rician sigma

  gNoised = AddNoise.addNoise(gtImg, 'GAUSSIAN', sigma = sigma) 
  saltNoised = AddNoise.addNoise(gtImg, 'SALTNPEPPER', p = p)
  ricianNoised = AddNoise.addNoise(gtImg, 'RICIAN', sigma = sigma1)

  # Parameters for denoising using gaussian filter
 # kernelSize = 3
  #kernel = (kernelSize , kernelSize)
  
  if gaussian:
    #NLM filter parameters
    gParams = {
      'bigWindow' : 20,
      'smallWindow':6,
      'h':16,
      'scale':scale,
    }

    #perform NLM filtering
    nlmFilteredGNoised = NLMeans.nonLocalMeans(gNoised, params = (gParams['bigWindow'], gParams['smallWindow'],gParams['h']), verbose = verbose)

    #perform gaussian filtering
    #gFilteredGNoised = cv2.GaussianBlur(gNoised,kernel,0)
    
    #log the results
    #log(index, gtImg, gNoised, gFilteredGNoised, nlmFilteredGNoised,  gParams, gaussian = True)
    
    #write images to file
    cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/Noised/Image' + str(index) + '-GNOISE.png', gNoised)
    cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/Denoised/Image' + str(index) + '-NLM-Gauss.png', nlmFilteredGNoised)
    #cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/GT/Image' + str(index) + '-GF-Gauss.png', gFilteredGNoised)


  
  if salted:
    #NLM filter parameters
    saltParams = {
      'bigWindow' : 30,
      'smallWindow':6,
      'h':29,
      'scale':scale,
    }

    #perform NLM filtering
    nlmFilteredSalted = NLMeans.nonLocalMeans(saltNoised, params = (saltParams['bigWindow'], saltParams['smallWindow'],saltParams['h']), verbose = verbose)

    #perform gaussian filtering
    #gFilteredSalted= cv2.GaussianBlur(saltNoised,kernel,0)
    
    #log the results
    #log( index, gtImg, saltNoised, gFilteredSalted, nlmFilteredSalted,  saltParams, salted = True)
    
    #write images to file
    cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/Noised/Image' + str(index) + '-SPNOISE.png', saltNoised)
    cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/NLMFilter/Image' + str(index) + '-NLM-Salted.png', nlmFilteredSalted)
    #cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/GFilter/Image' + str(index) + '-GF-Salted.png', gFilteredSalted)
  
    cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/GT/Image' + str(index) + '-GT.png', gtImg)
  
  if rician:
    # Paramètres du filtre NLM adaptés pour le bruit Ricien
    rParams = {
        'bigWindow': 20,
        'smallWindow': 6,
        'h': 10,  # Paramètre de similarité (h) ajusté pour le bruit Ricien
        'scale': scale,
    }
    
    #perform NLM filtering
    nlmFilteredRNoised = NLMeans.nonLocalMeans(ricianNoised, params = (rParams['bigWindow'], rParams['smallWindow'],rParams['h']), verbose = verbose)

    #perform gaussian filtering
    #rFilteredRNoised = cv2.GaussianBlur(ricianNoised,kernel,0)
    
    #log the results
    #log(index, gtImg, ricianNoised, rFilteredRNoised, nlmFilteredRNoised,  rParams, rician = True)
    
    #write images to file
    cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/Noised/Image' + str(index) + '-RNOISE.png', ricianNoised)
    cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/Denoised/Image' + str(index) + '-NLM-Rician.png', nlmFilteredRNoised)
    #cv2.imwrite('/Users/selmafanani/Downloads/Dossier_MI/GT/Image' + str(index) + '-GF-Rician.png', rFilteredRNoised)

  print("--------COMPLETED IMAGE", index, '-----------')
