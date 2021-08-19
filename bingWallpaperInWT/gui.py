import tkinter as tk
from PIL import Image, ImageTk
import endpoint


def run_app():
    window = tk.Tk()
    window.title('Show')
    window.geometry('800x600')
    today_image_url = endpoint.get_single_image_url(0)
    tk_image_stream = endpoint.get_single_image_stream(today_image_url)
    pil_image = Image.open(tk_image_stream)
    resize_image = pil_image.resize((800, 600))
    tk_image = ImageTk.PhotoImage(resize_image)
    label = tk.Label(window, image=tk_image, bg='black')
    label.pack()
    window.mainloop()


if __name__ == '__main__':
    run_app()
