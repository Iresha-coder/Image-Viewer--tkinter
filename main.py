from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from preferences import *
from image_create import image_create

global root

root = Tk()
root.title("Image Viewer")
root.iconbitmap('C:/Users')
root.geometry("590x400")
root.configure(bg="white")

global frame_main
global frame_btn
global frame_inter
global btn_width

frame_main = LabelFrame(root, bd=0, bg="white")
frame_btn = LabelFrame(frame_main, bd=0, bg="white")
frame_inter = LabelFrame(frame_main, bd=0, bg="white")

pref_ico = ImageTk.PhotoImage(Image.open("C:/Users/iresh/Documents/black-24dp/2x/outline_settings_black_24dp.png"))

theme_op = [
	"Light",
	"Dark"
]

font_op = [
	"Helvetica",
	"Consolas",
	"Segoe UI Light",
	"Segoe UI Bold",
]

font_size_op = [
	"Small",
	"Medium",
	"Large"
]

clicked_theme = StringVar()
clicked_theme.set(theme_op[0])

clicked_font = StringVar()
clicked_font.set(font_op[0])

clicked_font_size = StringVar()
clicked_font_size.set(font_size_op[1])

btn_width = 40

def chk_font_size(font_size):
	if font_size == "Small":
		return 13
	elif font_size == "Medium":
		return 15
	elif font_size == "Large":
		return 18
	else:
		return 15

# dark theme function
def dark(font, fontsize):
	global root
	global frame_main
	global frame_btn
	global frame_inter
	global l_font_size
	global pref_open

	root.configure(bg="black")

	frame_main.pack_forget()
	frame_inter.pack_forget()
	frame_btn.pack_forget()

	if font == "":
		font = "Helvetica"
 
	if fontsize == "Small":
		btn_width = 30
		root.geometry("560x450")
	elif fontsize == "Medium":
		btn_width = 40
		root.geometry("900x450")
	elif fontsize == "Large":
		btn_width = 43
		root.geometry("1210x450")
	
	if font == "Segoe UI Bold":
		if fontsize == "Small":
			btn_width = 30
			root.geometry("620x450")
		elif fontsize == "Medium":
			btn_width = 40
			root.geometry("970x450")
		elif fontsize == "Large":
			btn_width = 45
			root.geometry("1270x450")


	l_font_size = chk_font_size(fontsize)

	frame_main = LabelFrame(root, bd=0, bg="black", fg="white")
	frame_btn = LabelFrame(frame_main, bd=0, bg="black", fg="white")
	frame_inter = LabelFrame(frame_main, bd=0, bg="black", fg="white")

	open_btn = Button(frame_btn, text="Open Image", bg="black", fg="white", command=open_img, width=btn_width, font=(font, l_font_size))
	pref = Button(frame_btn, text="Preferences", bg="black", fg="white", command=lambda: pref_func(clicked_font.get(), clicked_font_size.get(), btn_width), width=btn_width, font=(font, l_font_size))
	head = Label(frame_inter, text="Image Viewer", bg="gray", fg="blue", justify="center", font=("Segoe UI Bold", 25), bd=5)
	space = Label(frame_inter, text="\n\n\n", bg="black", justify="center")
	intro = Label(frame_inter, text="An open-source image viewer created by Iresha Samarakoon.", bg="black", fg="white", font=("Segoe UI Bold", 13))

	frame_main.pack()
	frame_btn.pack()
	frame_inter.pack()

	open_btn.pack(side=LEFT)
	pref.pack(side=RIGHT)
	head.grid(row=0, column=0, ipadx=10, ipady=10)
	space.grid(row=1, column=0)
	intro.grid(row=2, column=0)

