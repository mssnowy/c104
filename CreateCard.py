import cv2

img=cv2.imread('poster.jpg')
rocket=img[120:360,400:500]

img[0:240,500:600]=rocket

text_to_show='hello'
name_to_show='sisira'

cv2.putText(img,text_to_show,(20,220),
fontScale=1,fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,color=(0,0,255))

cv2.putText(img,name_to_show,(20,250),
fontScale=1,fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,color=(0,0,255))

cv2.imshow('output',img)
cv2.waitKey(0)