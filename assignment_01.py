import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
Tk().withdraw()

print("select the image")
img_path = askopenfilename(title="chose Image")

if not img_path:
    print("No image selected")
    exit()

image = cv2.imread(img_path)
if image is None:
    print("Error: Cannot read the image file.")
    exit()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("GRAY SCALE IMAGE ", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Select location to save the gray scale image")
save_path = asksaveasfilename(
    title="Save image",
    defaultextension=".png"
)

if save_path:
    cv2.imwrite(save_path, gray)
    print(f"Image is saved at {save_path}")
else:
    print("Save cancelled.")
