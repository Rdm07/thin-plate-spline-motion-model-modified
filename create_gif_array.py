import imageio
import numpy as np

from PIL import Image

gif1 = imageio.get_reader('results/result_nemo_1_advait_5.gif')
gif2 = imageio.get_reader('results/result_nemo_1_advait_10.gif')
gif3 = imageio.get_reader('results/result_nemo_1_advait_15.gif')
gif4 = imageio.get_reader('results/result_nemo_1_advait_20.gif')
gif5 = imageio.get_reader('results/result_nemo_1_advait_25.gif')

# source_img1 = imageio.imread('assets/source_vox_priyavrat.png')
# source_img2 = imageio.imread('assets/source_vox_advait.jpg')
# source_img3 = imageio.imread('assets/source_vox_varun.jpg')
# source_img4 = imageio.imread('assets/source_vox_fed.jpg')
# source_img5 = imageio.imread('assets/source_vox_nadal.jpg')

# source_img1 = np.array(Image.fromarray(source_img1).resize((256, 256))).astype(np.uint8)[:,:,:3]
# source_img2 = np.array(Image.fromarray(source_img2).resize((256, 256))).astype(np.uint8)[:,:,:3]
# source_img3 = np.array(Image.fromarray(source_img3).resize((256, 256))).astype(np.uint8)[:,:,:3]
# source_img4 = np.array(Image.fromarray(source_img4).resize((256, 256))).astype(np.uint8)[:,:,:3]
# source_img5 = np.array(Image.fromarray(source_img5).resize((256, 256))).astype(np.uint8)[:,:,:3]

driving_gif = imageio.get_reader('assets/driving_nemo_smile1.gif')

number_of_frames = gif1.get_length()

gif_array = []
for frame_number in range(number_of_frames):
    d_img = driving_gif.get_next_data()
    d_img = np.array(Image.fromarray(d_img).resize((256, 256))).astype(np.uint8)[:,:,:3]

    img1 = gif1.get_next_data().astype(np.uint8)[:,:,:3]
    img2 = gif2.get_next_data().astype(np.uint8)[:,:,:3]
    img3 = gif3.get_next_data().astype(np.uint8)[:,:,:3]
    img4 = gif4.get_next_data().astype(np.uint8)[:,:,:3]
    img5 = gif5.get_next_data().astype(np.uint8)[:,:,:3]

    # blank_image = np.ones(shape=source_img1.shape).astype(np.uint8)*255
    
    # print(blank_image.shape, source_img1.shape, d_img.shape, img1.shape)
    # new_image1 = np.hstack((blank_image, source_img1, source_img2, source_img3, source_img4, source_img5))
    new_image2 = np.hstack((d_img, img1, img2, img3, img4, img5))

    # new_image = np.vstack((new_image1, new_image2))
    gif_array.append(new_image2)

imageio.mimsave(uri='results/nemo_smile1_advait.gif', ims=gif_array)