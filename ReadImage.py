import cv2
img = cv2.imread('butterfly.jpg')
cv2.imshow('displayimage',img)


grey_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

cv2.imshow('greyscale',grey_img)
cv2.waitKey(0)