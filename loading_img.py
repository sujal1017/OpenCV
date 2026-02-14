import cv2

image = cv2.imread('me.png')

if image is None:
    print('Error : Image not loaded')
else:
    print('Success : Image loaded successfully')