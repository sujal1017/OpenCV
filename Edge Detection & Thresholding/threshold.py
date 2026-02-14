# Thresholding is a technique used in image processing to separate objects from background.
# It converts a grayscale image into a simpler image (often black & white).

import cv2

image = cv2.imread(r"C:\Users\sujal\OneDrive\Desktop\Lang\python\openCV\me.png",cv2.IMREAD_GRAYSCALE)

ret,thres = cv2.threshold(image,120,255,cv2.THRESH_BINARY)    #cv2.threshold(src, thresh, maxval, type)


cv2.imshow("Original image",image)
cv2.imshow("Threshold image",thres)

cv2.waitKey(0)
cv2.destroyAllWindows() 


# If threshold = 50
# More white areas.
# If threshold = 200
# Very little white areas.
# Higher threshold → darker output.


# Used for:
# Object detection
# Background removal
# Document scanning
# OCR (text detection)
# Shape detection
# It simplifies the image.