# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:38:24 2019

@author: 301-1
"""

#%%
import sys, os
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
from keras.models import load_model
from PIL import Image
import numpy as np
#%%
root_dir = "C:/Users/301-1/Desktop/data/dummy/Python/MachineLearning/kfood/"
image_files = [root_dir+"test_img/dosobab01.png",
root_dir+"test_img/test_chicken01.png",
root_dir+"test_img/test_chicken02.png"]
#%%
image_size = 64
nb_classes = len(image_files)
categories = ["Chicken", "Dolsotbab"]
#%%
X = []
files = []
# 이미지 불러오기 (2)
for fname in image_files:
    print(fname)
    img = Image.open(fname)
    img = img.convert("RGB")
    img = img.resize((image_size, image_size))
    in_data = np.asarray(img)
    in_data = in_data.astype("float") / 256
    X.append(in_data)
    files.append(fname)
print(X)
print(files)
#%%
X = np.array(X)
# 모델 파일 읽어오기 (3)
model = load_model(root_dir + 'koreanfood02_model.h5')
# 예측 실행 (4)
pre = model.predict(X)
# 예측 결과 출력 (5)
for i, p in enumerate(pre):
    y = p.argmax()
    print("입력:", files[i])
    print("예측:", "[", y, "]", categories[y], "/ Score",p[y])
