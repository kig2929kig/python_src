# _*_ coding : utf-8 _*_

import os, eyed3, io
from guizero import App, ListBox, PushButton, Text, Picture, Window, TextBox, Slider
from PIL import Image
from subprocess import Popen

path="C:\music\\"
flag = 1

def show_files() :
    show_file = []
    
    files = os.listdir(path)

    for f in files:
        show_file.append(f)
    return show_file

def select(value) :
    tag.value = "가수 : " 
    v = value
    
        
    audio = eyed3.load(path + v)
    tag.value = tag.value + audio.tag.artist + "\n" + "앨범 : " + audio.tag.album + "\n" + "타이틀 : " + audio.tag.title
    
    imgs = audio.tag.images
    
    for img in imgs :
        #print(img.image_data)
        print(img.mime_type)
        print(img.picture_type)
        print(img.description)
        
        picture.image = Image.open(io.BytesIO(img.image_data))
        
        for i in audio.tag.lyrics :
            #print(lyrics.text)
            lyrics.value = i.text
         
    return v

def play() :
    v = listbox.value.replace(" ", "\ ") #음악파일 공백 처리
    os.system('killall -9 vlc')
    v = 'cvlc -Z ' + path + v + ' &'
  
    os.system(v)
    
def stop() :
    os.system('killall -9 vlc')
        

def volume(value):
    value = str(value)
    os.system('amixer set Master ' + value + '%')
        
    
app =App(title="Music Player", height=600)
window = Window(app, title="가사")

#tkinter : app.tk.
print(app.tk.winfo_x())
print(app.tk.winfo_y())

#위치 변경
window.tk.geometry("+600+87")
 
listbox = ListBox(app, items=show_files(), command=select, selected=show_files()[0], scrollbar=True)
btn1 = PushButton(app, text="play", command=play)
btn2 = PushButton(app, text="stop", command=stop)

tag = Text(app, text="음원 정보")
picture = Picture(app, width=200, height=200)
lyrics = TextBox(window, text="가사", width="fill", height="fill", multiline=True, scrollbar=True)
slider = Slider(app, command=volume)
slider.value = 50

app.display()