# light theme function
def light(font, fontsize):
	global root
	global frame_main
	global frame_btn
	global frame_inter
	global l_font_size

	frame_main.pack_forget()
	frame_btn.pack_forget()
	frame_inter.pack_forget()

	root.configure(bg="white")

	if font == "":
		font = "Helvetica"
	if font == "Segoe UI Light":
		root.geometry("650x700")

	if fontsize == "Small":
		btn_width = 30
		root.geometry("560x450")
	elif fontsize == "Medium":
		btn_width = 40
		root.geometry("900x450")
	elif fontsize == "Large":
		btn_width = 43
		root.geometry("1210x450")

	if font == "Segoe UI Bold":
		if fontsize == "Small":
			btn_width = 30
			root.geometry("620x450")
		elif fontsize == "Medium":
			btn_width = 40
			root.geometry("970x450")
		elif fontsize == "Large":
			btn_width = 45
			root.geometry("1250x450")

	l_font_size = chk_font_size(fontsize)

	frame_main = LabelFrame(root, bd=0, bg="white")
	frame_btn = LabelFrame(frame_main, bd=0, bg="white")
	frame_inter = LabelFrame(frame_main, bd=0, bg="white")

	open_btn = Button(frame_btn, text="Open Image", bg="white", command=open_img, width=btn_width, font=(font, l_font_size))
	pref = Button(frame_btn, text="Preferences", bg="white", command=lambda: pref_func(clicked_font.get(), clicked_font_size.get(), btn_width), width=btn_width, font=(font, l_font_size))

	head = Label(frame_inter, text="Image Viewer", bg="gray", fg="blue", justify="center", font=("Segoe UI Bold", 25), bd=5)
	space = Label(frame_inter, text="\n\n\n", bg="white", justify="center")
	intro = Label(frame_inter, text="An open-source image viewer created by Iresha Samarakoon.", bg="white", font=("Segoe UI Bold", 13))

	frame_main.pack()
	frame_btn.pack()
	frame_inter.pack()

	open_btn.pack(side=LEFT)
	pref.pack(side=RIGHT)
	head.grid(row=0, column=0, ipadx=10, ipady=10)
	space.grid(row=1, column=0)
	intro.grid(row=2, column=0)

def btn_backward(im_n):
	global image_number
	global frame_img_l
	global frame_a_btn
	global frame_sub
	global img_list
	frame_img_l.pack_forget()
	frame_sub.pack_forget()
	frame_a_btn.pack_forget()
	image_number = image_number - 1
	if clicked_theme.get() == "Dark":
		frame_img_l = LabelFrame(frame_main, bd=0, bg="black")
		frame_sub = LabelFrame(frame_img_l, bd=0, bg="black")
		frame_a_btn = LabelFrame(frame_img_l, bd=0, bg="black")
	else:
		frame_img_l = LabelFrame(frame_main, bd=0, bg="white")
		frame_sub = LabelFrame(frame_img_l, bd=0, bg="white")
		frame_a_btn = LabelFrame(frame_img_l, bd=0, bg="white")
	val = 10
	try:
		img_lab = Label(frame_sub, image=img_list[im_n - 1])
	except IndexError:
		val = 0
		img_lab = Label(frame_sub, image=img_list[0])
	if val == 0:
		button_forward = Button(frame_img_l, text=">>", bg="lightgray", state=DISABLED, font=("Segoe UI Bold", 16))
		button_backward = Button(frame_img_l, text="<<", bg="lightgray", state=DISABLED, font=("Segoe UI Bold", 16))
	else:
		button_forward = Button(frame_img_l, text=">>", bg="lightgray", command=lambda: btn_forward(image_number), font=("Segoe UI Bold", 16))
		button_backward = Button(frame_img_l, text="<<", bg="lightgray", command=lambda: btn_backward(image_number), font=("Segoe UI Bold", 16))
	if image_number == 0:
		button_backward = Button(frame_img_l, text="<<", bg="lightgray", state=DISABLED, font=("Segoe UI Bold", 16))
	frame_img_l.pack()
	frame_sub.pack()
	frame_a_btn.pack()
	img_lab.pack()
	button_backward.pack(side=LEFT, padx=0, pady=10, ipadx=10, ipady=5)
	button_forward.pack(side=RIGHT, padx=0, pady=10, ipadx=10, ipady=5)

