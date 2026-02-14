import cv2

image = cv2.imread(r"C:\Users\sujal\OneDrive\Desktop\Lang\python\openCV\me.png")

blurred = cv2.GaussianBlur(image,(5,5),5) #(image,kernalsize(larger kernalsize more blur),SIGMA (Small sigma → Less smooth Large sigma → More smooth))

cv2.imshow("Original Image",image)
cv2.imshow("Blurred Image",blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()