from guizero import App, Text, TextBox, PushButton, info

app = App(title="Password Check GUI")

def btn_go_clicked() :
	if(textPassword1.value == "") or (textPassword2.value == "") :
		if (textPassword1.value == "") and (textPassword2.value == "") :
			info("Error!", "Both password values omitted!")
			return
		if (textPassword1.value == "") :
			info("Error!", "Password value 1 omitted!")
			return
		info("Error!", "Password value 2 omitted!")
		return
	if (textPassword1.value != textPassword2.value) :
		info("Error!", "Password values not equal!")
		return
	info("Excellent!", "The password values are equal!")
	
	textPassword1.value = ""
	textPassword2.value = ""
	return
	
lbl1_pwd1 = Text(app, text="Enter the password")
textPassword1 = TextBox(app)
textPassword1.hide_text = True

lbl2_pwd2 = Text(app, text="Reenter the password")
textPassword2 = TextBox(app)
textPassword2.hide_text = True

btn_go = PushButton(app, command=btn_go_clicked, text="Verify")

app.display()

