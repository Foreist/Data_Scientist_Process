#!/usr/bin/env python
# coding: utf-8

# In[32]:


from sklearn import model_selection
from sklearn.model_selection import train_test_split
from PIL import Image
import os, glob
import numpy as np


# ## 데이터 불러오기

# In[33]:


root_dir = 'C:/Users/301-1/Desktop/data/dummy/Python/MachineLearning/kfood/'


# ## 카테고리 지정

# In[50]:


categories = ['Chicken', 'Dolsotbab']


# In[51]:


nb_classes = len(categories)


# ## 이미지 크기 지정

# In[52]:


image_width = 64
image_height = 64


# ## 이미지 데이터 X, 레이블 Y

# In[53]:


[category for idx, category in enumerate(categories)]


# In[54]:


for i, j in enumerate(categories):
    print(j)


# In[56]:


X = []
Y = []
for idx, category in enumerate(categories):
    image_dir = root_dir + category
    # glob() 함수는 경로에 대응되는 모든 파일 및 디렉터리의 리스트를 반환합니다.
    files = glob.glob(image_dir + '/' + '*.jpg')
    print(image_dir + '/' + '*.jpg')
    
    for i, f in enumerate(files):
        print(i, f)
        img = Image.open(f)
        img = img.convert('RGB')
        img = img.resize((image_width, image_height)) # 64 * 64로 변경
        data = np.asarray(img)
        X.append(data)
        Y.append(idx)
        
X = np.array(X)
Y = np.array(Y)
print(X.shape, Y.shape)


# In[57]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
xy = (X_train, X_test, Y_train, Y_test)


# In[ ]:

#%%
import numpy as np
np.save(root_dir + 'koreanfood02.npy', xy)
print('데이터 로드 완료')

