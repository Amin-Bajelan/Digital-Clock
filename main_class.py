import datetime
import tkinter as tk

Color_background = '#686D76'
Color_text = '#DC5F00'
Btn_color = '#EEEEEE'


def return_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M:%S %p")


def close_app():
    window.destroy()


def change_time():
    clock_text = str(return_time())
    label.config(text=clock_text)
    label.after(1000, change_time)


window = tk.Tk()
window.title('Digital Clock')
window.config(width=350, height=170, background=Color_background)
window.maxsize(350, 170)
window.minsize(350, 170)

label = tk.Label(window, text='')
label.config(width=20, font=('Digital-7 MonoItalic',23), fg=Color_text, bg=Color_background, highlightthickness=0)
label.place(x=27, y=60)
change_time()

btn_break = tk.Button(window, text=" Close ", command=close_app, font=('Arial', 10), fg=Color_text, bg=Btn_color,
                      highlightthickness=0)
btn_break.place(x=150, y=110)

window.mainloop()
