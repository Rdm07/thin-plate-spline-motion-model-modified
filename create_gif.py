import os, copy
import imageio
import numpy as np

from skimage.transform import rescale
from skimage import io, img_as_float32
from skimage.transform import rescale
from skimage.color import gray2rgb

os.chdir(os.path.dirname(__file__))

def make_gif(name, frame_shape):
    """
    Read video which can be:
      - an image of concatenated frames
      - '.mp4' and'.gif'
      - folder with videos
    """

    if os.path.isdir(name):
        frames = sorted(os.listdir(name))
        num_frames = len(frames)
        video_array = np.array(
            [img_as_float32(io.imread(os.path.join(name, frames[idx]))) for idx in range(num_frames)])
    elif name.lower().endswith('.png') or name.lower().endswith('.jpg'):
        image = io.imread(name)

        if len(image.shape) == 2 or image.shape[2] == 1:
            image = gray2rgb(image)

        if image.shape[2] == 4:
            image = image[..., :3]
        
        image = img_as_float32(image)
        image = rescale(image, 4, multichannel=True, anti_aliasing=True)

        img_h, img_w, img_c = image.shape
        if img_h != frame_shape[0] and img_w != frame_shape[0]:
            raise Exception("Check Frame Shape")
        
        video_array = np.array([image[x:x+frame_shape[0], y:y+frame_shape[0]] for x in range(0,img_h,frame_shape[0]) for y in range(0,img_w,frame_shape[0])])

    video_array = (video_array*255).astype(np.uint8)

    return video_array

dirname = 'nemo'

for dir in os.listdir(dirname):
    subdirname = os.path.join(dirname, dir)
    if os.path.isdir(subdirname):
        for filename in os.listdir(subdirname):
            file_path = os.path.join(subdirname, filename)
            video_array = make_gif(file_path, (256,256))
            file_name_only = filename.split('.')[0]
            gif_name = file_name_only+'.gif'
            gif_path = os.path.join(subdirname, gif_name)
            imageio.mimsave(gif_path, video_array)
