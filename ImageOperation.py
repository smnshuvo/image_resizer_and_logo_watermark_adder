from PIL import Image, ImageDraw, ImageFont
import os
import copy


class ImageOperation:
    def __init__(self, image):
        self.image = image
        # Copy the variable rather than reference
        self.backup = copy.copy(self.image)
        global width, height
        width, height = self.image.size

    @staticmethod
    def get_position(p):
        print(width)
        return {
            1: (10, 10),
            2: (10, height-50),
            3: (width-150, 10),
            4: (width-150, height-50),
            5: (width/2-width/6, height/2),
        }.get(p, 1)

    def add_water_mark(self, text, position):
        pos = self.get_position(position)
        self.image = copy.copy(self.backup)
        draw = ImageDraw.Draw(self.image)
        # maintain a ratio
        font = ImageFont.truetype('arial.ttf', int(height/15))
        draw.text(pos, text, font=font)
        # create the thumb again
        self.create_thumb()

    def resize_image(self, size):
        self.image.thumbnail(size)

    def create_thumb(self):
        # convert the ratio
        size_480 = (480, int((height*480)/width))
        self.image.thumbnail(size_480)
        self.save_thumb()

    def save_thumb(self):
        if not os.path.exists('temp'):
            os.makedirs('temp')
        self.image.save("temp/thumb.png")


