import moviepy.video.io.VideoFileClip as moviepy_clip
from pathlib import Path
import cv2

def extract_audio(my_video):
    video_file=Path(my_video)
    video=moviepy_clip.VideoFileClip(str(video_file))
    audio_output_path = video_file.with_suffix('.mp3')
    if video.audio is not None:
       print('extracting audio track')
       video.audio.write_audiofile(str(audio_output_path))
       print('saved successfully')
    else:
        print('no audio found in this video')
        audio_output_path=None
    video.close()
    return audio_output_path

def extract_frames(my_video):
    video_file=Path(my_video)
    output_folder=video_file.parent
    output_folder.mkdir(exist_ok=True)
    print('extracting video frames')
    capture=cv2.VideoCapture(str(video_file))
    fps=capture.get(cv2.CAP_PROP_FPS)
    if fps==0:
        print('error in reading the frame rate of the video')
        return []
    saved_frames=[]
    frame_count=0
    image_count=0
    while True:
        success,frame=capture.read()
        if not success:
            break
        if frame_count % int(fps)==0:
            frame_filename=output_folder
            cv2.imwrite(str(frame_filename),frame)
            saved_frames.append(str(frame_filename))
            image_count+=1
        frame_count+=1
    capture.release()
    print('frames processed successfully')
    return saved_frames

def run_all_preprocesssing(my_video):
    print('starting prerprocessing')
    audio_file=extract_audio(my_video)
    frame_list=extract_frames(my_video)
    return {'audio path:':audio_file,'video_path':frame_list}