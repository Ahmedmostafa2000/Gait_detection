#importing necessary libraries
import cv2
import pandas as pd
import numpy as np


FILE_NAME = "Videos3/Ahmad_final.mp4"
VIDEO_NAME = "Ahmad_final_graph"

capture = cv2.VideoCapture(FILE_NAME)

out = cv2.VideoWriter('OUTPUT/'+VIDEO_NAME+".avi",
	cv2.VideoWriter_fourcc(*"MJPG"),
	fps = 30,frameSize=(1280,720))

df = pd.read_csv("Angles.csv")

frame = 0
print((int((527/527)*1280),int(df.iloc[400][1])))
print(len(df))


plot = np.zeros((720,1280,3))
while True:
	
	#reading realtime image
	success, image = capture.read()

	if not success:
		break
	if frame != 0 and df.iloc[frame][1]:
		cv2.line(plot,(int((frame/199)*1280),int(df.iloc[frame*2][1])),(int((frame/199)*1280),int(df.iloc[frame*2-1][1])),(0,255,0),2)


		image[:200,:] = plot[:200,:]
	frame+=1


	#showing the current frame
	cv2.imshow("Object",image)
	out.write(image)
	#to close the loop and end the app
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break
print(frame)
out.release()
capture.release()



