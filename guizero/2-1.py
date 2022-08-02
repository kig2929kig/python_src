
# Box : 다른 위젯의 컨테이너 역할을 하는 위젯, 기본적으로 보이지 않으며 다른 위젯을 보다 쉽게 배치하고 디자인을 변경하는 데 사용
from guizero import App, Box, PushButton
app = App()

box = Box(app, align="left", width="500", border=2) # align 값을 top, right 등 변경, width 값을 500 등으로 변경 매개변수의 의미를 파악
button = PushButton(box)
button1 = PushButton(box, text="another button")

app.display()

# 크기가 다른 3박스가 포함된 앱을 만드세요.
# 상자의 다양한 매개 변수를 변경하세요.
# 세 개의 위젯을 더 작성하고 각각의 위젯을 다른 상자 안에 넣으세요.
# 프로그램 소스코드를 실행하기 전에 앱이 어떻게 보일지 추측해보세요.
