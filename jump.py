import tkinter
import ctypes
from PIL import ImageTk
import os
os.chdir(os.path.dirname(__file__))
#画面の部品，＝ウィジェット

ctypes.WinDLL("shcore").SetProcessDpiAwareness(True)
#にじみを消すおまじない

def onclick(e):
    global flag
    flag = not flag
    if flag == True:
        chara["image"] = idle_img
    else:
        chara["image"] = jump_img

flag = True
    
root = tkinter.Tk()
root.geometry("700x500")
root.title("Firstmariorun")
root.bind("<space>", onclick)
root.pack_propagate(False)
jump_img = ImageTk.PhotoImage(file="jumpmortion.jpg")
idle_img = ImageTk.PhotoImage(file="mario_run.jpg")
chara = tkinter.Label(root, image=idle_img)
chara.pack()
root.mainloop()