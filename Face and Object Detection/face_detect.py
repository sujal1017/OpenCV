import cv2

face_cascade = cv2.CascadeClassifier(r"C:\Users\sujal\OneDrive\Desktop\Lang\python\openCV\Face and Object Detectioon\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,5)

    """ detectMultiScale() - scan and detect faces
    1.1 balance,not too slow, blind 

    minNeighbors = 5"""

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    """
    x,y = top left corner
    (x+w,y+h) = bottom right
    faces = [
    (100,150,80,80) face 1
    (250,120,90,90) face 2
    ]

    x = how far from left
    y = how far from top 
    w = width of face
    h = hight of face
    """

    cv2.imshow("Webcam face detection",frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()