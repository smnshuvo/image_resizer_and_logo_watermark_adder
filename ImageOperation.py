from PIL import Image, ImageDraw, ImageFont
import os
import copy


class ImageOperation:
    def __init__(self, image):
        self.image = image
        # Copy the variable rather than reference
        self.backup = copy.copy(self.image)

    @staticmethod
    def get_position(p):
        return {
            1: (10, 10),
            2: (40, 40),
            3: (50, 50),
            4: (100, 100),
            5: (140, 140),
        }.get(p, 1)

    def add_water_mark(self, text, position):
        pos = self.get_position(position)
        self.image = copy.copy(self.backup)
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype('arial.ttf', 36)
        draw.text(pos, text, font=font)
        # create the thumb again
        self.create_thumb()

    def resize_image(self, size):
        self.image.thumbnail(size)

    def create_thumb(self):
        size_480 = (480, 480)
        self.image.thumbnail(size_480)
        self.save_thumb()

    def save_thumb(self):
        if not os.path.exists('temp'):
            os.makedirs('temp')
        self.image.save("temp/thumb.png")


