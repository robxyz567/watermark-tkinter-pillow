from tkinter import filedialog
from PIL import Image


class File:

    def __init__(self):

        filepath = filedialog.askopenfilename()
        image = Image.open(filepath)
        self.image_copy = image.copy()

        self.x_size = self.image_copy.size[0]
        self.y_size = self.image_copy.size[1]

        self.image_copy.save("copy.jpg", format='JPEG', subsampling=0, quality=100)
        self.image_copy.save("watermark.gif", format='GIF', quality=100)

    def image_size(self):

        return self.x_size, self.y_size

    def image_convert(self):

        Image.open("watermark.jpg").convert('RGB').save('watermark.gif')