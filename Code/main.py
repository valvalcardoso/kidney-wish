#trabalho de Biologia - funcionalidades do sistema excretor.
#Kidney Wish.

__authors__ = "equipe 8"
from task import *
import pygame as pg

pg.init()

		
fase1 = "none"
fase2 = "none"
fase3 = "none"
cont = 0

while True:
	cont += 1
	
	if cont == 1:
		loading_init()
	
	if fase1 != "Ok":
		fase1 = Init(task1)

	if fase1 == "Ok":
		End(win)
		loading_init()
		fase2 = Init(task2)
		print(fase2)
		
		if fase2 == "Ok":
			End(win)
			loading_init()
			fase3 = Init(task3)
			
			if fase3 == "Ok":
				End(win)
				loading_init()
				End(agradecimentos)
				pg.quit()
				break
				
			elif fase3 == "Not Ok":
				End(game_over_image)
				break
				
			
		elif fase2 == "Not Ok":
			print(fase2)
			End(game_over_image)
			break
	
	elif fase1 == "Not Ok":
		End(game_over_image)
		break
		
	pg.display.update()
				
	
	
