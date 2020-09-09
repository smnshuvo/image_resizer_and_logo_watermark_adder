from PIL import Image
from file_validator import is_image
from ImageOperation import ImageOperation
import os
# input directory
i_dir = "input"
# output directory
o_dir = "output"

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


