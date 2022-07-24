#trabalho de Biologia - funcionalidades do sistema excretor.
#Kidney Wish.

__authors__ = "equipe 8"

import pygame as pg
from kidneywish_lib import *
from random import choice 
from time import sleep
from database import *


def Play(i1, i2, i3, sound1, sound2,sound3, Kidney,group, screen):
	pg.init()
	clock = pg.time.Clock()
	cont = 0
	font = pg.font.SysFont("Arial", 40)
	
	while True:
		
		hitsoundeffect = sound2
		failsoundeffect = sound3
		
		clock.tick(60)
		cont += 1		

		for ev in pg.event.get():
			if ev.type == quit:
				pg.quit()
				
			elif ev.type == pg.MOUSEBUTTONDOWN:
				
				if TouchRect_right. collidepoint(ev.pos):
					
					Kidney.right = True
					
				if TouchRect_left.collidepoint(ev.pos):
					Kidney.left = True
					
			elif ev.type == pg.MOUSEBUTTONUP:
				Kidney.left = False
				Kidney.right = False
				
		if cont == 1 or cont % 1300 == 0:
			sound1.set_volume(0.9)
			sound1.play()
			
		hits_text = font.render(f"Seus Acertos:{Kidney.hit}", 1,(0,0,0))
		errors_text = font.render(f"Seus Erros:{Kidney.error}", 1,(0,0,0))
		
		screen.blit(bg,(0,0))
		screen.blit(hits_text, (0,10))
		screen.blit(errors_text,(0,70))
		group.draw(screen)
		
		i1.update(cont, Kidney, hitsoundeffect, failsoundeffect)
		i2.update(cont,Kidney, hitsoundeffect, failsoundeffect)
		i3.update(cont,Kidney, hitsoundeffect, failsoundeffect)
		
		Kidney.update()
		pg.display.update()
		
		if Kidney.error >= 5:
			d = "Perdeu"
			break
			
		elif Kidney.hit >= 10:
			d = "Ganhou"
			break
			
	pg.mixer.Sound.stop(sound1)
	return d
		
def Init(task_array):
	pg.init()
	
	screen = pg.display.set_mode((width, height))
	
	#Object
	
	Kidney = MyKidney() 
	
	#Groups
	group = pg.sprite.Group()
	group.add(Kidney)
	
	Items1 = BuildItem(20,task_array['wrong'],screen, group, task_array['right'])
		
	Items2 = BuildItem(400,task_array['wrong'],screen, group, task_array['right'])
		
	Items3 = BuildItem(650,task_array['wrong'],screen, group, task_array['right'])
	cont = 0
	while True:
		cont += 1
		for ev in pg.event.get():
			if ev.type == quit:
				pg.quit()
				
			elif ev.type == pg.MOUSEBUTTONDOWN:
				if task_array['button'][0].collidepoint(ev.pos):
				 d = Play(Items1,Items2,Items3, soundtrack, eatsound,failsound, Kidney, group,screen)
					
		screen.blit(bg,(0,0))
		screen.blit(task_array['items'], (100,0))
		screen.blit(task_array['task'], (0,350))
			
		if cont >= 20:
			screen.blit(task_array['button'][1], (task_array['button'][0].left,task_array['button'][0].top))
			
		pg.display.update()
		
		try:
			if d == "Perdeu" or d == "Ganhou" :
				break
			
		except:
			continue
			
	if d == "Ganhou":
		win_sound.play()
		return "Ok"
		
	elif d == "Perdeu":
		game_over_sound.play()
		return "Not Ok"

def loading_init():
	pg.init()
	screen = pg.display.set_mode((width, height)) 
	
	while True:
		screen.blit(loading,(0,0))
		pg.display.update()
		sleep(3)
		break
	
def End(type):
	c = "continua"
	pg.init()
	screen = pg.display.set_mode((width, height))
	cont = 0
	while True:
		cont += 1
		for ev in pg.event.get():
			if ev.type == pg.MOUSEBUTTONDOWN and cont >= 20:
				c = "acabou"
				break
				
		screen.blit(bg, (0,0))
		if type == win:
			screen.blit(type, (50,200))
			
		elif type in (game_over_image, agradecimentos):
			screen.blit(type,(0,0))
		
		pg.display.update()
		
		try:
			if c == "acabou":
				break
		except:
			continue
	
