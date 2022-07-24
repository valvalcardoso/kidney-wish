import pygame as pg
from database import Kidney_image
pg.init()

#Classes and Functions

class MyKidney(pg.sprite.Sprite):
	
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		#tamanho do objeto
		self.w = 300
		self.h = 300
		
		#Imagem e Rect do objeto. 
		self.image = Kidney_image
		self.rect = self.image.get_rect()
		self.rect[0] = 250
		self.rect[1] = 800
		self.rect[2] = self.w
		self.rect[3] = self.h
		
		#Isso garanti que o objeto esteja parado.
		self.left = False
		self.right = False
		self.hit = 0
		self.error = 0
	
	#Faz com que o objeto faça algo durante o loop.
	def update(self):
		
		#Se o atributo self.left for verdadeiro e a sua posição em relação à esquerda da tela for menor que 530.
		if self.left and self.rect[0] < 530:
			self.toleft()
			
		elif self.right and self.rect[0] > - 48:
			self.toright()
	
	#Move o rect/imagem para a direita. 
	def toleft(self):
		self.rect.left += 35
	
	#Move o rect/imagem para a esquerda. 	
	def toright(self):
		self.rect.right -= 35
		
		
class Item(pg.sprite.Sprite):
		
	def __init__(self, img, pos):
		
		pg.sprite.Sprite.__init__(self)
		
		self.image = img
		self.rect = self.image.get_rect()
		self.rect[0] = pos[0]
		self.rect[1] = pos[1]
		self.onscreen = True	
		self.type = "wrong"
		self.velocidade = 30
		self.there = False
		
	def update(self):
		if self.there:
			self.rect.top += self.velocidade
			
		if self.rect.left <= 10:
			self.rect.left += 30
				
		elif self.rect.left >= 600:
			self.rect.left -= 30
		

class BuildItem:
	
	def __init__(self,left, imgs,screen, group, right_images):
		#self.imgs vai receber um array com as imagens referentes à task.
		self.imgs = imgs
		self.screen = screen
		self.group = group 
		self.left = left
		
		#O primeiro array garanti que um objeto irá existir e o outro garanti que o objeto irá aparecer na tela.
		self.array = []
		self.onscreen = []
		
		#Para cada imagem um objeto será criado e adicionado ao array. 
		for img in self.imgs:
			item = Item(img,(left, -200))
			self.array.append(item)
			
		#Para cada imagem referente ao item certo.
		for img in right_images:
			item = Item(img,(left, - 200))
			item.type = "right"
			self.array.append(item)
			
			
	def update(self, cont, kidney, ok, fail):
		from random import choice
		
		#momentos em que os itens podem aparecer. 
		moment = (20,30,40)
		
		#se o cont for divisível por um desses momentos. 
		if cont % choice(moment) == 0:
			#escolhe uma imagem aleatória. 
			Chosen = choice(self.array)
			self.group.add(Chosen)
			self.onscreen.append(Chosen)
			Chosen.there = True
		
		#Se esse item estiver na tela:
		for thing in self.onscreen:
			pos = [thing.rect.left, thing. rect.left + 5,thing.rect.left - 5]
			thing.rect.left = choice(pos)
			thing.update()
			self.collide(thing, kidney, ok, fail)
			thing.rect.width = 50
			thing.rect.height = 50
			
	def collide(self, item, obj, ok, fail):
		
		#se haver colisão entre o rim e o item.
		if pg.sprite.collide_mask(item,obj) or item.rect.top > 1200:
			
			if pg.sprite.collide_mask(item,obj):
				item.rect.left = -400
				if item.type == "right":
					ok.set_volume(0.9)
					obj.hit += 1
					ok.play()
					
				elif item.type == "wrong":
					obj.error += 1
					fail.play()
			
			#remove de tudo.
			self.group.remove(item)
			self.onscreen.remove(item)
			item.rect.left = self.left
			item.rect.top = -200
			item.there = False
