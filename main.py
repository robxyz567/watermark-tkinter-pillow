from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def checking():

    watermark_image = image_copy.copy()
    image_size = watermark_image.size

    text = text_entry.get()
    x = int(x_entry.get())
    x = x / 100 * image_size[0]
    y = int(y_entry.get())
    y = (1 - y / 100) * image_size[1]
    font_size = int(font_size_entry.get())
    font_color = font_color_entry.get()
    if font_color == 'white':
        font_color = (255, 255, 255)
    elif font_color == 'black':
        font_color = (0, 0, 0)

    draw = ImageDraw.Draw(watermark_image)
    font = ImageFont.truetype("arial.ttf", font_size)
    draw.text((x, y), text, font_color, font=font)

    watermark_image.save("watermark.gif")
    watermark_image.show()


def quit():
    window.destroy()


def upload():

    global image_copy

    filepath = filedialog.askopenfilename()
    image = Image.open(filepath)

    image_copy = image.copy()
    image_copy.save("copy.gif")
    image_copy.show()


window = Tk()
window.title("Watermark")
window.config(padx=50, pady=50)

#Entries
text_entry = Entry(width=35)
text_entry.grid(row=2, column=1, columnspan=2)
text_entry.focus()

x_entry = Entry(width=35)
x_entry.grid(row=3, column=1, columnspan=2)

y_entry = Entry(width=35)
y_entry.grid(row=4, column=1, columnspan=2)

font_size_entry = Entry(width=35)
font_size_entry.grid(row=5, column=1, columnspan=2)

font_color_entry = Entry(width=35)
font_color_entry.grid(row=6, column=1, columnspan=2)

#Buttons
upload_button = Button(text='Open', width=29, command=upload)
upload_button.grid(row=1, column=1, columnspan=2)

checking_button = Button(text="Check", width=14, command=checking)
checking_button.grid(row=7, column=1)

save_button = Button(text="Save and quit", width=14, command=quit)
save_button.grid(row=7, column=2)

#Labels
logo_label = Label(text="IMAGE WATERMARK APP", font=('Arial', 12, "bold"))
logo_label.grid(row=0, column=1, columnspan=2)

text_label = Label(text="Font text: ")
text_label.grid(row=2, column=0)

x_label = Label(text="Font x pos.: ")
x_label.grid(row=3, column=0)

y_label = Label(text="Font y pos.: ")
y_label.grid(row=4, column=0)

font_size_label = Label(text="Font size: ")
font_size_label.grid(row=5, column=0)

font_color_label = Label(text="Font color (black or white): ")
font_color_label.grid(row=6, column=0)


window.mainloop()
