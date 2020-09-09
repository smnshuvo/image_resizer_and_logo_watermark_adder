from PIL import Image
from file_validator import is_image
from ImageOperation import ImageOperation
from tkinter import *
import os

# open image
def open_image():
    # remove the current frame
    base_f.forget()


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
size_640 = (640,640)
for img in os.listdir(i_dir):
    img_name, img_ext = os.path.splitext(img)
    # full directory
    f_dir = i_dir+"/"+img
    # create a folder if doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')
    if is_image(img_ext):
        crnt_img = Image.open(f_dir)
        # make a water mark there
        my_image = ImageOperation(crnt_img)
        my_image.resize_image(size_640)
        my_image.add_water_mark("Shuvo")
        crnt_img.save('output/{}.png'.format(img_name))


