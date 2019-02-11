from moviepy.editor import *

clip1 = VideoFileClip("./samples-videos/sample-1.mp4").subclip(2,4)
clip2 = VideoFileClip("./samples-videos/sample-2.mp4").subclip(10,13)

movie = concatenate_videoclips([clip1, clip2])

movie.write_videofile("movie1.mp4", fps=25, codec="libx264")

