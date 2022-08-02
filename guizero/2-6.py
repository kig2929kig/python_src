from guizero import App, Text, Box, PushButton, TextBox
app = App()

top = Box(app, align="top", width="fill")
#top.bg = "blue"
bottom = Box(app, width="fill", height="fill")
cross = Box(top, align="left")

flag = Box(cross)
flag.bg="white"

first = Text(flag, bg="red", align="top", height=1, width=3)
second = Text(flag, bg="yellow", align="left", height=1, width=3)
third = Text(flag, bg="light blue", align="left", height=1, width=3)
fourth = Text(flag, bg="red", align="left", height=1, width=3)
#fifth = Text(flag, bg="green", align="bottom", height=1, width=3)

flag_cont = Box(cross, width="fill")
flag_cont.bg = "white"

fifth = Text(flag_cont, bg="green", align="bottom", height=1, width=3)
#fifth2 = Text(flag_cont, bg="red", align="left", height=1, width=3)

fill = Text(top, align="left", height="fill", width="fill", bg="red")
fill_cont = Text(bottom, height="fill", width="fill", bg="red")

app.display()
