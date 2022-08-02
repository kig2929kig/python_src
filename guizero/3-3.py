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
#from guizero import App, Box, Text, TextBox
#app = App()

#box_fname = Box(app, width="fill")
#lbl_fname = Text(box_fname, text="First name", align="left", width=10)
#txt_fname = TextBox(box_fname, align="left")

#box_sname = Box(app, width="fill")
#lbl_sname = Text(box_sname, text="Surname", align="left", width=10)
#txt_sname = TextBox(box_sname, align="left")

#box_dob = Box(app, width="fill")
#lbl_dob = Text(box_dob, text="Date of birth", align="left", width=10)
#txt_dob = TextBox(box_dob, align="left")

#app.display()

# 그리드 레이아웃 사용
from guizero import App, Text, TextBox
app = App(layout="grid")

lbl_fname = Text(app, text="First name", grid=[0,0])
txt_fname = TextBox(app, grid=[1,0])

lbl_sname = Text(app, text="Surname", grid=[0,1])
txt_sname = TextBox(app, grid=[1,1])

lbl_dob = Text(app, text="Date of birth", grid=[0,2])
txt_dob = TextBox(app, grid=[1,2])

app.display()

# 그리드 레이아웃은 별도의 박스에 배치할 필요가 없다.
# 그래서 코드의 양이 작다.
# 그리드 레이아웃은 각 위젯이 깔끔하게 정렬되지만 box를 이용한 레이아웃은 글자의 크기 등에 영향을 받는다.
# 그리드 레이아웃은 장점은 많지만 항상 적절한 것은 아닌다. 코드를 완성하고 수정이 생기면 그리드 레이아웃 전체를
# 수정해야한다.