def btn_forward(im_n):
	global img_num
	global image_number
	global frame_img_l
	global frame_sub
	global frame_a_btn
	global img_list
	frame_img_l.pack_forget()
	frame_sub.pack_forget()
	frame_a_btn.pack_forget()
	image_number = image_number + 1
	if clicked_theme.get() == "Dark":
		frame_img_l = LabelFrame(frame_main, bd=0, bg="black")
		frame_sub = LabelFrame(frame_img_l, bd=0, bg="black")
		frame_a_btn = LabelFrame(frame_img_l, bd=0, bg="black")
	else:
		frame_img_l = LabelFrame(frame_main, bd=0, bg="white")
		frame_sub = LabelFrame(frame_img_l, bd=0, bg="white")
		frame_a_btn = LabelFrame(frame_img_l, bd=0, bg="white")
	val = 10
	try: 
		img_lab = Label(frame_sub, image=img_list[im_n + 1])
	except IndexError:
		val = 1
		img_lab = Label(frame_sub, image=img_list[0])
	if val == 1:
		button_backward = Button(frame_img_l, text="<<", bg="lightgray", state=DISABLED, font=("Segoe UI Bold", 16))
		button_forward = Button(frame_img_l, text=">>", bg="lightgray", state=DISABLED, font=("Segoe UI Bold", 16))
	else:
		button_backward = Button(frame_img_l, text="<<", bg="lightgray", command=lambda: btn_backward(image_number), font=("Segoe UI Bold", 16))
		button_forward = Button(frame_img_l, text=">>", bg="lightgray", command=lambda: btn_forward(image_number), font=("Segoe UI Bold", 16))
	if len(img_list) == image_number + 1:
		button_forward = Button(frame_img_l, text=">>", bg="lightgray", state=DISABLED, font=("Segoe UI Bold", 18))
	frame_img_l.pack()
	frame_sub.pack()
	frame_a_btn.pack()
	img_lab.pack()
	button_backward.pack(side=LEFT, padx=0, pady=10, ipadx=10, ipady=5)
	button_forward.pack(side=RIGHT, padx=0, pady=10, ipadx=10, ipady=5)

def img_enter():
	global path_list
	global img_num
	global image_number
	global frame_img_l
	global frame_sub
	global frame_a_btn
	global frame_btn
	global img_list
	global val
	global pref_open
	pref_open = 0
	image_number = 0
	val = 1
	path_list = []
	img_list = []
	img_num = imnum_en.get()
	frame_btn.pack_forget()
	for i in range(1, int(img_num) + 1):
		root.filename = filedialog.askopenfilename(initialdir="C:/Users/iresh/Pictures", title="Select A File", filetypes=(("PNG Files", "*.png"), ("JPEG Files", "*.jpeg"), ("JPG Files", ".jpg"), ("All Files", "*.*")))
		path_list.append(str(root.filename))
		frame_inter.pack_forget()
	if clicked_theme.get() == "Dark":
		frame_img_l = LabelFrame(frame_main, bd=0, bg="black")
		frame_sub = LabelFrame(frame_img_l, bd=0, bg="black")
		frame_a_btn = LabelFrame(frame_img_l, bd=0, bg="black")
		frame_btn = LabelFrame(frame_main, bd=0, bg="black")
	else:
		frame_img_l = LabelFrame(frame_main, bd=0, bg="white")
		frame_sub = LabelFrame(frame_img_l, bd=0, bg="white")
		frame_a_btn = LabelFrame(frame_img_l, bd=0, bg="white")
		frame_btn = LabelFrame(frame_main, bd=0, bg="white")
	if clicked_theme.get() == "Dark":
		open_btn = Button(frame_btn, text="Open Image", bg="black", fg="white", command=open_img, width=btn_width, font=(clicked_font.get(), chk_font_size(clicked_font_size.get())))
		pref = Button(frame_btn, text="Preferences", bg="black", fg="white", command=lambda: pref_func(clicked_font.get(), clicked_font_size.get(), btn_width), width=btn_width, font=(clicked_font.get(), chk_font_size(clicked_font_size.get())))
	else:
		open_btn = Button(frame_btn, text="Open Image", bg="white", command=open_img, width=btn_width)
		pref = Button(frame_btn, text="Preferences", bg="white", command=lambda: pref_func(clicked_font.get(), 
		clicked_font_size.get(), btn_width), width=btn_width, font=(clicked_font.get(), chk_font_size(clicked_font_size.get())))
	img_list = image_create(img_num, path_list)
	img_lab = Label(frame_sub, image=img_list[image_number], padx=10, pady=10)
	if int(img_num) == 1:
		button_forward = Button(frame_img_l, text=">>", bg="lightgray", state=DISABLED, bd=1, font=("Segoe UI Bold", 18))
	else:
		button_forward = Button(frame_img_l, text=">>", bg="lightgray", command=lambda: btn_forward(image_number), bd=1, font=("Segoe UI Bold", 18))
	button_backward = Button(frame_img_l, text="<<", bg="lightgray", state=DISABLED, bd=1, font=("Segoe UI Bold", 18))

	frame_btn.pack()
	frame_img_l.pack()
	frame_sub.pack()
	frame_a_btn.pack()
	img_lab.pack()

	open_btn.pack(side=LEFT)
	pref.pack(side=RIGHT)
	button_backward.pack(side=LEFT, padx=0, pady=10, ipadx=10, ipady=5)
	button_forward.pack(side=RIGHT, padx=0, pady=10, ipadx=10, ipady=5)

