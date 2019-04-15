from tkinter import *
from tkinter import Tk, ttk
import tkinter as tk
import PIL 
import urllib.request
from bs4 import BeautifulSoup

# from PIL import ImageTk,Image


class SolverHuntMain(Frame):

    def __init__(self, parent):
       
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Solver Hunt")
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.centreWindow()
        self.pack(fill=BOTH, expand=1)
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=fileMenu)

        firstNameLabel = Label(self, text=" Url:")
        firstNameLabel.grid(row=0, column=0, sticky=W+E)
        lastNameLabel = Label(self, text="   Text Data:  ")
        lastNameLabel.grid(row=1, column=0, sticky=W+E)
        
        
        
        okBtn = Button(self, text="OK", width=10)
        okBtn.grid(row=4, column=1, padx=5, pady=3, sticky=W+E)
        closeBtn = Button(self, text="Close", width=10, command=self.onExit)
        closeBtn.grid(row=5, column=1, padx=5, pady=3, sticky=W+E)
    
    def centreWindow(self):
        w = 1000
        h = 600
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def onExit(self):
        self.quit()

def main():
    root = Tk()

    root.resizable(width=TRUE, height=TRUE)
    # resizable

    app = SolverHuntMain(root)

    # img = ImageTk.PhotoImage(Image.open("logo.jpg"))
    # panel = Label(root, image = img)
    # panel.pack(side = "bottom", fill = "both", expand = "no")

    root.mainloop()

if __name__ == '__main__':
    main()
