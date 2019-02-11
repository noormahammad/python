from moviepy.editor import VideoFileClip, clips_array, vfx

clip1 = VideoFileClip("./samples-videos/obama.mp4").subclip(10,30).margin(10)
clip2 = clip1.fx(vfx.mirror_x)
clip3 = clip1.fx(vfx.mirror_y)
clip4 = VideoFileClip("./samples-videos/sample-2.mp4").margin(10)
final_clip = clips_array([[clip1, clip2], [clip3, clip4]])

final_clip.write_videofile("my_stack.mp4", fps=25, codec='libx264')
