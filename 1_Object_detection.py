#importing necessary libraries
import cv2
import pandas as pd

FILE_NAME = "Videos3/Ahmad1.mp4"
VIDEO_NAME = "Ahmad1last"
N_TPOINTS = 3

capture = cv2.VideoCapture(FILE_NAME)

success, image = capture.read()

image2 = cv2.resize(image, (1920//2,1080//2))
box = [[]]*N_TPOINTS

for i in range(N_TPOINTS):
	box[i] = list(cv2.selectROI("Tracked Object", image2 ,False))
	for j in range(4):
		box[i][j] *= 2
print(box)


# box = [[58, 868, 16, 26], [110, 772, 32, 30], [126, 688, 26, 24], [194, 692, 32, 26], [218, 766, 34, 26], [258, 852, 30, 34]]
for i in range(N_TPOINTS):
	# if i==0:
	# 	print('OUTPUT/'+VIDEO_NAME+f"{i}.avi")
	# 	capture = cv2.VideoCapture('OUTPUT/'+VIDEO_NAME+f"{i}.avi")
	# 	df = pd.read_csv("OUTPUT/"+VIDEO_NAME+f'{i}.csv')
	# 	continue
	# print(box)
	# print(box[i] or "Failed")
	out = cv2.VideoWriter('OUTPUT/'+VIDEO_NAME+f"{i}.avi",
		cv2.VideoWriter_fourcc(*"MJPG"),
		fps = 30,frameSize=(1920,1080))
	
	tracker = cv2.TrackerCSRT_create()
	success, image = capture.read()
	tracker.init(image, box[i])

	fps_record = []
	track_record = []
	fps_count = 0
	while True:
		#Counting fps
		fps_count+=1
		#Calculating fps
		timer = cv2.getTickCount()
		#reading realtime image
		success, image = capture.read()
		if not success:
			break
		success, box[i] = tracker.update(image)
		if success:
			if i != 0:
				if (int(df.iloc[fps_count][0]),int(df.iloc[fps_count][1]))!=(0,0):
					cv2.line(image,(int(df.iloc[fps_count][0]),int(df.iloc[fps_count][1])),
						(box[i][0]+box[i][2]//2,box[i][1]+box[i][3]//2),(0,255,0),5)


		cv2.circle(image, (box[i][0]+box[i][2]//2,box[i][1]+box[i][3]//2),10,(0,0,255),cv2.FILLED)
			
		
		#Calculating fps
		fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
		if success:
			fps_record.append(fps)
			track_record.append([box[i][0]+box[i][2]/2,box[i][1]+box[i][3]/2])
		else:
			if i!=0:
				track_record.append([int(df.iloc[fps_count][0]),int(df.iloc[fps_count][1])])
			else:
				track_record.append([0,0])
		out.write(image)
		#showing the current frame
		image = cv2.resize(image, (1920//2,1080//2))
		cv2.imshow("Object",image)

		#box is a tuple of initals, height and width x1,y1,h,w
		

		#to close the loop and end the app
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break
	# print(min(fps_record),max(fps_record),sum(fps_record)/len(fps_record))

	out.release()
	capture.release()
	if i != N_TPOINTS-1:
		capture = cv2.VideoCapture('OUTPUT/'+VIDEO_NAME+f"{i}.avi")
	cv2.destroyAllWindows()
	df = pd.DataFrame(track_record, columns = ['x','y'])
	df.to_csv("OUTPUT/"+VIDEO_NAME+f'{i}.csv')


