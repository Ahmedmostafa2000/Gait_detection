#importing necessary libraries
import cv2
import pandas as pd
import numpy as np

def empty(a):
    pass





FILE_NAME = "Videos/Hesham1_light.mp4"
VIDEO_NAME = "Hesham1_light"



cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,300)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",19,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",110,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",240,255,empty)
cv2.createTrackbar("Val Min","TrackBars",153,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)


capture = cv2.VideoCapture(FILE_NAME)
# out = cv2.VideoWriter('output/'+VIDEO_NAME,
# 	cv2.VideoWriter_fourcc(*'MP4V'),
# 	fps = 30,frameSize = (720,480))
success, image = capture.read()
while True:
	
	if not success:
		print("Exiting")
		capture = cv2.VideoCapture(FILE_NAME)
		success, image = capture.read()
	
        
	image = cv2.resize(image, (1920//3,1080//3))
	imageHSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
	h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
	h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
	s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
	s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
	v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
	v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
	print(h_min,h_max,s_min,s_max,v_min,v_max)
	lower = np.array([h_min,s_min,v_min])
	upper = np.array([h_max,s_max,v_max])
	mask = cv2.inRange(imageHSV,lower,upper)
	imageResult = cv2.bitwise_and(image,image,mask=mask)

	cv2.imshow("Images", imageResult)
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break