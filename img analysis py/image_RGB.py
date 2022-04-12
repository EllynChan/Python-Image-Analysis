#USED: https://medium.com/analytics-vidhya/how-to-calculate-rgb-values-for-some-images-in-python-ccf9abcea8f3
#Returns [name, red, green, blue, luminance, contrast, object condition, object type]


#Install all the things
from PIL import Image
import numpy as np
from tabulate import tabulate
import os
import csv
import glob

#set directory (change to whatever your directory is)
#dst_img = "C:\\Users\\Ellyn\\Desktop\\Python-Image-Analysis\\img analysis py\\Images"
#dst_img = "C:\\Users\\Palombo Lab\\Desktop\\Python-Image-Analysis\\img analysis py\\Images"

#set up for writing csv
header = ['Name', 'R', 'G', 'B', 'Luminance', 'Contrast', 'Thing/Object', 'Negative/Neutral']
data = []

for dst_img in glob.glob('C:\\Users\\Palombo Lab\\Desktop\\Python-Image-Analysis\\img analysis py\\Images\\*', recursive = True):
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

        #LUMI 0-255, higher means more intense formula: https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color
        #CONT higher means greater contrast in luminance of the img's grayscale: https://stackoverflow.com/questions/58821130/how-to-calculate-the-contrast-of-an-image
        #source of images used for testing: https://riptutorial.com/opencv/example/23407/adjusting-brightness-and-contrast-of-an-image-in-cplusplus

        if "Images_negthing" in dst_img:
            condition = "Negative"
            obj = "Thing"
        elif "Images_neuthing" in dst_img:
            condition = "Neutral"
            obj = "Thing"
        else:
            condition = "Neutral"
            obj = "Object"

        #record this row of csv data
        data.append([file_name, f'{R:.1f}', f'{G:.1f}', f'{B:.1f}', f'{(0.2126*R + 0.7152*G + 0.0722*B):.1f}', f'{newArr.std():.1f}', condition, obj])

#set path for the csv file
with open('C:\\Users\\Palombo Lab\\Desktop\\Python-Image-Analysis\\img analysis py\\analysisResult.csv', 'w') as f:
#with open('C:\\Users\\Ellyn\\Desktop\\Python-Image-Analysis\\img analysis py\\analysisResult.csv', 'w') as f:
    writer = csv.writer(f) #create the csv writer

    writer.writerow(header) #write the header

    writer.writerows(data) #write all rows of data

    print('data saved successfully')