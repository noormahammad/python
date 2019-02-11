from moviepy.editor import *

clip1 = VideoFileClip("./samples-videos/sample-1.mp4").subclip(2,4)
clip1 = clip1.volumex(0.5)
clip2 = VideoFileClip("./samples-videos/sample-2.mp4").subclip(10,13)
clip2 = clip2.volumex(1.5)

txt_clip = TextClip("Hello World",fontsize=90, color='red')

txt_clip = txt_clip.set_position('center').set_duration(3)

movie = concatenate_videoclips([clip1, clip2])

final_movie = CompositeVideoClip([movie,txt_clip])

final_movie.write_videofile("movie1.mp4", fps=25, codec="libx264")

