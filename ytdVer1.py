from tkinter import *
from tkinter.ttk import *
from pytube import YouTube
import os

def progress(stream, chunk, bytes_remaining) :
            
    tasks = stream.filesize
    currnet = ((stream.filesize - bytes_remaining) / stream.filesize) * 100
    bar['value'] = round(currnet, 2)
       
    percent_label.set(str(bar['value'])+"%")
    window.update_idletasks()
        
        
def download() :
    # 다운로드 폴더 설정
    #########################################
    save_folder = "./youtube"
    if not os.path.exists(save_folder) :
        os.mkdir(save_folder)
    else :
        pass
    #########################################
    
    url = 'https://www.youtube.com/watch?v=AOkDKC094mQ&list=RDEMsIZ55rx2f_ttXJMoOkJ5Ag&start_radio=1'
    yt = YouTube(url, on_progress_callback=progress)
    #yt.register_on_progress_callback(progress)
    #yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(save_folder) 
    down_clip = yt.streams.get_highest_resolution().download(save_folder)

window = Tk()
percent_label = StringVar()
bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent_label).pack()

button = Button(window, text="download", command=download).pack()

window.mainloop()
