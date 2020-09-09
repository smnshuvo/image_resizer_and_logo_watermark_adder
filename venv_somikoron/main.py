import PIL.Image
from file_validator import is_image
from ImageOperation import ImageOperation
from tkinter import *
from tkinter import filedialog as fd
import os

# open image
def open_image():
    # remove the current frame
    base_f.forget()
    single_image_activity()



# single image edit activity
def single_image_activity():
    # input image
    i_img = fd.askopenfilename()
    # Single Image Frame
    simg_w = "Add Text Water Mark or logo water mark"
    simg_f = LabelFrame(base_w, text=simg_w, width=1280, height=480)
    simg_f.pack(padx=10, pady=10)
    # image thumbnail
    # making the img_view fixed my issue of not getting the image
    global img_view
    img_view = PhotoImage(file=i_img)
    i_canvas = Canvas(simg_f, width=480, height=480, bg="white")

    # Add images wo the canvas
    try:
        canvas_image = i_canvas.create_image(20,20, anchor=NW,image=img_view)
    except Exception as e:
        print(e)
    i_canvas.pack()





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

