from moviepy.editor import VideoFileClip, clips_array, vfx

clip1 = VideoFileClip("./test/tazi-video-1.mp4").subclip(5,15).margin(10)
clip2 = clip1.fx(vfx.mirror_x)
clip3 = clip1.fx(vfx.)
clip4 = clip3.fx(vfx.mirror_y)
final_clip = clips_array([[clip1,clip2], [clip3, clip4]])

#final_clip.write_videofile("my_stack.mp4", fps=25, codec='libx264')
final_clip.write_videofile("my_stack.mp4")