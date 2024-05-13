#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:23:05 2024

@author: selmafanani
"""
import os
import Denoise.python3
from Tests import Tests
from multiprocessing import Pool



if __name__ == '__main__':
  #multiprocessing allows us to parallely finish off all images!
	pool = Pool(processes=os.cpu_count())
	pool.map(Denoise.denoise, [1, 2, 3, 4, 14, 15, 16, 18])

# Tests
image_path1 = 'image1.png'
image_path2 = 'image2.png'
print(compare_images(image_path1, image_path2))

