# 위젯 : 앱의 인터페이스를 구축하는 데 사용할 수 있는 다양한 구성 요소
# Text, ButtonGroup, TextBox, Slider, Check, Combo, PushButton
# 위젯 라이브러리 : https://lawsie.github.io/guizero/widgetoverview/

from guizero import App, TextBox, PushButton, Text, info

app = App()

def btn_go_clicked() :
	info("Greetings", "Hello, " + txt_name.value + " - I hope you're having a nice day")
	

lbl_name = Text(app, text="Hello, What's your name?")
txt_name = TextBox(app)
btn_go = PushButton(app, command=btn_go_clicked, text="Done")

app.display()

# 코드를 보고 무엇을 할 것인지 예측해 보자.
# 코드는 세 가지 위젯을 작성
# Text - lbl_name (라벨)
# TextBox - txt_name (이름을 입력)
# PushButton - 클릭할 수 있는 '완료' 버튼(이벤트 발생)

# def btn_go_clicked() : PushButton을 클릭했을 때 수행할 작업을 설명하는 함수 정의
# info - info 상자를 표시(첫번째 매개 변수 (Greetings)는 상자의 제목
#      - 두번째 매개 변수는 상자 자체 내부에 나타나는 텍스트
# btn_go = PushButton() : PushButton이 생성되며 클릭하면 btn_go_clicked 함수의 기능이 작동
# 프로그램이 실행되면 이벤트가 트리거될 때까지 기다린다. 

#과제
# 사용자에게 다른 정보(예: 동물이름)를 요청하려면 두 개의 Text 및 TextBox 위젯을 추가
# 푸시 버튼을 클릭하면 Info 팝업 상자에 새로운 정보가 표시되어 한다.
# 예) 너의 이름은 Ingoo 이고 너는 cat을 좋아한다.
# 두 번째 푸시버튼을 추가, 이 버튼을 클릭하면 다른 메시지가 표시되어야 한다.
# 사용자에게 암호를 두 번 입력하도록 요청한 다음 두 번 모두 동일하게 입력했는지 여부를 알려주는 새 앱을 만들자.
