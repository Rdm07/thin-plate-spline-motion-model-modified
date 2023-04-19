import os, copy
from PIL import Image
import numpy as np

os.chdir(os.path.dirname(__file__))

image = np.array(Image.open('example2.png'),dtype=np.uint8)[:,:,:3]
# print(image.shape)

img_array = np.array([image[:,x:x+256] for x in range(0,2304,256)], dtype=np.uint8)


for i in range(len(img_array)):
    img = Image.fromarray(img_array[i])
    img.save('example2_{}.png'.format(i))