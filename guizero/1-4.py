from guizero import App, Text, ButtonGroup, Combo, PushButton, TextBox
app = App(title="Hero-o-matic") # xxxx-o-matic : 이름을 지을 때 다른 단어와 합성하는 데 쓰이는 접미

def make_hero_name() :
	adjective = bgp_adjective.value
	colour = txt_colour.value
	animal = cmb_animal.value
	hero = adjective + " " + colour + " " + animal
	lbl_output.value = "You are ... The " + hero + "."

message1 = Text(app, text="Choose an adjective")
bgp_adjective = ButtonGroup(app, options=["Amazing", "Bonny", "Charming", "Delightful"], selected="Amazing")

message2 = Text(app, text="Enter a colour?")
txt_colour = TextBox(app)

message3 = Text(app, text="Pick an animal")
cmb_animal = Combo(app, options = ["Aardvark", "Cat", "Dolphin", "Tiger", "Velociraptor", "Walrus"], selected="Aardvark", width=20)

btn_make_name = PushButton(app, command=make_hero_name, text="Make me a hero")
lbl_output = Text(app, text="A hero name will appear here")

app.display()

# 프로그램에 형용사와 동물을 추가해라.
# 코드에서 한 유형의 위젯을 다른 유형의 위젯으로 교체하여 프로그램을 변경
