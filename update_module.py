from PIL import Image, ImageFont, ImageDraw


def update(img_parameters):

    image = Image.open("copy.jpg")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", size=img_parameters[2])
    draw.text(xy=(img_parameters[0], img_parameters[1]), text=img_parameters[4], fill=img_parameters[3], font=font)
    image.save("watermark.jpg", format='JPEG', subsampling=0, quality=100)

