
from guizero import App, TextBox, PushButton, Box, Combo, CheckBox, Slider, MenuBar

def open_file() :
	with open(file_name.value, "r") as f:
		editor.value = f.read()
		
def save_file() :
	with open(file_name.value, "w") as f:
		f.write(editor.value)
		save_button.disable()

def enable_save() :
	save_button.enable()

def exit_app():
	app.destroy()
	

app = App(title="textzero")

menubar = MenuBar(app, toplevel=["File"], options=[[["open", open_file], ["save", save_file], ["exit", exit_app]]])

file_controls = Box(app, align="top", width="fill", border=True)
file_name = TextBox(file_controls, text="text_file.txt", width=50, align="left")

save_button = PushButton(file_controls, text="Save", command=save_file, align="right")
open_button = PushButton(file_controls, text="Open", command=open_file, align="right")

editor = TextBox(app, multiline=True, height="fill", width="fill", command=enable_save)

app.display()

# 과제
# 편집기의 다른 기능을 추가하고 메뉴를 만들어 .보세요.
