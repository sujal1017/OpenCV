import cv2

image = cv2.imread("me.png")


if image is not None:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("GRAY SCALE IMAGE ", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Error : Cannot convert the image to GRAY SCALE")