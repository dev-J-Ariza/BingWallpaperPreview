import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from bingWallpaperInWT import endpoint
from functools import lru_cache

image_url = ''
index = 0
info = ""
info_txt = None
tk_image = None

window = tk.Tk()
window.title('Show Bing Wallpaper')
window.geometry('900x600')
window.resizable(False, False)
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack(fill="both", expand=True)


def run_app():
    global image_url, index, canvas, info, info_txt  # https://blog.csdn.net/u011304970/article/details/72820836
    # image
    index = 0
    image_url, info = endpoint.get_single_image_url_info(index)
    # tk_image = ImageTk.PhotoImage(file='res/left_arrow.png')
    canvas.create_image(450, 300, image=get_image(image_url))

    # button frame
    button_frame = tk.Frame(canvas)
    info_txt = tk.Label(button_frame, width=8, height=2, text="Info", relief='groove')
    info_txt.bind('<Enter>', show_info)  # mouse in
    info_txt.bind('<Leave>', hide_info)  # mouse out
    info_txt.pack(side='left', fill='y')
    image_path = os.path.join(os.path.dirname(__file__), 'res', 'left_arrow.png')
    left_arrow = tk.PhotoImage(file=image_path)
    left_btn = tk.Button(button_frame, image=left_arrow, width=40, height=20,
                         command=previous).pack(side='left', fill='both')
    image_path = os.path.join(os.path.dirname(__file__), 'res', 'right_arrow.png')
    right_arrow = tk.PhotoImage(file=image_path)
    right_btn = tk.Button(button_frame, image=right_arrow, width=40, height=20,
                          command=after).pack(side='left', fill='both')
    image_path = os.path.join(os.path.dirname(__file__), 'res', 'download.png')
    down_arrow = tk.PhotoImage(file=image_path)
    download_btn = tk.Button(button_frame, image=down_arrow, width=40, height=20,
                             command=download).pack(side='left', fill='both')
    button_frame.pack(side='bottom', anchor='e', padx=100, pady=30)
    window.mainloop()


@lru_cache(maxsize=12, typed=False)
def get_image(url):
    global tk_image
    tk_image_stream = endpoint.get_single_image_stream(url)
    pil_image = Image.open(tk_image_stream)
    resize_image = pil_image.resize((900, 600))
    tk_image = ImageTk.PhotoImage(resize_image)
    return tk_image


def previous():
    global image_url, index, tk_image, canvas
    if index < 7:
        index += 1
        global info
        image_url, info = endpoint.get_single_image_url_info(index)
        canvas.create_image(450, 300, image=get_image(image_url))


def after():
    global image_url, index, tk_image, canvas
    if index > 0:
        index -= 1
        global info
        image_url, info = endpoint.get_single_image_url_info(index)
        canvas.create_image(450, 300, image=get_image(image_url))


def show_info(event):
    info_txt.config(text=info, width=75)


def hide_info(event):
    info_txt.config(text="Info", width=8)


def download():
    saving_path = tk.filedialog.asksaveasfile(filetypes=[('JPG', '.jpg'), ('PNG', '.png'), ('GIF', '.gif')],
                                              defaultextension='.jpg')
    if not saving_path:
        return
    tk_image_stream = endpoint.get_single_image_stream(image_url)
    pil_image = Image.open(tk_image_stream)
    pil_image.save(saving_path)
