from tkinter import *
from files_module import File
from display_module import Display
from update_module import Update
import os


def color_chose(color):

    global font_color
    font_color = color


def checking():

    watermark_parameters = []
    image_size = file.image_size()

    text = text_entry.get()
    x = int(x_scale.get())
    x = x / 100 * image_size[0]
    y = int(y_scale.get())
    y = (1 - y / 100) * image_size[1]
    font_size = int(font_size_scale.get())

    watermark_parameters.append(x)
    watermark_parameters.append(y)
    watermark_parameters.append(font_size)
    try:
        watermark_parameters.append(font_color)
    except NameError:
        watermark_parameters.append('black')
    watermark_parameters.append(text)

    Update(watermark_parameters)
    file.image_convert()
    watermark.update_watermark()
    watermark.show_watermark()


def quiting():

    window.destroy()
    watermark.destroy()
    os.remove('copy.jpg')


def upload():

    global file, watermark
    file = File()
    watermark = Display(file.image_size())
    watermark.show_watermark()


window = Tk()
window.title("Watermark Menu")
window.config(padx=50, pady=50)

#Entries
text_entry = Entry(width=43)
text_entry.grid(row=2, column=1, columnspan=8)
text_entry.focus()

#Scales
x_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
x_scale.grid(row=3, column=1, columnspan=4)
y_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
y_scale.grid(row=4, column=1, columnspan=4)
font_size_scale = Scale(from_=0, to=100, orient=HORIZONTAL)
font_size_scale.grid(row=5, column=1, columnspan=4)

#Color_Buttons
black_button = Button(width=3, bg='black', command=lambda: color_chose('black'))
black_button.grid(row=6, column=1)
white_button = Button(width=3, bg='white', command=lambda: color_chose('white'))
white_button.grid(row=6, column=2)
red_button = Button(width=3, bg='red', command=lambda: color_chose('red'))
red_button.grid(row=6, column=3)
orange_button = Button(width=3, bg='orange', command=lambda: color_chose('orange'))
orange_button.grid(row=6, column=4)
yellow_button = Button(width=3, bg='yellow', command=lambda: color_chose('yellow'))
yellow_button.grid(row=6, column=5)
green_button = Button(width=3, bg='green', command=lambda: color_chose('green'))
green_button.grid(row=6, column=6)
blue_button = Button(width=3, bg='blue', command=lambda: color_chose('blue'))
blue_button.grid(row=6, column=7)
purple_button = Button(width=3, bg='purple', command=lambda: color_chose('purple'))
purple_button.grid(row=6, column=8)

#Other_Buttons
upload_button = Button(text='Select a file to upload', width=36, command=upload)
upload_button.grid(row=1, column=1, columnspan=8)
checking_button = Button(text="Check", width=17, command=checking)
checking_button.grid(row=7, column=1, columnspan=4)
save_button = Button(text="Save&quit", width=17, command=quiting)
save_button.grid(row=7, column=5, columnspan=4)

#Labels
logo_label = Label(text="IMAGE WATERMARK APP", font=('Arial', 12, "bold"))
logo_label.grid(row=0, column=1, columnspan=8)
text_label = Label(text="Font text: ")
text_label.grid(row=2, column=0)
x_label = Label(text="Font x pos.: ")
x_label.grid(row=3, column=0)
y_label = Label(text="Font y pos.: ")
y_label.grid(row=4, column=0)
font_size_label = Label(text="Font size: ")
font_size_label.grid(row=5, column=0)
font_color_label = Label(text="Font color: ")
font_color_label.grid(row=6, column=0)


window.mainloop()
