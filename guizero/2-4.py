from guizero import App, Text
app = App(title="align")

top_text = Text(app, text="at the top", align="top")
bottom_text = Text(app, text="at the bottom", align="bottom")
left_text = Text(app, text="to the left", align="left")
left_text1 = Text(app, text="to the left again", align="left")
right_text = Text(app, text="to the right", align="right")

app.display()
