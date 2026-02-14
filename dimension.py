import cv2

image = cv2.imread('me.png')

if image is not None:
    h,w,c = image.shape    #helps to get the dimensions of any image 
    print(f'Image loaded :\n Height = {h}\n Width = {w}\n channels = {c}')
else:
    print('Error : Cannot load the image ')