#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image,ImageOps
import image_slicer
import os


# In[2]:


directory = 'place_images_here/'
num_slices = 400


# In[3]:


# removing old tiles
for name in os.listdir('place_images_here/tiles/'):
    os.remove('place_images_here/tiles/' + name)
for name in os.listdir('place_images_here/tiles/'):
    os.remove('place_images_here/tiles/' + name)


# In[5]:


# scaling provided images
for name in os.listdir('place_images_here/'):
    if name.endswith('.png'):
        
        image_path = 'place_images_here/' + name
        
        im = Image.open(image_path)
        
        im = ImageOps.fit(im, (3200, 1600))
        
        im.save('place_images_here/' + 'scaled/' + name, format = 'PNG')


# In[7]:


# slicing scaled images
for i, name in enumerate(os.listdir('place_images_here/' + 'scaled')):
    
    if name.endswith('.png'):
        
        image_path = 'place_images_here/' + 'scaled/' + name
        
        im = Image.open(image_path)
        
        tiles = image_slicer.slice(image_path, num_slices, save=False, )
                
    
        image_slicer.save_tiles(tiles, directory=('place_images_here/' + 'tiles'),                            prefix=f'slice{i}', format='png')        

