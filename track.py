import cv2

vid = cv2.VideoCapture(0)
while vid.isOpened():
	ret, orginal = vid.read()
	img = orginal

	img = cv2.GaussianBlur(img, (9, 9), 2)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	img = cv2.inRange(img, (25, 130, 130), (37, 255, 255))

	contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

	if len(contours) > 0:
		ball = sorted(contours, key=cv2.contourArea)[-1]
		(x, y), r = cv2.minEnclosingCircle(ball)
		cv2.circle(orginal, (int(x), int(y)), int(r), (0, 0, 255), 5)

	cv2.imshow("Image", orginal)
	if cv2.waitKey(1) & 0xff == ord('q'):
		break

vid.release()
cv2.destroyAllWindows()
