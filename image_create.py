from tkinter import messagebox
from PIL import ImageTk, Image
from sys import exit

def image_create(path_list):
	img_list = []
	for x in path_list:
		try:	
			img = ImageTk.PhotoImage(Image.open(x))
			img_list.append(img)
		except AttributeError:
			messagebox.showerror("No Image Selected", "No Image Selected. Try Again!")
			exit(0)
	return img_list