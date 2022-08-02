# https://lawsie.github.io/guizero/app/

from guizero import App, Text, ButtonGroup, Combo, PushButton, TextBox, Box
app = App(title="Hero-o-matic", width=300, bg="red")

message1 = Text(app, text="Choose an adjective")
bgp_adjective = ButtonGroup(app, options=["Amazing", "Bonny", "Charming", "Delightful"], selected="Amazing")

message2 = Text(app, text="Choose a colour")
message2.text_color = "blue"
txt_colour = TextBox(app)

message3 =  Text(app, text="Pick an animal")
cmb_animal = Combo(app, options=["Aardvark", "Badger", "Cat", "Dolphin", "Velociraptor"], selected="Aardvark", width=20)

box = Box(app)


btn_make_name = PushButton(box, text="Make me a hero")
lbl_output = Text(box, text="Your hero name will appear here")
lbl_output.font = "Times New Roman"

box.bg="white"
box.text_size = 12

app.display()

# 과제
# 위 프로그램의 요소들을 어떻게 그룹화하겠습니까? 각 그룹을 별도의 상자에 넣어 보세요.
# 원하는 색상표를 사용하여 앱을 다시 디자인하세요.
# 힌트 : https://lawsie.github.io/guizero/colors/
