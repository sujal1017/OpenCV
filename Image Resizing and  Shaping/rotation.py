import cv2
image = cv2.imread("me.png")

if image is None:
    print("Error, Cannot load the Image")
else:
    print("Image loaded Successfully")

    (h,w) = image.shape[:2]
    center = (w//2,h//2)

    M = cv2.getRotationMatrix2D(center,90,1.0)
    rotated = cv2.warpAffine(image,M,(w,h))

    cv2.imshow("Original image",image)
    cv2.imshow("Rotated image",rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()