import tkinter as tk
from PIL import Image, ImageTk
import endpoint


def run_app():
    window = tk.Tk()
    window.title('Show Bing Wallpaper')
    window.geometry('800x600')

    # image
    today_image_url = endpoint.get_single_image_url(0)
    tk_image_stream = endpoint.get_single_image_stream(today_image_url)
    pil_image = Image.open(tk_image_stream)
    resize_image = pil_image.resize((800, 600))
    tk_image = ImageTk.PhotoImage(resize_image)
    # tk_image = ImageTk.PhotoImage(file='res/left_arrow.png')
    canvas = tk.Canvas(window, width=800, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(400, 300, image=tk_image)

    # button frame
    button_frame = tk.Frame(canvas)
    info = tk.Label(button_frame, width=8, height=2, text="Info", relief='groove').pack(side='left', fill='y')
    left_arrow = tk.PhotoImage(file='res/left_arrow.png')
    left_btn = tk.Button(button_frame, image=left_arrow, width=40, height=20).pack(side='left', fill='both')
    right_arrow = tk.PhotoImage(file='res/right_arrow.png')
    right_btn = tk.Button(button_frame, image=right_arrow, width=40, height=20).pack(side='left', fill='both')
    down_arrow = tk.PhotoImage(file='res/download.png')
    download_btn = tk.Button(button_frame, image=down_arrow, width=40, height=20).pack(side='left', fill='both')
    button_frame.pack(side='bottom', anchor='e', padx=100, pady=30)
    window.mainloop()


if __name__ == '__main__':
    run_app()
