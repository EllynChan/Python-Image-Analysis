#USED: https://medium.com/analytics-vidhya/how-to-calculate-rgb-values-for-some-images-in-python-ccf9abcea8f3
#Returns [red, green, blue]

#Install all the things
from PIL import Image
import numpy as np
from tabulate import tabulate
import os

#set directory (change to whatever your directory is)
dst_img = "C:\\Users\\Ellyn\\Desktop\\Python-Image-Analysis\\img analysis py\\Images"
#dst_img = "C:\\Users\\Palombo Lab\\Desktop\\img analysis\\img analysis py\\Images"

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
    newArr = np.array(Image.open(os.path.join(dst_img, image)).convert('L'))

    #LUMI 0-255, higher means more intense formula: https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color
    #CONT 0-255, higher means greater contrast in luminance of the img's grayscale: https://stackoverflow.com/questions/58821130/how-to-calculate-the-contrast-of-an-image
    #source of images used for testing: https://riptutorial.com/opencv/example/23407/adjusting-brightness-and-contrast-of-an-image-in-cplusplus
    print(f'[{file_name}, R={R:.1f},  G={G:.1f}, B={B:.1f}, LUMI={(0.2126*R + 0.7152*G + 0.0722*B):.1f}, CONT={(newArr.std()):.1f}]')

#[for insta should be: R=234.1,  G=153.1, B=186.2 ]
