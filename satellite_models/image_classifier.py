#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
import os
import imageio
import numpy as np
import pandas as pd
import tensorflow as tf


# In[2]:


image_source = 'place_images_here/tiles/'


# In[9]:


images = []
for name in os.listdir(image_source):
    im = imageio.imread(image_source + '/' + name)
    im = im[:,:,:3]
    images.append(im)
images = np.array(images)


# In[10]:


model = tf.keras.models.load_model('stored_image_classifier')


# In[11]:


predictions = model.predict(images)


# In[12]:


print(predictions)


# In[ ]:




