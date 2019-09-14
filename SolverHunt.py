from tkinter import *
from tkinter import Tk, ttk
import tkinter as tk
import PIL 
import urllib.request
from bs4 import BeautifulSoup
from subprocess import call


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
        
        self.urlText = Entry(self, width=100)
        self.urlText.grid(row=0, column=1, padx=5, pady=5, ipady=2, sticky=W+E)

        
        self.textData = Text(self,height=25, width=100)
        self.textData.grid(row=1, column=1, padx=5, pady=5, ipady=2, sticky=W+E)
        urlFetch = Button(self, text="Get Data", width=10, command=self.getDataFromUrl)
        urlFetch.grid(row=0, column=2, padx=5, pady=3, sticky=W+E)
        deleteData = Button(self, text="Delete Data", width=10,command=self.deleteDataFromTextBox)
        deleteData.grid(row=1, column=2, padx=5, pady=3, sticky=W+E)
        
        okBtn = Button(self, text="OK", width=10, command=self.gotoNextWindow)
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

    def gotoNextWindow(self):
        call(["python", "generateSearchQueries.py"])
        call(["python", "parsedKeywordsWindow.py"])
        return

    def deleteDataFromTextBox(self):
        if(self.textData.get(INSERT)!=""):
            self.textData.delete('1.0',END)
    
    def demoPurpose(self):
        print("called demo")
        # with open("statement.html","rb") as url:
        raw = BeautifulSoup(open("wiki.html",encoding="utf8"))
        # print(raw.find_all('p'))
        soup=raw.find_all('p')
        htmlData=''
        for data in soup:
            htmlData=htmlData+data.text

        # soup=''.join(soup.stripped_strings)
        # soup = soup.replace("[","")
        # soup = soup.replace("]","")
        # soup = soup.replace(",","")
        soup =BeautifulSoup(htmlData)
        # print(url.read())
        # soup = BeautifulSoup(url.read())
        print("#######################")
        print(soup.get_text())
        # soup=soup.find("div", {"id": "problem"})
        for script in soup(["script", "style"]):
            script.extract()    # rip it out
        text=soup.get_text()
        print("#######################")
        print(text)
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        char_list = [text[j] for j in range(len(text)) if ord(text[j]) in range(65536)]
        htmltext=''
        for j in char_list:
            htmltext=htmltext+j
        self.textData.insert(INSERT,htmltext)

    def getDataFromUrl(self):
        urlString=self.urlText.get()
        if(self.textData.get(INSERT)!=""):
            self.textData.delete('1.0',END)
        with urllib.request.urlopen(urlString) as url:
            soup = BeautifulSoup(url.read(),"html5lib")
            f = open("data.html", "w",encoding="utf8")
            f.write(str(soup))
            f.close()
            for script in soup(["script", "style"]):
                script.extract()    # rip it out
            text=soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            char_list = [text[j] for j in range(len(text)) if ord(text[j]) in range(65536)]
            htmltext=''
            for j in char_list:
                htmltext=htmltext+j
            f = open("extractedText.txt", "w",encoding="utf8")
            f.write(str(htmltext))
            f.close()
        self.textData.insert(INSERT,htmltext)

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
