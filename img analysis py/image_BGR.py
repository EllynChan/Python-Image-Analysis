# FROM: https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv
#Returns [blue, green, red]
import cv2
import numpy
myimg = cv2.imread('insta.png')
avg_color_per_row = numpy.average(myimg, axis=0)
avg_color = numpy.average(avg_color_per_row, axis=0)
print(avg_color)

#for insta.png, should get [186.16561389 153.05188056 234.05469722]