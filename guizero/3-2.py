
# 복잡한 문제(프로그램)를 작은 단위(작은 프로그램)로 분해
# 전체 프로그램을 각 단계별로 구분하고 구분된 프로그램들을 조합해서 하나의 프로그램을 완성하는 것이 효과적
# 그리드 레이아웃
#                x
#           0      1      2       3       4
#   0     (0,0)  (1,0)  (2,0)   (3,0)   (4,0)
#   1     (0,1)  (1,1)  (2,1)   (3,1)   (4,1)
#   2     (0,2)  (1,2)  (2,2)   (3,2)   (4,2)
#   3     (0,3)  (1,3)  (2,3)   (3,3)   (4,3)
#
#
from guizero import App, PushButton
app = App(layout="grid")

button1 = PushButton(app, text="1", grid=[0,0])
button2 = PushButton(app, text="2", grid=[1,0])
button3 = PushButton(app, text="3", grid=[2,0])
button4 = PushButton(app, text="4", grid=[0,1])
button5 = PushButton(app, text="5", grid=[1,1])
button6 = PushButton(app, text="6", grid=[2,1])
button7 = PushButton(app, text="7", grid=[0,2])
button8 = PushButton(app, text="8", grid=[1,2])
button9 = PushButton(app, text="9", grid=[2,2])
button0 = PushButton(app, text="0", grid=[1,3])

app.display()