def save_pref():
	if clicked_font.get() == "Helvetica":
		if clicked_theme.get() == "Dark":
			dark("Helvetica", clicked_font_size.get())
		elif clicked_theme.get() == "Light":
			light("Helvetica", clicked_font_size.get())
	elif clicked_font.get() == "Consolas":
		if clicked_theme.get() == "Dark":
			dark("Consolas", clicked_font_size.get())
		elif clicked_theme.get() == "Light":
			light("Consolas", clicked_font_size.get())
	elif clicked_font.get() == "Segoe UI Bold":
		if clicked_theme.get() == "Dark":
			dark("Segoe UI Bold", clicked_font_size.get())
		elif clicked_theme.get() == "Light":
			light("Segoe UI Bold", clicked_font_size.get())
	elif clicked_font.get() == "Segoe UI Light":
		if clicked_theme.get() == "Dark":
			dark("Segoe UI Light", clicked_font_size.get())
		elif clicked_theme.get() == "Light":
			light("Segoe UI Light", clicked_font_size.get())
	else:
		pass

def open_img():
	global open_w
	global imnum_en
	if clicked_theme.get() == "Dark":
		if clicked_font.get() == "Helvetica":
			font = "Helvetica"
		elif clicked_font.get() == "Consolas":
			font = "Consolas"
		elif clicked_font.get() == "Segoe UI Bold":
			font = "Segoe UI Bold"
		elif clicked_font.get() == "Segoe UI Light":
			font = "Segoe UI Light"
		open_w = Toplevel()
		open_w.title("Open Image")
		open_w.configure(bg="black")
		open_w.geometry("630x115")
		ask_im_num = Label(open_w, text="How many images do you want to open?", bd=2, bg="black", fg="white", font=(font, 16))
		imnum_en = Entry(open_w, bd=0, bg="lightGray", font=(font, 14))
		im_enter_btn = Button(open_w, text="Enter", bg="black", fg="white", font=(font, 12), command=img_enter)

		ask_im_num.grid(row=0, column=0, ipadx=10, ipady=10)
		imnum_en.grid(row=0, column=1)
		im_enter_btn.grid(row=1, column=0, columnspan=2, ipadx=10, ipady=5)
	else:
		if clicked_font.get() == "Helvetica":
			font = "Helvetica"
		elif clicked_font.get() == "Consolas":
			font = "Consolas"
		elif clicked_font.get() == "Segoe UI Bold":
			font = "Segoe UI Bold"
		elif clicked_font.get() == "Segoe UI Light":
			font = "Segoe UI Light"
		open_w = Toplevel()
		open_w.title("Open Image")
		open_w.configure(bg="white")
		open_w.geometry("630x115")
		ask_im_num = Label(open_w, text="How many images do you want to open?", bd=2, bg="white", font=(font, 16))
		imnum_en = Entry(open_w, bd=0, bg="lightGray", font=(font, 14))
		im_enter_btn = Button(open_w, text="Enter", font=(font, 12), command=img_enter)

		ask_im_num.grid(row=0, column=0, ipadx=10, ipady=10)
		imnum_en.grid(row=0, column=1)
		im_enter_btn.grid(row=1, column=0, columnspan=2, ipadx=10, ipady=5)

