 
from guizero import App, PushButton
app = App()

on = PushButton(app, text="on", enabled = True)
off = PushButton(app, text="off", enabled = False)

app.display()

#위젯을 보이지 않게 .hide()
#위젯을 볼 수 있게 .show()
