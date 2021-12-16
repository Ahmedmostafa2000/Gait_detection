import math
import pandas as pd
import numpy as np

#calculating angles
hip = pd.read_csv("OUTPUT/Ahmad/Ahmad12.csv")
knee = pd.read_csv("OUTPUT/Ahmad/Ahmad11.csv")
anckle = pd.read_csv("OUTPUT/Ahmad/Ahmad10.csv")


vector_hip_knee = knee-hip
vector_knee_anckle = knee-anckle

cos_knee_joint = (vector_hip_knee*vector_knee_anckle)/(np.linalg.norm(vector_hip_knee)*np.linalg.norm(vector_knee_anckle))

knee_joint_angle = np.arccos(cos_knee_joint)*180/math.pi

knee_joint_angle.to_csv("Ahmad_Angles.csv")

