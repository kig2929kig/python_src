from tkinter import *
from tkinter import messagebox

def result() :
    global lbl_var
        
    lbl_var.set(E_I_var.get() + S_N_var.get() + T_F_var.get() + J_P_var.get()) 
    
    
################################################################## MBTI 유형 ##################################################################
E_category = ["나는 여러 친구들과 많이 사귀는 편이다."]
I_category = ["나는 몇 명의 친구들과 깊이 사귀는 편이다."]
S_category = ["나는 친구들에게 내가 직접 보고 들은 것에 대해 얘기하는 것을 좋아한다."]
N_category = ["난 친구들에게 내가 상상한 것을 이야기하는 것을 좋아한다."]
T_category = ["나는 불공평한 것이 가장 나쁘다고 생각한다."]
F_category = ["나는 다른 사람의 마음에 상처를 주는 것이 가장 나쁘다고 생각한다."]
J_category = ["내가 해야 할 일을 먼저 하고 논다."]
P_category = ["내가 할 수 있는 일이라면 먼저 재미있게 놀고 난 후에 해도 괜찮다."]
################################################################## MBTI 유형 ##################################################################

window = Tk()
window.title("MBTI TEST by kig2929kig")
window.geometry("600x600")
window.resizable(False,False)


################################################ 제목 #####################################################
ttl = Label(window, text="나의 성격 유형과 관련 직업", font=("Arial", 14, "bold"))
ttl.pack(pady=10)
################################################ 제목 #####################################################

############################################ MBTI 프레임  #################################################
mbti_frm = Frame(window, relief="ridge", bd=1)
mbti_frm.pack(padx=5, pady=5, fill="both")
############################################ MBTI 프레임  #################################################

### 변수 ###
E_I_var = StringVar()
S_N_var = StringVar()
T_F_var = StringVar()
J_P_var = StringVar()
### 변수 ###

############################## MBTI 프레임  - 나의 에너지 방향은 - ########################################
E_I_frm = LabelFrame(mbti_frm, text="나의 에너지 방향은?")
E_I_frm.pack(padx=5, pady=5, fill="x")

rd_btn_E = Radiobutton(E_I_frm, text=E_category[0], variable=E_I_var, value="E")
rd_btn_E.pack(anchor="w")
rd_btn_I = Radiobutton(E_I_frm, text=I_category[0], variable=E_I_var, value="I")
rd_btn_I.pack(anchor="w")
############################## MBTI 프레임  - 나의 인식 기능은 - ##########################################
S_N_frm = LabelFrame(mbti_frm, text="나의 인식 기능은?")
S_N_frm.pack(padx=5, pady=5, fill="x")

rd_btn_S = Radiobutton(S_N_frm, text=S_category[0], variable=S_N_var, value="S")
rd_btn_S.pack(anchor="w")
rd_btn_N = Radiobutton(S_N_frm, text=N_category[0], variable=S_N_var, value="N")
rd_btn_N.pack(anchor="w")
############################## MBTI 프레임  - 나의 판단 기능은 - ##########################################
T_F_frm = LabelFrame(mbti_frm, text="나의 판단 기능은?")
T_F_frm.pack(padx=5, pady=5, fill="x")

rd_btn_T = Radiobutton(T_F_frm, text=T_category[0], variable=T_F_var, value="T")
rd_btn_T.pack(anchor="w")
rd_btn_F = Radiobutton(T_F_frm, text=F_category[0], variable=T_F_var, value="F")
rd_btn_F.pack(anchor="w")
############################## MBTI 프레임  - 나의 생활 양식은 - ##########################################
J_P_frm = LabelFrame(mbti_frm, text="나의 생활 양식은?")
J_P_frm.pack(padx=5, pady=5, fill="x")

rd_btn_J = Radiobutton(J_P_frm, text=J_category[0], variable=J_P_var, value="J")
rd_btn_J.pack(anchor="w")
rd_btn_P = Radiobutton(J_P_frm, text=P_category[0], variable=J_P_var, value="P")
rd_btn_P.pack(anchor="w")

############################## 확인 버튼 ##########################################
btn = Button(window, text="확인", font=("Arial", 12), command=result)
btn.pack()

############################## 결과 Label ##########################################
lbl_var = StringVar()
lbl_var.set("당신의 MBTI : ")
lbl = Label(window, textvariable = lbl_var, font=("Arial", 14, "bold"))
lbl.pack(padx=5, pady=5)
    
window.mainloop()

