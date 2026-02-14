# Canny is an algorithm used to detect edges (boundaries) in an image.

# Edges are areas where:
# Pixel intensity changes sharply
# Color changes sharply

# Example:
# Boundary of a face
# Edge of an object
# Borders of shapes


import cv2

image = cv2.imread(r"C:\Users\sujal\OneDrive\Desktop\Lang\python\openCV\me.png",cv2.IMREAD_GRAYSCALE)

edge = cv2.Canny(image,50,150)        #cv2.Canny(image, threshold1, threshold2)

cv2.imshow("Original Image",image)
cv2.imshow("Edges",edge)

cv2.waitKey(0)
cv2.destroyAllWindows()