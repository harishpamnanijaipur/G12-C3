# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 18:26:20 2021

@author: dell
"""

import pygame,sys

#initialising pygame and its functions 
pygame.init()

# creating game window and title
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("asteroid")

# Display game window 
background_image = pygame.image.load("bg2.jpg").convert()
screen.fill((0,0,0))
screen.blit(background_image,[0,0])


#Creating Players 
player=pygame.Rect(200,200,30,30)
player_image = pygame.image.load("s4.png").convert_alpha()
screen.blit(player_image , player)
pygame.display.update()

playerSpeed=20
angle=0
change=0
speed=5
press=False

while True:
  screen.blit(background_image,[0,0])
  #event loop to check which key is print
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
      
    if event.type == pygame.KEYUP:
      if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
        change= 0
      if event.key == pygame.K_UP:
        press=False
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        change =30
      if event.key ==pygame.K_RIGHT:
        change = -30
      if event.key == pygame.K_UP:
        press=True;   
        
  angle += change
  angle=angle % 360
  newimg=pygame.transform.rotate(player_image,angle)

 
  screen.blit(newimg , player)
  
  
  pygame.display.update()






#Game Loop
'''while True:
  
  screen.blit(background_image,[0,0])
  #event loop to check which key is print
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYUP:
      if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
        change= 0
      if event.key == pygame.K_UP:
        press=False'''