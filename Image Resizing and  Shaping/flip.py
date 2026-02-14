import cv2

image = cv2.imread("me.png")
# image.subset[3,3]

if image is None:
    print("Error:cannot find the image")
else:
    print("Image loaded successfully")

    small = cv2.resize(image, (300, 300))


    flip_horizontal = cv2.flip(small,1)
    flip_vertical = cv2.flip(small,0)
    flip_both = cv2.flip(small,-1)

    cv2.imshow("Original image",small)
    cv2.imshow("Horiontal image",flip_horizontal)
    cv2.imshow("Vertical image",flip_vertical)
    cv2.imshow("Both image",flip_both)

    cv2.waitKey(0)
    cv2.destroyAllWindow()
