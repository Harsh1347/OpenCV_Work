import tensorflow as tf
import cv2
import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten,Conv2D,MaxPool2D

X = pickle.load(open("X.pickle",'rb'))
y = pickle.load(open("y.pickle",'rb')) 

X= X/255
X = np.array(X)
y = tf.keras.utils.to_categorical(y,3)

model = Sequential()
model.add(Conv2D(64,(3,3),input_shape = X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPool2D(pool_size = (2,2)))

model.add(Conv2D(64,(3,3)))
model.add(Activation("relu"))
model.add(MaxPool2D(pool_size = (2,2)))
model.add(Flatten())
model.add(Dense(64))
model.add(Activation("relu"))

model.add(Dense(3))
model.add(Activation('softmax'))

model.compile(loss="categorical_crossentropy",
                optimizer="adam",
                metrics=['accuracy'])

model.summary()

model.fit(X,np.array(y),epochs = 5)

model.save('gest.h5')

