import cv2

image = cv2.imread('me.png')
subset = image[3,3]

if image is not None:
    cv2.imshow('This is my image', image)   #open the window, imshow helps to dispplay the image
    cv2.waitKey(0)                          #waits for the key
    cv2.destroyAllWindows()                #close the window
    print('Success : Displayed the image successfully')

else:
    print('Error : Cannot display the image')