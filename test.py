#%%
from moviepy.editor import *

clip = VideoFileClip("./samples-videos/sample-1.mp4").subclip(2,4)
clip.ipython_display(width=280)
