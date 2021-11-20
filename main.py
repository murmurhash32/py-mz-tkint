from tkinter import *
import pandas as pd


def path_build():
	head


def path_walls(canvas, line_distance):
	canvas.create_line(10, 0, 10, 10, fill="Black")
	canvas.create_line(10, 10, 20, 10, fill="Black")

	for x in range(line_distance, canvas_width, line_distance):
		canvas.create_line(x, 0, x, canvas_height, fill="Black")
	for y in range(line_distance, canvas_height, line_distance):
		canvas.create_line(0, y, canvas_width, y, fill="Black")


def path_color(canvas):
	canvas.create_rectangle(10,10,20,20, fill = "Blue")



if __name__ == "__main__":
	#Black = "#000000"
	#Blue = "#0000FF"


	master = Tk()
	canvas_width = 200
	canvas_height = 200 
	c = Canvas(master, width=canvas_width, height=canvas_height)
	c.pack()

	path_walls(c, 20)
	mainloop()