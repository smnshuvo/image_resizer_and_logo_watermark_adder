from PIL import Image, ImageDraw, ImageFont


class ImageOperation:
    def __init__(self, image):
        self.image = image

    def add_water_mark(self, text):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype('arial.ttf', 36)
        draw.text((10, 10), text, font=font)

    def resize_image(self, size):
        self.image.thumbnail(size)
