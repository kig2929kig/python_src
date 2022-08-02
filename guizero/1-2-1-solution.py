from guizero import App, Text, TextBox, PushButton, info

app= App(title="Event GUI")

def btn1_go_clicked() :
	if (textUserName.value=="") or (textAnimalName.value=="") :
		return
	
	info("Greetings!", "Hello, " + textUserName.value + ", I hope you're having a nice day with your " + textAnimalName.value + ".")
	textUserName.value = ""
	textAnimalName.value = ""

def btn2_go_clicked() :
	if (textUserName.value=="") or (textAnimalName.value=="") :
		return
	
	info("Greetings!", "So, " + textUserName.value + ", you like " + textAnimalName.value + "s!")
	textUserName.value = ""
	textAnimalName.value = ""

lbl1_name = Text(app, text="Hello. What's your name?")
textUserName = TextBox(app)

lbl2_name = Text(app, text="What is your favorite animal?")
textAnimalName = TextBox(app)

btn1_go = PushButton(app, command=btn1_go_clicked, text="Enter")
btn2_go = PushButton(app, command=btn2_go_clicked, text="Done")

app.display()
