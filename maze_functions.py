import pygame
import sys
import random
from button import Button
import time
from colors import*
#dimensions
WIDTH = 440
HEIGHT = 640
w=20

def draw_grid(screen,grid): 
	x = 20
	y = 0
  
	for i in range(1,21): # 1 to 20 for 20 cells
		x = 20 #reset x coordinate
		y = y + 20 #add a new row
		for j in range(1,21):
			pygame.draw.line(screen , WHITE, [x,y], [x+w,y]) #where, color, start, end for TOP border
			pygame.draw.line(screen, WHITE, [x,y], [x,y+w]) #left
			pygame.draw.line(screen, WHITE, [x+w,y], [x+w,y+w]) #right
			pygame.draw.line(screen, WHITE, [x,y+w], [x+w,y+w]) #bottom
			grid.append((x,y)) #add the cell to the list of grids, by adding the x and y coordinate of top left corner
			x += 20 #move cell to next position to the right


def move_up(screen, x, y):
	pygame.draw.rect(screen, BLUE, (x + 1, y - w + 1, 19, 39))           # draw a rectangle twice the width of the cell 
	pygame.display.update()                                              # one pixel from left, one pixel down from top to keep border


def move_down(screen, x, y):
	pygame.draw.rect(screen, BLUE, (x +  1, y + 1, 19, 39))
	pygame.display.update()


def move_left(screen, x, y):
	pygame.draw.rect(screen, BLUE, (x - w +1, y +1, 39, 19))
	pygame.display.update()


def move_right(screen, x, y):
	pygame.draw.rect(screen, BLUE, (x +1, y +1, 39, 19))
	pygame.display.update()                               

def current_cell(screen, x, y):
	pygame.draw.rect(screen, GREEN, (x +1, y +1, 18, 18))          # draw a single width cell
	pygame.display.update()

def backtracking_cell(screen, x, y):
	pygame.draw.rect(screen, BLUE, (x +1, y +1, 18, 18))        # used to re-colour the path after single_cell
	pygame.display.update()  

def solution_cell(screen, x,y):
	pygame.draw.rect(screen, RED, (x+8, y+8, 5, 5))             # used to show the solution
	pygame.display.update()                                        # has visited cell

def carve_out_maze(screen, grid, stack, visited, solution, x=20, y=20):
	stack.append((x,y))                                            # place starting cell into stack
	visited.append((x,y))                                          # add starting cell to visited list
	while len(stack) > 0:                                          # loop until stack is empty
		time.sleep(.01)                                    
		cell = []                                                  # define cell list
		if (x + w, y) not in visited and (x + w, y) in grid:       # right cell available?
			cell.append("right")                                   # if yes add to cell list

		if (x - w, y) not in visited and (x - w, y) in grid:       # left cell available?
			cell.append("left")

		if (x , y + w) not in visited and (x , y + w) in grid:     # down cell available?
			cell.append("down")

		if (x, y - w) not in visited and (x , y - w) in grid:      # up cell available?
			cell.append("up")

		if len(cell) > 0:                                          # check to see if cell list is empty
			cell_chosen = (random.choice(cell))                    # select one of the cell randomly

			if cell_chosen == "right":                             # if this cell has been chosen
				move_right(screen, x, y)                                   # call push_right function
				solution[(x + w, y)] = x, y                        # solution = dictionary key = new cell, other = current cell
				x = x + w                                          # make this cell the current cell
				visited.append((x, y))                              # add to visited list
				stack.append((x, y))                                # place current cell on to stack

			elif cell_chosen == "left":
				move_left(screen, x, y)
				solution[(x - w, y)] = x, y
				x = x - w
				visited.append((x, y))
				stack.append((x, y))

			elif cell_chosen == "down":
				move_down(screen, x, y)
				solution[(x , y + w)] = x, y
				y = y + w
				visited.append((x, y))
				stack.append((x, y))

			elif cell_chosen == "up":
				move_up(screen, x, y)
				solution[(x , y - w)] = x, y
				y = y - w
				visited.append((x, y))
				stack.append((x, y))
		else:
			x, y = stack.pop()                                    # if no cells are available pop one from the stack
			current_cell(screen, x, y)                                     # use single_cell function to show backtracking image
			time.sleep(.05)                                       # slow program down a bit
			backtracking_cell(screen, x, y) 
def plot_route_back(solution, screen, x, y):
	solution_cell(screen, x, y)                                          # solution list contains all the coordinates to route back to start
	while (x, y) != (20,20):                                     # loop until cell position == start position
		x, y = solution[x, y]                                    # "key value" now becomes the new key
		solution_cell(screen, x, y)                                      # animate route back
		time.sleep(.01)
def color_box(grid, screen):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	for i in range(0,len(grid)):
		if int(mouse_x) >= int(grid[i][0]) and int(mouse_x) < int((grid[i][0] + 20)) and int(mouse_y) >= int(grid[i][1]) and int(mouse_y) < int((grid[i][1] + 20)) :
			pygame.draw.rect(screen, YELLOW, (grid[i][0] + 5, grid[i][1] + 5, 10, 10))
			pygame.display.update()
def event_checker(button, solution, screen):
	event = pygame.event.poll()
	if event.type == pygame.MOUSEBUTTONDOWN:
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if button.rect.collidepoint(mouse_x, mouse_y):
			plot_route_back(solution, screen, 400, 400)         

		else:
			color_box(grid,screen)  
	# check for closing the window
	elif event.type == pygame.QUIT:
		pygame.quit()
		sys.exit()
		running = False
