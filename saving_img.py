import cv2

image = cv2.imread('me.png')          #(im=image) imread loads/reads the image 

if image is not None:
    success = cv2.imwrite('python_saved_img.png',image) # this will save the image (even if i make changes or not it will save if i run this program)
    if success:
        print('Image saved successfully')
    else:
        print('Image not saved')

else:
    print('Error : cannot save the image ')