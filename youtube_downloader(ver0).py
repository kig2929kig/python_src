from guizero import App, Box, Text, TextBox, PushButton, Picture
from pytube import YouTube
from PIL import Image
import requests, os

def youtube_download() :
    global video_title_label, thumbnail_pic

    save_folder = "./youtube"
    if not os.path.exists(save_folder) :
        os.mkdir(save_folder)
    else :
        pass
    
    try :
        video_title_label.value =""
        url = url_txtbox.value
        yt = YouTube(url)
        video_title_label.value = video_title_label.value + str(yt.title[0:50] + "...")
        #thumbnail_pic.image = yt.thumbnail_url.split("?")
        img_url = yt.thumbnail_url
        img_url = img_url.split("?")

        img = Image.open(requests.get(img_url[0], stream=True).raw)
        thumbnail_pic.value = img
    
        down_clip = yt.streams.get_highest_resolution().download(save_folder)
        app.info("다운로드 완료" , "파일이 저장되었습니다.")
    except :
        app.info("다운로드 실패" , "파일이 저장되지 않았습니다.")

    #print(yt.title)
    #print(img_url)
    

app = App(title="유튜브 Downloader by kig2929kig", width=620, height=300)
app.tk.resizable(False, False) # 윈도우의 크기 변경을 금지

url_label1 = Text(app, text="주소(URL)")
url_txtbox = TextBox(app, width=60)
btn_down = PushButton(app, text="다운로드", command=youtube_download)
thumbnail_pic = Picture(app, height=180, width=180)

video_title_label = Text(app, text="제목 : ")
video_thumbnail_label = Text(app, text="썸네일 : ")


url_label1.tk.place(x=10, y=14)
url_txtbox.tk.place(x=95, y=18)
btn_down.tk.place(x=530, y=8)
video_title_label.tk.place(x=10, y=55)
video_thumbnail_label.tk.place(x=10, y=75)
thumbnail_pic.tk.place(x=10, y=100)
app.display()
