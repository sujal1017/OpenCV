import cv2

image = cv2.imread("me.png")

if image is None:
    print("Error:Cannot load the image")

else:
    print("Image loaded successfully")

    pt1 = (270,170)
    pt2 = (500,400)
    color = (0,255,0)
    thickness = 2

    cv2.rectangle(image,pt1,pt2,color,thickness)

    cv2.imshow("Rectangled image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
