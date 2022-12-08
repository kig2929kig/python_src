from guizero import App, Text, Box, TextBox, PushButton
from pytube import YouTube
from pytube.cli import on_progress
import os

video_tit = ""

def btn() :
    
    global title_input
    url = title_input.value
    youtube_download(url.strip()) 
    #print(title_input.value)
    video_title = Text(title_box ,size=10 , width=35,align='left', text=video_tit[0:20]+"...", grid=[1,1])
     

def youtube_download(url) :
    global video_tit, button
    save_folder = "./youtube"
    if not os.path.exists(save_folder) :
        os.mkdir(save_folder)
    else :
        pass
    
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f'영상제목 : {yt.title}')
    video_tit = f'제목 : {yt.title}'
    down_clip = yt.streams.get_highest_resolution().download(save_folder)
    print(f'다운완료')
    
    # 자막
    caption = yt.captions.get_by_language_code('ko')
    #print(caption)
    
    if caption == None :
        caption = yt.captions.all()[0]
    
    #print(caption.xml_captions)     
    #print(caption.generate_srt_captions())
    caption.download(yt.title)
    
    
    
    
    

app = App(title="유튜브 다운로드 by kig2929kig", height=70, width=380, layout="grid")
title_box = Box(app, layout="grid", grid=[0,0])

title = Text(title_box, text="유튜브 URL : ", size=10, color="#ff0000", font="Arial", grid=[0,0] )
title_input = TextBox(title_box, text='ss', width=40, grid=[1,0])

button = PushButton(title_box, command=btn, grid=[0,1], text="다운로드")

app.display()