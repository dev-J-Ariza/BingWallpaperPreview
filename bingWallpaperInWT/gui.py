import tkinter as tk
import endpoint


def run_app():
    window = tk.Tk()
    window.title('Show')
    window.geometry('800x600')
    today_image_url = endpoint.get_single_image_url(0)
    tk_image = endpoint.get_single_tk_image(today_image_url)
    label = tk.Label(window, image=tk_image, bg='black')
    window.mainloop()


if __name__ == '__main__':
    run_app()