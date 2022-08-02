# https://lawsie.github.io/guizero
# sudo pip3 install guizero
# Text - https://lawsie.github.io/guizero/text/#properties

from guizero import App, Text

app = App(title="This is my first GUI")

message = Text(app, text="GUIs are cool.")

app.display()
