import cv2
import mediapipe as mp
import pandas as pd
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

FILE_NAME = "Videos3/Ahmad1.mp4"
VIDEO_NAME = "Ahmad1last"
N_TPOINTS = 6

cap = cv2.VideoCapture(FILE_NAME)



out = cv2.VideoWriter('OUTPUT/'+VIDEO_NAME+".avi",
		cv2.VideoWriter_fourcc(*"MJPG"),
		fps = 60,frameSize=(1920,1080))
pose_lms = [0]*32
record = []
frame = 0
with mp_pose.Pose(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    frame+=1
    if not success:
      break
    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = pose.process(image)

    pose_lm = results.pose_landmarks

    if pose_lm:
        for position in results.pose_landmarks:
            for ide, lm in enumerate(position.landmark):
                pose_lms[ide]=lm


    record.append([frame,pose_lm])
    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    out.write(image)
    image = cv2.resize(image, (1920//2,1080//2))
    cv2.imshow('MediaPipe Pose', image)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
    	print(hand_lm_n)
    	break
cap.release()
out.release()

df = pd.DataFrame(record,columns=["frame","x","y"])