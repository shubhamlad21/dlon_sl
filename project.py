# -*- coding: utf-8 -*-
"""deep_learning_old_to_new.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CkX2cpANcMsvprCNaRLHNIsHXfbkDTtD
"""
"""
from google.colab import drive
drive.mount('/content/drive')
"""
"""# **Image**"""

#pip install jupyter-dash
git clone https://github.com/shubhamlad21/dlon_sl.git dlon

cd dlon

from dlon import device
from dlon.device_id import DeviceId
device.set(device=DeviceId.GPU0)
import torch
if not torch.cuda.is_available():
    print('GPU not available.')

!pip install -r requirements-colab.txt

import fastai
from dlon.visualize import *
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

!mkdir 'models'
!wget https://www.dropbox.com/scl/fi/a20jp8dagw7y8nuzikq07/ColorizeArtistic_gen.pth -O ./models/ColorizeArtistic_gen.pth

mv ColorizeArtistic_gen.pth* /content/dlon/models/ColorizeArtistic_gen.pth

colorizer = get_image_colorizer(artistic=True)

source_url = 'https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-after/Landscape-BW.jpg' #@param {type:"string"}
render_factor = 40  #@param {type: "slider", min: 7, max: 40}
watermarked = True #@param {type:"boolean"}

if source_url is not None and source_url !='':
    image_path = colorizer.plot_transformed_image_from_url(url=source_url, render_factor=render_factor, compare=True, watermarked=watermarked)
    #show_image_in_notebook(image_path)
else:
    print('Provide an image url and try again.')

# @title
for i in range(40,41,1):
    colorizer.plot_transformed_image('test_images/image.png', render_factor=i, display_render_factor=False, figsize=(10,10))


#for i in range(20,41,20):
 #   colorizer.plot_transformed_image('test_images/image.png', render_factor=i, display_render_factor=True, figsize=(5,5))

"""# **Video**"""

!mkdir 'models'
!wget https://www.dropbox.com/scl/fi/ksfr8b0q2kfcdxxhfei2c/ColorizeVideo_gen.pth?rlkey=ub9cf9hberniwtxkhgeyclyzm&dl=0 -O ./models/ColorizeVideo_gen.pth

mv ColorizeVideo_gen.pth* /content/dlon/models/ColorizeVideo_gen.pth

vcolorizer = get_video_colorizer()

"""

---

"""

source_url = 'https://s3.amazonaws.com/tempmedia.tumblr.com/3aff2ed7dbefbcdd07d1b38865d12dc7/egjzxtfjp6gwsgow48cwokgc8_tumblr_tmp.mp4' #@param {type:"string"}
#'https://va.media.tumblr.com/tumblr_r0r9jfEuVr1wrnpgu_720.mp4'
render_factor = 40  #@param {type: "slider", min: 5, max: 40}
watermarked = True #@param {type:"boolean"}

if source_url is not None and source_url !='':
    video_path = vcolorizer.colorize_from_url(source_url, 'video.mp4', render_factor, watermarked=watermarked)
    show_video_in_notebook(video_path)
else:
    print('Provide a video url and try again.')

import imageio
from IPython.display import HTML

video = imageio.mimread('/content/dlon/video/result/video.mp4',memtest=False)  #Loading video
#video = [resize(frame, (256, 256))[..., :3] for frame in video]    #Size adjustment (if necessary)
HTML(display_video(video).to_html5_video())  #Inline video display in HTML5

# prompt: code to play the video from the result folder

video = imageio.mimread('/content/dlon/video/result/video.mp4',memtest=False)  #Loading video
HTML(display_video(video).to_html5_video())  #Inline video display in HTML5