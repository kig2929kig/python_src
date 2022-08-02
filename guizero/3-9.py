from guizero import App, Text, PushButton
from time import sleep

#t = 10

def countdown(t) :
	while t > 0:
		text.value = int(text.value) - 1
		print(t)
		#t = int (text.value)
		sleep(1)

app = App()

text = Text(app, text=10)
countdown(10)

#button = PushButton(app, command=countdown(t), text="countdown")

app.display()

# text 값을 업데이트하지 못한다.
