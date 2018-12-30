import numpy as np
import cv2
import cv2.aruco as aruco

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    

    #operations on the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convort RGB format image into the gray format 
    aruco_dict = aruco.Dictionary_get(aruco.DICT_7X7_1000)
    parameters = aruco.DetectorParameters_create()
    corners, ids, _ = aruco.detectMarkers(gray,aruco_dict , parameters = parameters)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(gray, "id = "+str(ids), (100,200), font, 1, (255,0,255), 2, cv2.LINE_AA)
   
    cv2.imshow('frame',gray) #display the image onto the frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
