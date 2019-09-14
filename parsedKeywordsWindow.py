from tkinter import *
from tkinter import Tk, ttk
import tkinter as tk
import PIL 
import urllib.request
import os
from bs4 import BeautifulSoup
OUTPUT_DIR="CollectedData"
import fetchFromWeb
import subprocess

# from PIL import ImageTk,Image


class ParesedKeywordsWindow(Frame):

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

        summaryLabel = Label(self, text="Summary")
        summaryLabel.grid(row=0, column=0, sticky=W+E)
        keywordsLabel = Label(self, text="keywords")
        keywordsLabel.grid(row=0, column=1, sticky=W+E)

        getSummary = Button(self, text="Get Summary", width=10,command=self.getSummaryFromFile)
        getSummary.grid(row=1, column=0, padx=5, pady=3, sticky=W+E)
        getKeywords = Button(self, text="Get Keywords", width=10,command=self.getKeywordsFromFile)
        getKeywords.grid(row=1, column=1, padx=5, pady=3, sticky=W+E)

        self.summaryData = Text(self,height=25, width=60)
        self.summaryData.grid(row=2, column=0, padx=5, pady=5, ipady=2, sticky=W+E)
        self.keywordsData = Text(self,height=25, width=60)
        self.keywordsData.grid(row=2, column=1, padx=5, pady=5, ipady=2, sticky=W+E)
        
        updateSummary = Button(self, text="Update Summary", width=10,command=self.updateSummaryInFile)
        updateSummary.grid(row=3, column=0, padx=5, pady=3, sticky=W+E)
        updateKeywords = Button(self, text="Update Keywords", width=10,command=self.updateKeywordsInFile)
        updateKeywords.grid(row=3, column=1, padx=5, pady=3, sticky=W+E)

        accuracyLabel= Label(self, text="Accuracy")
        accuracyLabel.grid(row=4, column=0, sticky=W+E)
        accuracyEntry= Entry(self, width=50)
        accuracyEntry.grid(row=4, column=1, sticky=W+E)

        closeWindow = Button(self, text="Close Window", width=10,command=self.onExit)
        closeWindow.grid(row=5, column=0, padx=5, pady=3, sticky=W+E)
        proceedToCollectData = Button(self, text="Proceed To Collect Data", width=10,command=self.proceedToResults)
        proceedToCollectData.grid(row=5, column=1, padx=5, pady=3, sticky=W+E)

    def proceedToResults(self):
        fetchFromWeb.fileAndData()
        subprocess.call(['invokeBrave.bat'])


    def onExit(self):
            self.quit()

    def getSummaryFromFile(self):
        with open(os.path.join(OUTPUT_DIR, 'summary.html'), 'r',encoding="utf8") as summaryfile:
            text=summaryfile.read()
            if(self.summaryData.get(INSERT)!=""):
                self.summaryData.delete('1.0',END)
            self.summaryData.insert(INSERT,text)

    def getKeywordsFromFile(self):
        with open('searchQueries.txt', 'r',encoding="utf8") as keywordsFile:
            text=keywordsFile.read()
            if(self.keywordsData.get(INSERT)!=""):
                self.keywordsData.delete('1.0',END)
            self.keywordsData.insert(INSERT,text)

    def updateSummaryInFile(self):
        with open(os.path.join(OUTPUT_DIR, 'summary.html'), 'w+',encoding="utf8") as summaryfile:
            text=self.summaryData.get('1.0',END)
            summaryfile.write(text)

    def updateKeywordsInFile(self):
        with open('searchQueries.txt', 'w+',encoding="utf8") as keywordsFile:
            text=self.keywordsData.get('1.0',END)
            # print(text)
            keywordsFile.write(text)
    
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

    app = ParesedKeywordsWindow(root)

    # img = ImageTk.PhotoImage(Image.open("logo.jpg"))
    # panel = Label(root, image = img)
    # panel.pack(side = "bottom", fill = "both", expand = "no")

    root.mainloop()

if __name__ == '__main__':
    main()
