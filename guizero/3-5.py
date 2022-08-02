
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
from random import shuffle
from guizero import App, Picture, Box

emojis_dir = "./emojis"

emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]
# https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
shuffle(emojis)

app = App("emoji match")
game_box = Box(app)

pictures_box = Box(game_box, layout="grid")
pictures = []

for x in range(0,3) :
	for y in range(0,3) :
		picture = Picture(pictures_box, grid=[x,y])
		pictures.append(picture)

for picture in pictures:
	picture.image = emojis.pop()
	
	# pop으로 꺼내면 리스트에서 이미지가 제거되어 한번 나온 이미지가 다시 나오지 않는 효과가 있다.
	
app.display()
