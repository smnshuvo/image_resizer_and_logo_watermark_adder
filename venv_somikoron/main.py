import PIL.Image
from file_validator import is_image
from ImageOperation import ImageOperation
from tkinter import *
from tkinter import filedialog as fd
import os

# Reload Image View
def refresh_imgview():
    try:
        img = PhotoImage(file="temp/thumb.png")
        new_img = i_canvas.create_image(20,20, anchor=NW,image=img)
    except Exception as e:
        print(e)
    finally:
        i_canvas.itemconfigure(canvas_image, image=new_img) # producing some exceptions

# add watermark
def add_wmark(wmark_text, position):
    t_img_obj.add_water_mark(wmark_text, position)
    refresh_imgview()

# setPosition
def set_position():
    # selection = "You selected the option " + str(p_var.get()) + "for text " + wmark_text.get()
    try:
        # Watermark text
        w_text = wmark_text.get()
    except Exception:
        print("couldn't get text")
        w_text = ""
    finally:
        add_wmark(w_text, p_var.get())

# open image
def open_image():
    # remove the current frame
    base_f.forget()
    single_image_activity()


# add images to the canvas
"""
i_canvas -> canvas
img_view -> image to add
"""
def add_to_canvas(i_canvas, img_view):
    global canvas_image
    try:
        canvas_image = i_canvas.create_image(20,20, anchor=NW,image=img_view)
    except Exception as e:
        print(e)
    i_canvas.grid(row=0, column=0)


# single image edit activity
def single_image_activity():
    # input image
    i_img = fd.askopenfilename()
    # tools' frame
    tool_f = Frame(base_w)
    tool_f.grid(row=0, column=0, padx=20)
    # water mark
    w_label = Label(tool_f, text="Water Mark")
    w_label.grid(row=0, column=1, sticky=W)
    # watermark text
    global wmark_text
    wmark_text = StringVar()
    w_text = Entry(tool_f, textvariable=wmark_text)
    # position of the entry
    w_text.grid(row=0, column=2)
    # water mark position
    w_positions = [
        ("top right", 1),
        ("top left", 2),
        ("bottom right", 3),
        ("bottom left", 4),
        ("center", 5)
    ]
    # Water Mark Position Text
    wp_label = Label(tool_f, text="Position")
    wp_label.grid(row=1, column=1, sticky=W)
    # global position variable
    global p_var
    p_var = IntVar()
    # position text, position value
    for p_text, p_value in w_positions:
        # Radio Button
        r_button = Radiobutton(tool_f, text=p_text, variable=p_var, value=p_value, command=set_position)
        # stick to the west of that column
        r_button.grid(row=p_value, column=2, sticky=W)
    # Single Image Frame
    simg_w = "Preview"
    simg_f = LabelFrame(base_w, text=simg_w, width=1280, height=480)
    simg_f.grid(row=0,column=1)
    # image thumbnail
    t_img = PIL.Image.open(i_img)
    # make a global image object
    global t_img_obj
    t_img_obj = ImageOperation(t_img)
    t_img_obj.create_thumb()
    # making the img_view fixed my issue of not getting the image
    global img_view
    # load the thumb rather than actual image
    img_view = PhotoImage(file="temp/thumb.png")
    # Image Canvas
    global i_canvas
    i_canvas = Canvas(simg_f, width=480, height=480, bg="white")

    # Add images wo the canvas
    add_to_canvas(i_canvas, img_view)





# input directory
i_dir = "input"
# output directory
o_dir = "output"
w_text = "Either choose open image to open a single image\nOr choose batch to modify all images at once"
# base window
base_w = Tk()
base_w.title("Developed by SMN Shuvo")
# base frame
base_f = LabelFrame(base_w, text=w_text, padx=10, pady=10)
base_f.pack(padx=20, pady=20)
# Open image button
base_o_img_btn = Button(base_f, command=open_image, text="Open image")
base_o_img_btn.pack()
base_o_img_btn.config(width = 30)
# Text
base_txt_or = Label(base_f, text="Or")
base_txt_or.pack()
# Batch image button
base_o_batch_btn = Button(base_f,  text="Select Batch")
base_o_batch_btn.pack()
base_o_batch_btn.config(width = 30)
base_w.mainloop()

