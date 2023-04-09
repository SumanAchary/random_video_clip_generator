from moviepy.editor import *
import random

video = VideoFileClip('main.mp4')
audio = AudioFileClip('music.mp3')

max_duration = 10  # in seconds, which would be for the output video.

clips = []
total_duration = 0
while total_duration < max_duration:
    start_time = random.uniform(0, video.duration - 10)
    end_time = start_time + random.uniform(5, 10)
    duration = end_time - start_time
    clip = video.subclip(start_time, end_time)
    clips.append(clip)
    total_duration += duration

final_clip = concatenate_videoclips(clips)
final_clip = final_clip.set_audio(audio)

final_clip.write_videofile('output.mp4', fps=24)