def pref_func(font, fontsize, btn_width):
	global pref_open
	global l_font_size

	pref_open = 1

	l_font_size = chk_font_size(fontsize)

	if clicked_theme.get() == "Light":
		pw = Toplevel()
		pw.title("Preferences")
		pw.geometry("400x300")
		pw.configure(bg="white")

		frame_pref = LabelFrame(pw, bd=0, bg="white")
		frame_save = LabelFrame(pw, bd=0, bg="white")

		theme_lb = Label(frame_pref, text="Theme: ", bd=0, bg="white", font=("Helvetica", 18))
		theme_drop = OptionMenu(frame_pref, clicked_theme, *theme_op)

		font_lb = Label(frame_pref, text="Font: ", bd=0, bg="white", font=("Helvetica", 18))
		font_drop = OptionMenu(frame_pref, clicked_font, *font_op)

		font_size_lb = Label(frame_pref, text="Font Size: ", bd=0, bg="white", font=(clicked_font.get(), 18))
		font_size_drop = OptionMenu(frame_pref, clicked_font_size, *font_size_op)

		pref_save = Button(frame_save, text="Save", command=save_pref)

		frame_pref.pack()
		frame_save.pack(side=BOTTOM)

		theme_lb.grid(row=0, column=0, ipadx=10, ipady=10)
		theme_drop.grid(row=0, column=1)
		font_lb.grid(row=1, column=0, ipadx=10, ipady=10)
		font_drop.grid(row=1, column=1)
		font_size_lb.grid(row=2, column=0, ipadx=10, ipady=10)
		font_size_drop.grid(row=2, column=1)
		pref_save.grid(row=0, column=0)
	elif clicked_theme.get() == "Dark":
		root.configure(bg="black")

		font = clicked_font.get()

		if font == "":
			font = "Helvetica"
		if font == "Segoe UI Light":
			root.geometry("950x500")

		pw = Toplevel()
		pw.title("Preferences")
		pw.geometry("400x300")
		pw.configure(bg="black")

		frame_pref = LabelFrame(pw, bd=0, bg="black")
		frame_save = LabelFrame(pw, bd=0, bg="black")

		theme_lb = Label(frame_pref, text="Theme: ", bd=0, bg="black", font=("Helvetica", 18), fg="white")
		theme_drop = OptionMenu(frame_pref, clicked_theme, *theme_op)

		font_lb = Label(frame_pref, text="Font: ", bd=0, bg="black", font=("Helvetica", 18), fg="white")
		font_drop = OptionMenu(frame_pref, clicked_font, *font_op)

		font_size_lb = Label(frame_pref, text="Font Size: ", bd=0, bg="black", font=(clicked_font.get(), 18), fg="white")
		font_size_drop = OptionMenu(frame_pref, clicked_font_size, *font_size_op)

		pref_save = Button(frame_save, text="Save", command=save_pref)

		frame_pref.pack()
		frame_save.pack(side=BOTTOM)

		theme_lb.grid(row=0, column=0, ipadx=10, ipady=10)
		theme_drop.grid(row=0, column=1)
		font_lb.grid(row=1, column=0, ipadx=10, ipady=10)
		font_drop.grid(row=1, column=1)
		font_size_lb.grid(row=2, column=0, ipadx=10, ipady=10)
		font_size_drop.grid(row=2, column=1)
		pref_save.grid(row=0, column=0)

open_btn = Button(frame_btn, text="Open Image", bg="white", command=open_img, width=btn_width)
pref = Button(frame_btn, text="Preferences", bg="white", command=lambda: pref_func(clicked_font.get(), clicked_font_size.get(), btn_width), width=btn_width)

head = Label(frame_inter, text="Image Viewer", bg="gray", fg="blue", justify="center", font=("Segoe UI Bold", 25), bd=5)
space = Label(frame_inter, text="\n\n\n", bg="white", justify="center")
intro = Label(frame_inter, text="An open-source image viewer created by Iresha Samarakoon.", bg="white", font=("Segoe UI Bold", 13))

frame_main.pack()
frame_btn.pack()
frame_inter.pack()

open_btn.pack(side=LEFT)
pref.pack(side=RIGHT)
head.grid(row=0, column=0, ipadx=10, ipady=10)
space.grid(row=1, column=0)
intro.grid(row=2, column=0)

root.mainloop()		