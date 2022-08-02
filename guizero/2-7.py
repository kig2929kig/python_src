# https://docs.python.org/3/library/functions.html#open

from guizero import App, TextBox, PushButton, Box, Combo, Text, Slider
app = App(title="texteditor")

def open_file() :
	with open(file_name.value, "r") as f:
		editor.value = f.read()

def save_file() :
	with open(file_name.value, "w") as f:
		f.write(editor.value)
	save_button.disable()

def change_font() :
	editor.font = font.value
	

def change_text_size() :
	editor.text_size= size.value
	editor.resize(1,1)
	editor.resize("fill", "fill")
	
def enable_save() :
	save_button.enable()

file_controls = Box(app, align="top", width="fill")
file_name = TextBox(file_controls, text="text_file.txt", width=30, align="left")
exit_box = Box(app, align="bottom", width="fill")
preferences_controls = Box(app, align="bottom", width="fill", border=True)
font = Combo(preferences_controls, options=["courier", "times new roman", "verdana"], align="left", command=change_font)

save_button = PushButton(file_controls, command=save_file, text="Save", align="right")
open_button = PushButton(file_controls, command=open_file, text="Open", align="right")

size = Slider(preferences_controls, align="left", command=change_text_size, start=10, end=42)

editor = TextBox(app, multiline=True, height="fill", width="fill", command=enable_save)
#editor.text_size = 20

exit_btn = PushButton(exit_box, command=exit, text="Exit", align="right")

app.display()

# 도전
# 폰트의 색을 변경하는 Combo 위젯을 만들어 보세요.
