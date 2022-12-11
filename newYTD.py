from tkinter import *
from tkinter import filedialog
import os

window_size_width = 640
window_size_height = 300

def url_entry_clear() :
    url_entry.delete(0, END)

def brower_open_button() :
    path = os.path.realpath("youtube")
    os.startfile(path)
    

root = Tk() # 최상위 레벨의 윈도우(window) 생성

root.title("YouTube Downloader by kig2929kig") # 윈도우 제목 표시줄
root.geometry(str(window_size_width) + "x" + str(window_size_height)) # 너비 x 높이 + x좌표 + y좌표
root.resizable(False, False) # 윈도우 크기 조절 - True(가능), False(불가능)
root.config(background='white')

url_Frame = LabelFrame(root, text="주소(URL)")
url_Frame.pack(padx=5, pady=5, fill="x")

progress_frame = LabelFrame(root, text="진행률")
progress_frame.pack(padx=5, pady=5, fill="both", expand="yes")

url_entry = Entry(url_Frame)
url_entry.pack(padx=2, pady=10, fill="both", expand="yes", side="left")

btn_clear_icon = PhotoImage(file = r"icon\close.png")
btn_clear_icon = btn_clear_icon.subsample(40,40)
btn_url_clear = Button(url_Frame , text="x", image=btn_clear_icon, command=url_entry_clear)
btn_url_clear.pack(padx=2, side="left")

btn_folder_icon = PhotoImage(file = r"icon\folder.png")
btn_folder_icon = btn_folder_icon.subsample(30,35)
btn_url = Button(url_Frame , text="...", image=btn_folder_icon, command=brower_open_button)
btn_url.pack(padx=2, side="left")


root.mainloop() # 윈도우(window) 종료될 때까지 실행

