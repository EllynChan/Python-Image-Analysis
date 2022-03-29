#USED: https://medium.com/analytics-vidhya/how-to-calculate-rgb-values-for-some-images-in-python-ccf9abcea8f3
#Returns [red, green, blue]

#Install all the things
from PIL import Image
import numpy as np
from tabulate import tabulate
import os

#set directory (change to whatever your directory is)
dst_img = "C:\\Users\\Ellyn\\Desktop\\img analysis py\\Images"

#listing files in images folder
list_img = os.listdir(dst_img)

#iterating over dst_image to get the images as arrays
for image in sorted(list_img):
    [file_name, ext] = os.path.splitext(image) #splitting file name from its extension
    arr = np.array(Image.open(os.path.join(dst_img, image))) #creating arrays for all the images
    [h, w] = np.shape(arr)[0:2]#calculating height and width for each image
    arr_dim = arr.ndim #calculating the dimension for each array
    arr_shape = arr.shape #calculating the shape for each array
    if arr_dim == 2:
        arr_mean = np.mean(arr)
        print(f'[{file_name}, greyscale={arr_mean:.1f}]')
    else:
        arr_mean = np.mean(arr, axis=(0,1))
        if len(arr_mean) == 3: #RGB CASE
            R = arr_mean[0]
            G = arr_mean[1]
            B = arr_mean[2]

            #LUMI formula: https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color
            print(f'[{file_name}, R={R:.1f},  G={G:.1f}, B={B:.1f}, LUMI={(0.2126*R + 0.7152*G + 0.0722*B):.1f} ]')
        else: #ALPHA CASE
            print(f'[{file_name}, R={R:.1f}, G={G:.1f}, B={B:.1f}, ALPHA={arr_mean[3]:.1f}]')




#[for insta should be: R=234.1,  G=153.1, B=186.2 ]
