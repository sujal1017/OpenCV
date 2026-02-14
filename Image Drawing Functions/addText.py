import cv2

image = cv2.imread("me.png")

if image is None:
    print("Error:Cannot load the image")

else:
    print("Image loaded successfully")

    cv2.putText(image,'Hello python programmer',(50,100),cv2.FONT_HERSHEY_SIMPLEX,1.7,(0,255,0),2)
   #cv2.putText(image,"String u want to add",org,font,fontscale,color,thickness)
  
    cv2.imshow("Text added to image",image)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()
