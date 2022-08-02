from guizero import App, Text

app = App(title="Hi there")

firstmessage = Text(app, text="This is big text", color="red")
secondmessage = Text(app, text="This is green", size=40)
thirdmessage = Text(app, text="Ansan Technical High School", font="Quicksand")

firstmessage.text_size = 40
secondmessage.bg = "green"


app.display()

