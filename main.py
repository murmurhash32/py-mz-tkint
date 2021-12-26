from tkinter import *
import pandas as pd
import numpy as np
import random


PATHCOLOR = "Blue"	# "#0000FF"
WALLCOLOR = "Black" # "#000000"


def path_build(): 
	pass


def build_walls(canvas, dist_btw_lines):
	canvas.create_line(10, 0, 10, 10, fill="Black")
	canvas.create_line(10, 10, 20, 10, fill="Black")

	for x in range(dist_btw_lines, canvas_width, dist_btw_lines):
		canvas.create_line(x, 0, x, canvas_height, fill="Black")
	for y in range(dist_btw_lines, canvas_height, dist_btw_lines):
		canvas.create_line(0, y, canvas_width, y, fill="Black")


def hitomezashi(canvas, dist_btw_lines):
	for x in range(dist_btw_lines, canvas_width, dist_btw_lines):
		if bool(random.getrandbits(1)):
			for i in range(dist_btw_lines, canvas_height, 2*dist_btw_lines):
				canvas.create_line(x, i, x, i+dist_btw_lines+1, fill="Black") # fill last pix too
		else:
			for i in range(0, canvas_height, 2*dist_btw_lines):
				canvas.create_line(x, i, x, i+dist_btw_lines+1, fill="Black")

	for y in range(dist_btw_lines, canvas_height, dist_btw_lines):
		if bool(random.getrandbits(1)):
			for i in range(dist_btw_lines, canvas_width, 2*dist_btw_lines):
				canvas.create_line(i, y, i+dist_btw_lines+1, y, fill="Black")
		else:
			for i in range(0, canvas_width, 2*dist_btw_lines):
				canvas.create_line(i, y, i+dist_btw_lines+1, y, fill="Black")




#def path_color(canvas):
#	canvas.create_rectangle(10,10,20,20, fill = "Blue")




def main():
	master = Tk()
	canvas_width = 500
	canvas_height = 500 
	c = Canvas(master, width=canvas_width, height=canvas_height)
	c.pack()

	#build_walls(c, 10)
	hitomezashi(c,10)
	mainloop()


if __name__ == "__main__":
	main()
	
