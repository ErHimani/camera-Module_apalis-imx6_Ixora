import cv2
cap = cv2.VideoCapture('imxv4l2videosrc device=\"/dev/video2\" ! videoconvert ! appsink')
while(True):
    # Capture frame-by-frame
	ret, frame = cap.read()
	image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      # Display the resulting frames
	cv2.imshow('frame',frame)
	cv2.imshow('gray',image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()