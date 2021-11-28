from tkinter import *


class Display:

    def __init__(self, xy_size):

        self.watermark_window = Tk()
        self.watermark_window.title("Watermark Picture")
        self.watermark_window.geometry(f"{xy_size[0]}x{xy_size[1]}")
        self.canvas = Canvas(master=self.watermark_window, width=xy_size[0], height=xy_size[1])

    def show_watermark(self):

        watermark_pic = PhotoImage(master=self.canvas, file="watermark.gif")
        self.image_id = self.canvas.create_image(0, 0, image=watermark_pic, anchor=NW)
        self.canvas.pack()
        self.watermark_window.mainloop()

    def update_watermark(self):

        watermark = PhotoImage(master=self.canvas, file="watermark.gif")
        self.canvas.itemconfig(self.image_id, image=watermark)

    def destroy(self):

        self.watermark_window.destroy()


