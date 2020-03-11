import numpy as np
import cv2



cap = cv2.VideoCapture("v4l2src device=\"/dev/video3\" !  videoconvert ! appsink")

cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame',480,320)
cv2.namedWindow('gray',cv2.WINDOW_NORMAL)
cv2.resizeWindow('gray',480,320)


while(True):
    # Capture frame-by-frame
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#Display the resulting frame
	cv2.imshow('frame',frame)
	cv2.imshow('gray',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()