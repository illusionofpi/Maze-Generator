# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 11:13:56 2018

@author: Pye Sone Kyaw
"""
import pygame
import sys
import random
from button import Button
import time
from maze_functions import*
import colors

stack = [] #to put the last known free pathway, in a stack data structure for popping
grid = [] #list of the squares' coordinates to reference 
visited = [] #ones already been to
solution = {} #for the traceback to start 

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) #initialise window given dimensions
    pygame.display.set_caption("Python Maze Generator") #window title
    clock = pygame.time.Clock()
    button = Button(screen, (0,255,0) , "Solution")
    button.draw_button()
    draw_grid(screen, grid)            
    carve_out_maze(screen, grid, stack, visited, solution)  
    running = True
    while running:
        event_checker(button, solution, screen)
run_game()