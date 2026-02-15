    roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray,1.1,10)
        if len(eyes) > 0:
            cv2.putText(frame, "Eyes Detected",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX)

        smile = smile_cascade.detectMultiScale(roi_gray,1.1,10)
        if len(smile) > 0:
            cv2.putText(frame, "Smiling",(x,y-20),cv2.FONT_HERSHEY_SIMPLEX)
