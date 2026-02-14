import cv2

image = cv2.imread("me.png")

if image is None:
    print("Error:Cannot load the image")

else:
    print("Image loaded successfully")

    center = (370,290)
    radius =100
    color = (0,255,0)
    thickness = 2

    cv2.circle(image,center,radius,color,thickness)

    cv2.imshow("Circled image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
