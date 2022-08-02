from guizero import App, Text

def increase() :
	text.text_size = int(text.text_size) + 1

app = App("textsize")

text = Text(app, text="bigger")
text.repeat(500, increase) # 0.5초 마다 increase 함수 호출

app.display()
