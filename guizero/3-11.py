# _*_ Encoding:UTF-8 _*_ #

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
# 이모지 다운로드
# https://rpf.io/fl-guis-emojis


import os
from random import shuffle, randint
from guizero import App, Picture, Box, PushButton, Text, warn

emojis_dir = "./emojis"

emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]
# https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
shuffle(emojis)


def counter() :
	timer.value = int(timer.value) - 1
	if int(timer.value) == 0 :
		timer.cancel(counter)
		result.value = "Game Over"
		warn("Time Out", "you've run out of time")
		timer.value = 30
		result.value=""
		setup_round()
		score.value = "0"
		timer.repeat(1000, counter)


def match_emoji(matched) :
	if matched:
		result.value = "correct"
		score.value = int(score.value) + 1
	else :
		result.value = "incorrect"
	setup_round()	

def setup_round() :
			
	for picture in pictures:
		picture.image = emojis.pop()
		
		# pop으로 꺼내면 리스트에서 이미지가 제거되어 한번 나온 이미지가 다시 나오지 않는 효과가 있다.

	for button in buttons:
		button.image = emojis.pop()
		button.update_command(match_emoji, [False])

	matched_emoji = emojis.pop()
	random_picture = randint(0,8)
	pictures[random_picture].image = matched_emoji

	random_button = randint(0,8)
	buttons[random_button].image = matched_emoji
	buttons[random_button].update_command(match_emoji, [True])
	
	

app = App("emoji match", height = 600)
result = Text(app)
game_box = Box(app)
pictures_box = Box(game_box, layout="grid")
pictures = []

buttons_box = Box(game_box, layout="grid")
buttons = []

for x in range(0,3) :
	for y in range(0,3) :
		picture = Picture(pictures_box, grid=[x,y])
		pictures.append(picture)
		
		button = PushButton(buttons_box, grid=[x,y])
		buttons.append(button)

extra_features = Box(app)
timer = Text(extra_features, text="Get Ready")
scoreboard = Box(app)
label = Text(scoreboard, text="Score", align="left")
score = Text(scoreboard, text="0", align="left")

setup_round()
timer.value = 30
timer.repeat(1000, counter)

app.display()

# 과제
# 플레이어가 잘못된 일치를 선택할 때마다 한 점을 빼십시오.
# 플레이어가 세 개의 정확한 추측을 할 때마다 보너스 포인트를 추가하라.
# 선수에게 보너스를 알려주는 경보도 추가할 수 있는가?
# 가산점으로 선수들에게 보상을 하는 대신, 추가 시간으로 보상하는 것으로 경기를 바꿀 수 있는가?
# 마지막 점수를 보여줄 수 있는가?




