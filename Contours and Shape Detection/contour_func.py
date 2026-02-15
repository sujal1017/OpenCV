import cv2

img = cv2.imread(r"C:\Users\sujal\OneDrive\Desktop\Lang\python\openCV\circle.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)    #cv2.threshold(source, threshold_value, max_value, threshold_type)

contours,heirarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)       #cv2.findContours(image, retrieval_mode, approximation_method)

cv2.drawContours(img,contours,-1,(0,255,0),3)         #cv2.drawContours(image, contours, contourIndex, color, thickness)

cv2.imshow("Contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
