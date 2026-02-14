import cv2

image = cv2.imread("me.png")

if image is None:
    print("Error : Cannot load the image")

else:
    print("Image loaded Successfully")

    resize = cv2.resize(image,(300,300))

    cv2.imshow("Original Image", image)
    cv2.imshow("Resized image", resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
