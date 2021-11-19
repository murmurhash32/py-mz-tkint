from tkinter import *

Black = "#000000"

master = Tk()
canvas_width = 200
canvas_height = 200 
c = Canvas(master, 
			width=canvas_width,
			height=canvas_height)
c.pack()


def grided(canvas, line_distance):
	canvas.create_line(10, 0, 10, 10, fill=Black)
	canvas.create_line(10, 10, 20, 10, fill=Black)

	"""
	for x in range(line_distance, canvas_width, line_distance):
		canvas.create_line(x, 0, x, canvas_height, fill=Black)
	for y in range(line_distance, canvas_height, line_distance):
		canvas.create_line(0, y, canvas_width, y, fill=Black)
	"""




grided(c, 5)

mainloop()