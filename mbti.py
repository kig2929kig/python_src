from tkinter import *
from tkinter import messagebox

t_count = 0
f_count = 0

################################################################## MBTI 유형 ##################################################################
t_category = ["나는 불공평한 것이 가장 나쁘다고 생각한다.", "나는 공부 잘하는 실력 있는 학생으로 인정받고 싶다.",
              "우리 편이 지면 다음 번에는 이기도록 계획을 짠다.", "친구의 잘못된 점은 지적해 주는 편이다.",
              "나는 공평한 사람이 되고 싶다.", "달리기에서 이기면 기분이 아주 좋다.", "나는 똑똑한 사람으로 인정받고 싶다.",
              "도둑질을 하는 학생은 벌을 받아야 한다고 생각한다.", "벌금을 받을 때는 규칙대로 정확하게 받아야 한다." ]

f_category = ["나는 다른 사람의 마음에 상처를 주는 것이 가장 나쁘다고 생각한다.", "나는 친구들 사이에서 인기가 좋은 학생으로 인정받고 싶다.",
              "우리 편이 지면 '다음에 이기면 되지'하면서 친구들의 기분을 좋게 해준다.",
              "친구의 잘못된 점을 지적해 주면 친구가 어떻게 생각할까 걱정이 돼서 말하지 않는 편이다.", "나는 친철한 사람이 되고 싶다.",
              "달리기에서 이기면 기분은 좋지만 진 사람은 기분이 어떨까 생각한다.", "나는 따뜻한 사람으로 인정받고 싶다.",
              "도둑질을 하는 학생은 도둑질을 하지 않도록 도움을 받아야 한다고 생각한다.",
              "벌금을 받을 때는 상황에 따라 그 사람의 사정을 고려해서 받아야 한다."]

j_category = ["내가 해야 할 일을 먼저 하고 논다.", "수업 계획에 따라 차근차근 가르쳐 주시는 선생님이 좋다.",
              "나는 정리정돈 된 깨끗한 방이 좋다.", "하기 쉽게 잘 짜여진 숙제를 나는 좋아한다.",
              "자전거를 탈 때 어디로 갈지 미리 생각하고 탄다.", "나는 일기장이나 과제물을 잘 챙기는 편이다.",
              "무엇을 공부해야 할 지 자세히 가르쳐 주시는 선생님이 좋다.", "게임의 규칙은 절대로 바뀌어서는 안된다.",
              "나는 일을 계획적으로 해내는 편이다."]

p_category = ["내가 할 수 있는 일이라면 먼저 재미있게 놀고 난 후에 해도 괜찮다.",
              "그때그때마다 우리가 좋아하는 것에 맞추어 수업 내용을 바꾸어서 가르치는 선생님이 좋다.",
              "나는 내 마음대로 흩어놓을 수 있는 방이 좋다.", "새로운 방법으로 하는 숙제를 나는 좋아한다.",
              "자전거를 탈 때 그냥 달리고 나서 어디로 갈지 생각한다.", "나는 일기장이나 과제물을 잘 잊어먹는 편이다.",
              "우리들 스스로 공부할 것을 선택하도록 맡기시는 선생님이 좋다.", "게임의 규칙은 경우에 따라 바뀔 수 있다.",
              "나는 일을 그때 그때 해내는 편이다."]
################################################################## MBTI 유형 ##################################################################

def result() :
    global t_count, f_count, lbl_var

    t_count = 0
    f_count = 0
    msg = "nothing selected"
    if rd_btn1_var.get() == 1:
        t_count = t_count + 1
    if rd_btn1_var.get() == 2:
        f_count = f_count + 1
    if rd_btn2_var.get() == 1:
        t_count = t_count + 1
    if rd_btn2_var.get() == 2:
        f_count = f_count + 1
    if rd_btn3_var.get() == 1:
        t_count = t_count + 1
    if rd_btn3_var.get() == 2:
        f_count = f_count + 1
        
    if t_count > f_count :
        lbl_var.set("Result : I")
    else :
        lbl_var.set("Result : F")
    #messagebox.showinfo("info", msg)
    
window = Tk()
window.title("MBTI TEST by kig2929kig")
window.geometry("600x600")
window.resizable(False,False)


ttl_lbl = Label(window, text="나의 성격 유형과 관련 직업", font=("Arial", 14, "bold"))
ttl_lbl.pack(pady=10)

frm1 = Frame(window, relief="ridge", bd=1, height=500)
frm1.pack(padx=5, pady=5, fill="both")

lblfrm1 = LabelFrame(frm1, text="1번")
lblfrm1.pack(pady=5, fill="x")

rd_btn1_var = IntVar()
rd_btn2_var = IntVar()
rd_btn3_var = IntVar()
rd_btn1 = Radiobutton(lblfrm1, text=t_category[0], variable=rd_btn1_var, value=1)
rd_btn1.pack(anchor="w")
rd_btn2 = Radiobutton(lblfrm1, text=f_category[0], variable=rd_btn1_var, value=2)
rd_btn2.pack(anchor="w")

lblfrm2 = LabelFrame(frm1, text="2번")
lblfrm2.pack(pady=5, fill="x")
rd_btn3 = Radiobutton(lblfrm2, text=t_category[1], variable=rd_btn2_var, value=1)
rd_btn3.pack(anchor="w")
rd_btn4 = Radiobutton(lblfrm2, text=f_category[1], variable=rd_btn2_var, value=2)
rd_btn4.pack(anchor="w")

lblfrm3 = LabelFrame(frm1, text="3번")
lblfrm3.pack(pady=5, fill="x")
rd_btn5 = Radiobutton(lblfrm3, text=t_category[2], variable=rd_btn3_var, value=1)
rd_btn5.pack(anchor="w")
rd_btn6 = Radiobutton(lblfrm3, text=f_category[2], variable=rd_btn3_var, value=2)
rd_btn6.pack(anchor="w")

btn = Button(window, text="확인", command=result)
btn.pack()

lbl_var = StringVar()
lbl_var.set("Result : ")
lbl = Label(window, textvariable = lbl_var, font=("Arial", 14, "bold"))
lbl.pack()

window.mainloop()
