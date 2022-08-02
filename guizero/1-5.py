
# 그동안 배운 위젯 등을 사용하여 아래 내용을 추가해보자.
# app 창의 width, height 각각 1000픽셀로 변경
# ListBox 위젯을 추가하여 hero 이름에 추가
# CheckBox 위젯을 추가하여 체크박스를 체크하며 app 배경색을 light blue, 아니면 None 기능을 추가
# Slider 위젯을 추가하여 message1.size 크기를 변경해보자.
# Picture 위젯을 이용하며 app에 추가해보자.
#Picture(gif, png) resize
#sudo pip3 install --upgrade Pillow

from guizero import App, Text, ButtonGroup, Combo, PushButton, TextBox, ListBox, CheckBox, Slider, Picture
app = App(title="Hero-o-matic", width=1000, height=1000) # xxxx-o-matic : 이름을 지을 때 다른 단어와 합성하는 데 쓰이는 접미

def make_hero_name() :
	adjective = bgp_adjective.value
	colour = txt_colour.value
	lb = lstbox.value
	animal = cmb_animal.value
	hero = adjective + " " + colour + " " + lb + animal
	lbl_output.value = "You are ... The " + hero + "."

def highlight() :
	if (chckb.value == 1) :
		app.bg = "light blue"
	else :
		app.bg = None

def change_text_size(slider_value) :
	message1.size = slider_value
	
message1 = Text(app, text="Choose an adjective")
bgp_adjective = ButtonGroup(app, options=["Amazing", "Bonny", "Charming", "Delightful"], selected="Amazing")

message2 = Text(app, text="Enter a colour?")
txt_colour = TextBox(app)

message3 = Text(app, text="Pick an animal")
cmb_animal = Combo(app, options = ["Aardvark", "Cat", "Dolphin", "Tiger", "Velociraptor", "Walrus"], selected="Aardvark", width=20)

lstbox = ListBox(app, items=["powerfull", "boring", "Thin"], selected="powerfull")
chckb = CheckBox(app, command=highlight, text="light blue")
text_size = Slider(app, command=change_text_size, start=10, end=80)

btn_make_name = PushButton(app, command=make_hero_name, text="Make me a hero")
lbl_output = Text(app, text="A hero name will appear here")
my_son = Picture(app, image="/home/pi/Pictures/son.png", width=200, height=200)

app.display()
