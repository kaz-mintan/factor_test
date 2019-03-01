#!/usr/bin/env python
# -*- coding: utf-8 -*-

from input_out import *

from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Activation

x_train = get_input()
y_train = get_output()

x_train = x_train.reshape(-1,135)
y_train = to_categorical(y_train,8)

x_train = x_train.astype('float32')
y_train = y_train.astype('float32')

X = x_train
Y = y_train

seed = 7
np.random.seed(seed)
fold_num = 5

cvscores = []

#for train, test in kfold.split(X, Y):
for i in range(x_train.shape[1]):
  x_train = get_input()
  y_train = get_output()

  x_train = x_train.reshape(-1,135)
  y_train = to_categorical(y_train,8)

  x_test = x_train[i:i+2,:]
  y_test = y_train[i:i+2,:]

  for k in range(2):
    x_train = np.delete(x_train,i,0)
    y_train = np.delete(y_train,i,0)

  model = Sequential()
  model.add(Dense(units=256,input_shape=(135,)))
  model.add(Activation('relu'))
  model.add(Dense(units=100))
  model.add(Activation('relu'))
  model.add(Dense(units = 8))
  model.add(Activation('softmax'))

  model.compile(loss='categorical_crossentropy',
                optimizer='sgd',
                metrics=['accuracy'])

  model.fit(x_train,y_train,
            batch_size = 1, epochs=10,verbose = 1,
            #validation_data = (x_train,y_train))
            validation_data = (x_test,y_test))

  #score = model.evaluate(x_train,y_train,verbose=1)
  score = model.evaluate(x_test,y_test,verbose=1)
  cvscores.append(score[1]*100)
  print('Test loss:',score[0])
  print('Test accuracy:',score[1])
  print(i)

print(np.mean(cvscores),np.std(cvscores))
sc = np.array(cvscores)
np.savenpy("cvscores",sc)

