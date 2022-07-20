"""
All images should have their background removed. You can use image editing tools to remove manually 
or use a script such as this: https://github.com/nadermx/backgroundremover
(this tool is already installed on the Palombo Lab laptop)

Returns [name, red, green, blue, luminance, contrast, object condition, object type]
"""

#Install all the things
from PIL import Image
import numpy as np
from tabulate import tabulate
import os
import csv
import glob
import skimage.measure  
from skimage import io

#set up for writing csv
header = ['Name', 'R', 'G', 'B', 'Luminance', 'Contrast', 'Entropy', 'Negative/Neutral', 'Thing/Object']
data = []

"""
goes through all folders under the Images folder
there should be 4 folders named like so: object_pair_negative, object_pair_neutral, thing_negative, thing_neutral.
For the things, negative/neutral refers to the things themselves, but for objects, it refers to the things they're paired with

Here are the parameters of this analysis: 
R/G/B: 0-255, Red/Green/Blue colour channel values. Original code: https://medium.com/analytics-vidhya/how-to-calculate-rgb-values-for-some-images-in-python-ccf9abcea8f3
LUMINANCE: range 0-255, higher means more intense. Formula: https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color
CONTRAST: higher means greater difference in luminance values within the pixels of the img's grayscale: https://stackoverflow.com/questions/58821130/how-to-calculate-the-contrast-of-an-image
ENTROPY: higher means more variance in the pixel values in a given sample. Shannon entropy formula: https://stackoverflow.com/questions/50313114/what-is-the-entropy-of-an-image-and-how-is-it-calculated

source of images used for testing: https://riptutorial.com/opencv/example/23407/adjusting-brightness-and-contrast-of-an-image-in-cplusplus

"""
for dst_img in glob.glob('Images\\*', recursive = True):
    #listing files in images folder
    list_img = os.listdir(dst_img)

    #iterating over dst_image to get the images as arrays
    for image in sorted(list_img):
    
        [file_name, ext] = os.path.splitext(image) #splitting file name from its extension
        arr = np.array(Image.open(os.path.join(dst_img, image))) #creating arrays for all the images

        arr_mean = np.mean(arr, axis=(0,1))
        R = arr_mean[0]
        G = arr_mean[1]
        B = arr_mean[2]
        newArr = np.array(Image.open(os.path.join(dst_img, image)).convert('L')) #converting to grayscale for calculating contrast

        if "negative" in dst_img:
            condition = "Negative"
        elif "neutral" in dst_img:
            condition = "Neutral"
        else:
            condition = "n/a"

        if "object" in dst_img:
            obj = "Object"
        elif "thing" in dst_img:
            obj = "Thing"
        else:
            obj = "n/a"

       
        img = io.imread(dst_img + "\\" + image)
        entropy = skimage.measure.shannon_entropy(img)

        #record this row of csv data
        data.append([file_name, f'{R:.1f}', f'{G:.1f}', f'{B:.1f}', f'{(0.2126*R + 0.7152*G + 0.0722*B):.1f}', f'{newArr.std():.1f}', f'{entropy:.1f}', condition, obj])

#set path for the csv file
with open('results.csv', 'w') as f:
    writer = csv.writer(f) #create the csv writer

    writer.writerow(header) #write the header

    writer.writerows(data) #write all rows of data

    print('data saved to path')