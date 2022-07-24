import pygame as pg

pg.init()

def load(img, width, height):
	image = pg.image.load(img)
	image = pg.transform.scale(image, (width, height))
	return image

width = 800
height = 1280

screen = pg.display.set_mode((width, height))
	
#Loading Sounds... 
soundtrack = pg.mixer.Sound("../Sounds/soundtrack.mp3")
win_sound = pg.mixer.Sound("../Sounds/aplausos.mp3")
game_over_sound = pg.mixer.Sound("../Sounds/game_over.mp3")

failsound = pg.mixer.Sound("../Sounds/fail.mp3")
eatsound = pg.mixer.Sound("../Sounds/eating.mp3")
	
#Loading Main Images
bg = load("../Main Images/bg.png", width, height) 	
agradecimentos = load("../Main Images/agradecimento.png", 800,1280)
Kidney_image = load("../Main Images/rim.png",250,250)
win = load("../Main Images/win.png", 700,700)
game_over_image = load("../Main Images/game_over.png", 800,1280)
loading = load("../Main Images/loading.png", 800,1280)
start_image = load("../Main Images/start.png", 250,100)
	

#Loading Task 1 Images
task1_image = load("../Task 1-Images/task1.png", 800,800)
items1 = load("../Task 1-Images/items1.png", 600,600) 
task1_wrong_images = [
load("../Task 1-Images/pelve.png",150,150), 
load("../Task 1-Images/cálice.png",150,150), 
load("../Task 1-Images/piramide.png", 150,150)]

task1_right_images = [
load("../Task 1-Images/cortex.png", 150,150)]

#Loading Task 2 Images
task2_image = load("../Task 2-Images/task2.png", 800,800)
items2 = load("../Task 2-Images/items2.png", 600,600)

task2_wrong_images = [load("../Task 2-Images/contração.png",200,50), 
load("../Task 2-Images/transformação.png",200,50), load("../Task 2-Images/destruição.png", 200,50), load("../Task 2-Images/substituição.png", 200,50)]

task2_right_images = [
load("../Task 2-Images/reabsorção.png", 250,100), load("../Task 2-Images/absorção.png", 150,50),
load("../Task 2-Images/secreção.png", 150,50)]

#Loading Task 3 Images
task3_image = load("../Task 3-Images/task3.png", 800,800)
items3 = load("../Task 3-Images/items3.png", 600,600)

task3_wrong_images = [
load("../Task 3-Images/alcool.png",200,200), 
load("../Task 3-Images/urico.png",200,200),
load("../Task 3-Images/oxigenio.png", 200,200)]

task3_right_images = [
load("../Task 3-Images/h2o.png",200,200), 
load("../Task 3-Images/proteinas.png",200,200),
load("../Task 3-Images/sodio.png", 200,200)]

#arrays

task1 = {'task':task1_image, 'button':[start_image.get_rect(), start_image], 'wrong':[], 'right':[], 'items':items1}

task2 = {'task':task2_image, 'button':[start_image.get_rect(),start_image], 'items':items2, 'wrong':[], 'right':[]} 

task3 = {'task':task3_image, 'button':[start_image.get_rect(),start_image], 'items':items3, 'wrong':[], 'right':[]} 

#add images to dict

for img in task1_wrong_images:
	task1['wrong'].append(img)
	
for img in task1_right_images:
	task1['right'].append(img)	
	
for img in task2_wrong_images:
	task2['wrong'].append(img)
	
for img in task2_right_images:
	task2['right'].append(img)
	
for img in task3_wrong_images:
	task3['wrong'].append(img)
		
for img in task3_right_images:
	task3['right'].append(img)

#add button position
task1['button'][0].left = 280
task2['button'][0].left = 280
task3['button'][0].left = 280

task1['button'][0].top = 950
task2['button'][0].top = 950
task3['button'][0].top = 950


#creating touch invisible rects
white = (255,255,255,135)	

left = pg.Surface((400,600), pg.SRCALPHA)
TouchRect_left = left.get_rect()

right = pg.Surface((400,600), pg.SRCALPHA)
TouchRect_right = right.get_rect()

pg.draw.rect(left, white, TouchRect_left,0)
pg.draw.rect(right, white, TouchRect_right,0)

TouchRect_right.left = 0
TouchRect_right.top = 700

TouchRect_left.left = 400
TouchRect_left.top = 700
