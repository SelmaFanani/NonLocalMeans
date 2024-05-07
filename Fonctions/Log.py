#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:19:01 2024

@author: selmafanani
"""
from skimage.metrics import peak_signal_noise_ratio, mean_squared_error


def log( index, gtImg, noisy, gfiltered, nlmfiltered,  params, gaussian = False, salted = False, rician = False):
  '''
  This function logs the results in a .csv file.
  The skimage library is used to compute the MSE and PSNR
  '''

  f = open('/Users/selmafanani/Downloads/Dossier_MI' +str(index)+'-LOG.csv','a')
  if gaussian:
    f.write('Gaussian Noise\n')
  elif salted:
    f.write('Salt and Pepper Noise\n')
  elif rician:
    f.write('Rician Noise\n')

  f.write('Params: ' + str(params) + '\n')
  f.write('NOISY,GAUSSIAN FILTER on NOISE,NLM FILTER on NOISE\n')
  f.write(str(peak_signal_noise_ratio(gtImg, noisy)))
  f.write(',')
  f.write(str(peak_signal_noise_ratio(gtImg, gfiltered)))
  f.write(',')
  f.write(str(peak_signal_noise_ratio(gtImg, nlmfiltered)))
  f.write('\n')
  f.write(str(mean_squared_error(gtImg, noisy)))
  f.write(',')
  f.write(str(mean_squared_error(gtImg, gfiltered)))
  f.write(',')
  f.write(str(mean_squared_error(gtImg, nlmfiltered)))
  f.write('\n\n')
  
