# when_clicked
# when_left_button_pressed - 이벤트와 함께 버튼이 클릭될때 순간적으로 변화는 것처럼 보이도록 하기 위해 사용될 수 있다.
# when_left_button_released - 일반적으로 이전 이벤트와 함께 사용
# when_mouse_enters - 마우스 커서가 위젯에 들어갈 때 트리거됨. 또한 사용자가 GUI 를 탐색할 때 시각적 신호를 제공하는데 유용.
# when_mouse_leaves - 마우스가 위젯을 떠날 때 트리거 됨.
# when_mouse_dragged - 마우스를 클릭한 다음 위젯을 가로질러 끌 때.

# widget_name.when_left_button_pressed = function_name

from guizero import App, TextBox, PushButton, Text, info

app = App()

def btn_go_clicked() :
	info("Greetings", "Hello, " + txt_name.value + ", - I hope you're having a nice day")
	
def highlight() :
	txt_name.bg = "light blue"
	
def lowlight() :
	txt_name.bg = None

lbl_name = Text(app, text="Hello, What's your name?")
txt_name = TextBox(app)

txt_name.when_mouse_enters = highlight
txt_name.when_mouse_leaves = lowlight
g
btn_go = PushButton(app, command=btn_go_clicked, text="Done")

app.display()

# 이벤트 라이브러리 : https://lawsie.github.io/guizero/events/
