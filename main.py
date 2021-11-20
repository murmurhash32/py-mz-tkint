from tkinter import *




def grided(canvas, line_distance):
	canvas.create_line(10, 0, 10, 10, fill=BLACK)
	canvas.create_line(10, 10, 20, 10, fill=BLACK)

	"""
	for x in range(line_distance, canvas_width, line_distance):
		canvas.create_line(x, 0, x, canvas_height, fill=BLACK)
	for y in range(line_distance, canvas_height, line_distance):
		canvas.create_line(0, y, canvas_width, y, fill=BLACK)
	"""




if __name__ == "__main__":
	BLACK = "#000000"

	master = Tk()
	canvas_width = 200
	canvas_height = 200 
	c = Canvas(master, 
				width=canvas_width,
				height=canvas_height)
	c.pack()
	
	grided(c, 5)
	mainloop()