from tkinter import *


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
    pass

window = Tk()
window.title("MBTI TEST by kig2929kig")
window.geometry("600x600")
window.resizable(False,False)

scrollbar = Scrollbar(window, orient="vertical")
scrollbar.pack(side="right", fill="y")


ttl_lbl = Label(window, text="나의 성격 유형과 관련 직업", font=("Arial", 14, "bold"))
ttl_lbl.pack(pady=10)

frm1 = Frame(window, relief="ridge", bd=1, yscrollcommand=scrollbar.set)
frm1.pack()
scrollbar.config(command = frm1.yview)   

t_or_f_lblFrm = [] # t, f 유형의 질문이 들어갈 라벨프레임
t_q = [] # t 유형의 질문
f_q = [] # f 유형의 질문

for i in range(5) :
    v = 1
    t_or_f_lblFrm.append(LabelFrame(frm1, text= str(i) +"번"))
    t_or_f_lblFrm[i].pack(fill="x")                   

    t_q.append(Radiobutton(t_or_f_lblFrm[i], text=t_category[i], value="i", command=result))
    t_q[i].pack(anchor="w")
    f_q.append(Radiobutton(t_or_f_lblFrm[i], text=f_category[i], value="f", command=result))
    f_q[i].pack(anchor="w")

 

window.mainloop()
