import tkinter
import threading, random

flag = 1

def start_t():
	thread1 = threading.Thread(target=start)
	thread1.daemon = True
	thread1.start()

def start() :
	global flag
	while flag==1 :
		rnd = random.randrange(1,6)
		img.config(file = "/home/kig2929kig/Desktop/img/" + str(rnd) + ".png")
	
def select() :
	global flag
	print("종료")
	flag=0

window = tkinter.Tk()
window.title("당신의 미래 아내는?")
window.geometry("400x400")
window.resizable(False, False)

img = tkinter.PhotoImage()
canvas = tkinter.Canvas()
canvas.create_image(200, 200, image=img)
canvas.pack()

btn1 = tkinter.Button(window, text = "START", command=start_t)
btn1.pack()
btn2 = tkinter.Button(window, text = "SELECT", command=select)
btn2.pack()

window.mainloop()

