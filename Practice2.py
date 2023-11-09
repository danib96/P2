###this script it's made to have an interactive flow, if you'd prefer to use the code
###without any interaction, just comment those lines. The output line is meant to save the file
###in a path for my computer,if you'd like to save it in yours please change the path to one useful
###for you.

##made by Daniele Bellomo

import subprocess as sp

####exercise1
x=input("convert the video Big Buck Bunny into mpeg2 and save its info, press enter to continue")
def convert_bbb(input,output):
    conversion=[
        'ffmpeg',
        '-i', input,
        output
    ]
    sp.run(conversion)

    video_info=[
        'ffmpeg',
        '-i', output
    ]
    sp.run(conversion)
    sp.run(video_info)

convert_bbb('big_buck_bunny.mp4', '/mnt/c/Users/danie/PycharmProjects/VideoCoding/bbb_output.mpeg')

###exercise2
x=input("change the resolution of the video Big Buck Bunny, press enter to continue")
y=input("insert the width you want for the new video(numbers only),and press enter")
z=input("insert the height you want for the new video(numbers only),and press enter")
width=int(y)
height=int(z)

def change_res(input, output, width, height):

    resolution = [
        'ffmpeg',
        '-i', input,
        '-vf', f'scale={width}:{height}',
        output
    ]
    sp.run(resolution)

change_res('big_buck_bunny.mp4', '/mnt/c/Users/danie/PycharmProjects/VideoCoding/bbb_changedres.mp4', width,height)

##exercise3
x=input('insert the format you want to use for the conversion(ex.yuv420p) and press enter')
format=x
def chroma_subsampling(input, output,format):  #format is the new format we want the video to be converted

    chroma = [
        'ffmpeg',
        '-i', input,
        '-vf', f'format='+str(format),
        output
    ]
    sp.run(chroma)


chroma_subsampling('big_buck_bunny.mp4', '/mnt/c/Users/danie/PycharmProjects/VideoCoding/bbb_chroma.mp4',format)

##EX4

x=input("Let's get some useful information about our video, press enter to continue")
import cv2

def read_print_videodata(input):
    v_data=cv2.VideoCapture(input)
    fps=v_data.get(cv2.CAP_PROP_FPS)
    print('Frames per second : ', fps, 'FPS')
    f_count=v_data.get(cv2.CAP_PROP_FRAME_COUNT)
    print('Number of Frames  : ', f_count, 'Frames')
    v_format=v_data.get(cv2.CAP_PROP_FORMAT)
    print('Video Format : ', v_format)
    f_width=v_data.get(cv2.CAP_PROP_FRAME_WIDTH)
    print('Frame Width : ', f_width)
    f_height = v_data.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print('Frame Height : ', f_height)


read_print_videodata('big_buck_bunny.mp4')

x=input('convert the video into black and white, press enter to continue')
##ex5
from rgb_yuv import convert_to_bw
convert_to_bw('big_buck_bunny.mp4','/mnt/c/Users/danie/PycharmProjects/VideoCoding/bbb_blackandwhite.mp4')