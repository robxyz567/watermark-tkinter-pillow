from PIL import Image, ImageFont, ImageDraw


class Update:

    def __init__(self, parameters):

        image = Image.open("copy.jpg")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", size=parameters[2])
        draw.text((parameters[0], parameters[1]), text=parameters[4], fill=parameters[3], font=font)
        image.save("watermark.jpg", format='JPEG', subsampling=0, quality=100)

