import cv2
import numpy as npy

black = npy.zeros([600,600])
#print(black)

f_row=black[1:2]
f_col=black[:,1:2]

black[200:400,200:400]=255

cv2.imshow('black',black)

cv2.waitKey(0)