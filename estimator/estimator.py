# -*-coding: utf-8 -*-
import numpy as np
from scipy.stats import norm

gaze_datafile = ".csv"
head_datafile= ".csv"

gaze_x = 0
gaze_y = 1
head_x = 0
head_y = 1

CAM_NUM = 3
MOG_NUM = 7


#centre_x,centre_y,radius,conf
gaze_centre = np.array([[10,15,6,100],[10,5,25,75],[0,0,0,10],
                    [-12,0,10,100],[0,-5,10,80],[0,0,12,20],[0,0,0,0]],<
                    [[-20,15,5,80],[0,20,5,100],[20,5,5,80],
                    [0,0,30,20],[-18,-5,5,80],[10,-8,5,80],[5,0,5,80]],
                    [[0,0,0,0],[25,10,10,75],[-20,8,5,100],
                    [0,0,0,0],[0,10,10,60],[-12,-10,5,80],[5,-8,20,100]])

head_centre = np.array([[25,8,5,100],[45,-5,10,75],[40,-10,5,50],
                    [10,0,10,100],[30,2,5,80],[45,-15,5,40],[0,0,0,0]],
                    [[-10,-5,5,75],[6,3,5,100],[30,-2,2,75],
                    [-15,-7,5,80],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
                    [[0,0,0,0],[-15,-7,5,70],[-5,-5,5,100],
                    [-15,-10,3,40],[-20,-10,3,70],[-10,-10,5,80],[18,-7,3,100]])

gaze_data = np.loadtxt(gaze_datafile,delimiter=",")
head_data = np.loadtxt(head_datafile,delimiter=",")

for i in range(gaze_data.shape[0]):
    for cam in range(CAM_NUM):
        for mog in range(MOG_NUM):
          x = gaze_data[gaze_x,i]
          y = gaze_data[gaze_y,i]
          length = np.linalg.norm(np.array([x-gaze_centre[cam,mog],y-gaze_centre))
          t = norm.pdf(length,gaze_centre[3,gaze_centre[2])

