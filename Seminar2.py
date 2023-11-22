####seminar2 of video coding course, documents from Daniele Bellomo

import subprocess as sp

class s2:
##ex1
    def cut9sec(input,output):
        cut=[
            'ffmpeg',
            '-sseof','-9',
            '-i',input,
            '-c', 'copy',
            output
        ]
        sp.run(cut)


    ##cut9sec('big_buck_bunny.mp4', '/mnt/c/Users/danie/PycharmProjects/VideoCoding/bbb_cut9sec.mp4')

##ex2
    def boxing(input,output):
        output_cut='output_cut.mp4'
        duration=[
                  'ffmpeg',
                  '-ss', '00:00:00'
                  '-to', '00:00:50',
                  '-i', input,
                  '-c', 'copy',
                  output_cut
        ]
        sp.run(duration)

        out_mono='output_mp3mono.mp3'
        mp3_mono=[
            'ffmpeg',
            '-i',output_cut,
            '-ac','1',
            '-ar','44100',
            '-b:a','192k',
            out_mono
        ]
        sp.run(mp3_mono)
        out_stereo='output_mp3stereo.mp3'
        mp3_stereo=[
            'ffmpeg',
            '-i', output_cut,
            '-ac', '2',
            '-ar', '44100',
            '-b:a','128k',
            'stereo_mp3.mp3'
        ]
        sp.run(mp3_stereo)
        video_aac='bbb_aac.mp4'
        aac_cod=[
            'ffmpeg',
            '-i', output_cut,
            '-c:v',' copy',
            '-c:a', 'libfdk_aac',
            '-vbr',' 3',
            video_aac
        ]
        sp.run(aac_cod)
        output_aac='output_audio.aac'
        aac_cod2=[
            'ffmpeg',
            '-i', video_aac,
            '-vn', '-acodec',
            'copy',
            output_aac
        ]
        sp.run(aac_cod2)
        boxing_audio=[
            'ffmpeg',
            '-i', output_cut,
            '-i',mp3_mono,
            '-i', mp3_stereo,
            '-i', output_aac,
            '-map', '0:v',
            '-map', '1:a',
            '-map','2:a',
            '-map','3:a',
            '-c:v','copy',
            '-c:a','aac',
            '-b:a','192k',
        output
        ]
        sp.run(boxing_audio)


    ##boxing('big_buck_bunny.mp4', '/mnt/c/Users/danie/PycharmProjects/VideoCoding/bbb_newbox.mp4')
    def count_track(input):

         number_of_tracks = [
            'ffprobe',
            '-i', input,
            '-show_streams',
            '-select_streams', f'a:0',
         ]
         sp.run(number_of_tracks)
    ##count_track('insert the name of the file you want to process')
##ex4
    def add_subtitles(input,link,output):
        subtitles_srt='output_subtitles.srt'
        download_subt=[
            'ffmpeg',
            '-i', link,
            '-scodec', 'srt',
            subtitles_srt
        ]
        sp.run(download_subt)
        add_sub=[
            'ffmpeg',
            '-i', input,
            '-vf', 'subtitles=subtitles_srt',
            output
        ]
        sp.run(add_sub)
    ##add_subtitles('insert name of the video','insert the link to get the subtitles',' insert name output file')
##ex6
    def extract_yuv(input,output):
        ex_yuv=[
            'ffmpeg',
            '-i',input,
            '-vf',
            'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay',
            output
        ]
        sp.run(ex_yuv)
    ##extract_yuv('insert the name of the video','insert a name for the output')