import tkinter
import ctypes
#画面の部品，＝ウィジェット

ctypes.WinDLL("shcore").SetProcessDpiAwareness(True)
#にじみを消すおまじない

count = 0
def onclick():
    global count
    count += 1
    print("現在のクリック回数は",count,"回です")
    
root = tkinter.Tk()
btn = tkinter.Button(root, text = "OK", command = onclick)
btn.pack()

root.mainloop()

