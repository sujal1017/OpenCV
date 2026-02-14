import cv2

image = cv2.imread("me.png")

if image is None:
    print("Error:cannot load the image")

else:
    print("Image loaded successfully")
    pt1 = (50,100)
    pt2 = (300,100)
    thickness = 4
    color = (255,0,0)

    cv2.line(image,pt1,pt2,color,thickness)
    cv2.imshow("Line Drawing image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()