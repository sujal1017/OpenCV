import cv2

image = cv2.imread("me.png")

if image is None:
    print("Error: Cannot load the image")

else:
    print("Image loaded successfully")

    crop = image[100:500, 200:400]

    cv2.imshow("Original image",image)
    cv2.imshow("Croppes image",crop)

    cv2.waitKey(0)
    cv2.destroyAllWindows()