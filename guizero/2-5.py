from guizero import App, Box, PushButton
app = App()

box = Box(app, width="fill", border=2)
button = PushButton(box, align="left")

app.display()
