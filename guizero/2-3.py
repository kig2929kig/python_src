# 푸시버튼, 박스, 리스트박스, 그림, 슬라이더, 와플 위젯은 픽셀 단위로 측정
# size : https://lawsie.github.io/guizero/size/

from guizero import App, PushButton
app = App()

button = PushButton(app, text="Default Size")
button_sized = PushButton(app, text="New Size", width=20, height=10)
button_sized2 = PushButton(app, width="fill", height="fill")

app.display()

#과제
# 프로그램에서 위젯을 하나 또는 두개를 더 추가하고 크기를 변경해보자.
# 화면을 채우기 위해 편집기를 확장하면 크기가 커지는 위젯을 만들어 보자.
