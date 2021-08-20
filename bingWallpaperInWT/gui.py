import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import endpoint

image_url = ''
index = 0
tk_image = None

window = tk.Tk()
window.title('Show Bing Wallpaper')
window.geometry('800x600')
window.resizable(False, False)
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack(fill="both", expand=True)


def run_app():
    global image_url, index, canvas  # https://blog.csdn.net/u011304970/article/details/72820836
    # image
    index = 0
    image_url = endpoint.get_single_image_url(index)
    # tk_image = ImageTk.PhotoImage(file='res/left_arrow.png')
    canvas.create_image(400, 300, image=get_image())

    # button frame
    button_frame = tk.Frame(canvas)
    info = tk.Label(button_frame, width=8, height=2, text="Info", relief='groove').pack(side='left', fill='y')
    left_arrow = tk.PhotoImage(file='res/left_arrow.png')
    left_btn = tk.Button(button_frame, image=left_arrow, width=40, height=20,
                         command=previous).pack(side='left', fill='both')
    right_arrow = tk.PhotoImage(file='res/right_arrow.png')
    right_btn = tk.Button(button_frame, image=right_arrow, width=40, height=20,
                          command=after).pack(side='left', fill='both')
    down_arrow = tk.PhotoImage(file='res/download.png')
    download_btn = tk.Button(button_frame, image=down_arrow, width=40, height=20,
                             command=download).pack(side='left', fill='both')
    button_frame.pack(side='bottom', anchor='e', padx=100, pady=30)
    window.mainloop()


def get_image():
    global tk_image
    tk_image_stream = endpoint.get_single_image_stream(image_url)
    pil_image = Image.open(tk_image_stream)
    resize_image = pil_image.resize((800, 600))
    tk_image = ImageTk.PhotoImage(resize_image)
    return tk_image


def previous():
    global image_url, index, tk_image, canvas
    if index < 7:
        index += 1
        image_url = endpoint.get_single_image_url(index)
        tk_image = get_image()
        canvas.create_image(400, 300, image=get_image())


def after():
    global image_url, index, tk_image, canvas
    if index > 0:
        index -= 1
        image_url = endpoint.get_single_image_url(index)
        tk_image = get_image()
        canvas.create_image(400, 300, image=get_image())


def download():
    saving_path = tk.filedialog.asksaveasfile(filetypes=[('JPG', '.jpg'), ('PNG', '.png'), ('GIF', '.gif')],
                                              defaultextension='.jpg')
    if not saving_path:
        return
    tk_image_stream = endpoint.get_single_image_stream(image_url)
    pil_image = Image.open(tk_image_stream)
    pil_image.save(saving_path)


if __name__ == '__main__':
    run_app()
