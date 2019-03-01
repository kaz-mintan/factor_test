# -*-coding: utf-8 -*-
import numpy as np

def get_input():

  data1 = np.loadtxt("/home/kazumi/prog/table_design/euler_test1.csv",delimiter=",")
  data2 = np.loadtxt("/home/kazumi/prog/table_design/euler_test2.csv",delimiter=",")
  data3 = np.loadtxt("/home/kazumi/prog/table_design/euler_test3.csv",delimiter=",")

  gaze = np.loadtxt("/home/kazumi/prog/table_design/pic/gaze_test2.csv",delimiter=",")

  face= np.loadtxt("/home/kazumi/prog/table_design/pic/face_pt.csv",delimiter=",")

  length = 670

  eu_1 = np.zeros((4,length))
  eu_2 = np.zeros((4,length))
  eu_3 = np.zeros((4,length))

  face_pt= np.zeros((length,face.shape[1]))

  for jj in range(face.shape[0]):
    for kk in range(length):
      if face[jj,0] == kk:
        face_pt[kk,:] = face[jj,:]

#fig = plt.figure()
  for i in range(3):
    eu = np.empty((4,length))
    if i == 0:
      data = data1
    if i == 1:
      data = data2
    if i == 2:
      data = data3
    for j in range(data1.shape[0]):
      for k in range(length):
        if data[j,0] == k:
          eu[:,k] = data[j,:] 
        #else:
        #  eu[:,j] = np.array([None,None,None])

    if i == 0:
      eu_1 = eu
    if i == 1:
      eu_2 = eu
    if i == 2:
      eu_3 = eu


  face = np.hstack((face_pt[:,1:3],face_pt[:,7:9],
    face_pt[:,9:11],face_pt[:,15:17],
    face_pt[:,17:19],face_pt[:,23:]))

  set_data = np.hstack((eu_1[1:,:].T,eu_2[1:,:].T,eu_3[1:,:].T,
    gaze[:,1:],
    face))


  in_data = np.empty((5,set_data.shape[1],length-4))
  input_data = np.empty((5*set_data.shape[1],length-4))

  for i in range(4,666):
    for j in range(5):
      in_data[j,:,i] = set_data[i,:]
    input_data[:,i] = np.hstack((in_data[0,:,i],in_data[1,:,i],in_data[2,:,i],in_data[3,:,i],in_data[4,:,i]))

  return input_data


def get_output():
  length = 670 -4
  out = np.zeros((length,1))
  out[129:183,0] = 1.0
  out[183:275] = 2.0
  out[275:349] = 3.0
  out[349:423] = 4.0
  out[423:487] = 5.0
  out[487:546] = 6.0
  out[546:636] = 7.0
  return out

def make_input(data,length):
  print("now dummy")
  return 0
