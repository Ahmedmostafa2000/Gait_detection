#importing necessary libraries
import cv2
import pandas as pd
import mediapipe as mp


FILE_NAME = "Videos3/hesham1e30.mp4"
VIDEO_NAME = "hesham1e30mp"


capture = cv2.VideoCapture(FILE_NAME)
forcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('OUTPUT/'+VIDEO_NAME+".avi",
		cv2.VideoWriter_fourcc(*"MJPG"),
		fps = 60,frameSize=(1920,1080))




mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
fps_record = []
lm_record = []
frame_num = 0
while True:
	frame_num+=1
	#Calculating fps
	timer = cv2.getTickCount()
	#reading realtime image
	success, image = capture.read()
	
	if not success:
		break
	results = pose.process(image)
	if results.pose_landmarks:
		mpDraw.draw_landmarks(image,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
		for number, landmark in enumerate(results.pose_landmarks.landmark):
			h, w, c = image.shape
			if number in range(23,29):
				lm_record.append([frame_num,number,landmark.x,landmark.y])

	#Calculating fps
	fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
	if success:
		fps_record.append(fps)
	out.write(image)
	#showing fps
	cv2.putText(image,str(int(fps)),(600,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
	#showing the current frame
	image = cv2.resize(image, (1920//2,1080//2))
	cv2.imshow("Object",image)


	#to close the loop and end the app
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

df = pd.DataFrame(lm_record)
df.to_csv("A2.csv")
print(min(fps_record),max(fps_record),sum(fps_record)/len(fps_record))
out.release()
