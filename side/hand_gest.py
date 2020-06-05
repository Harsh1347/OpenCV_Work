import cv2
import numpy as np
import os
from matplotlib import pyplot as plt 
import random
import pickle

DATADIR ="D:\\GitHub\\OpenCV_Work\\img"
CATEGORIES = ['peace','thumbup','okay']

# for category in CATEGORIES:
#     path = os.path.join(DATADIR,category)
#     for img in os.listdir(path):
#         img_array = cv2.imread(os.path.join(path,img),0)
#         plt.imshow(img_array,cmap='gray')
#         plt.show()
#         new_array = cv2.resize(img_array,(50,50))
#         plt.imshow(new_array,cmap='gray')
#         plt.show()
#         break
#     break

data = []
def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR,category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array,(50,50))
            data.append([new_array,class_num])
create_training_data()
print(len(data))
            
random.shuffle(data)

for sample in data[:10]:
    print(sample[1])

X=[]
y=[]

for features, label in data:
    X.append(features)
    y.append(label)

x = np.array(X).reshape(-1,50,50,1)

pickle_out = open("X.pickle",'wb')
pickle.dump(x,pickle_out)
pickle_out.close()

pickle_out = open("y.pickle",'wb')
pickle.dump(y,pickle_out)
pickle_out.close()

        

        
    