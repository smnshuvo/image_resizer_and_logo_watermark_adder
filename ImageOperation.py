from PIL import Image, ImageDraw, ImageFont
import os

class ImageOperation:
    def __init__(self, image):
        self.image = image

    def add_water_mark(self, text):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype('arial.ttf', 36)
        draw.text((10, 10), text, font=font)

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
