from tkinter import *
from DataSet.MachineDataSet import MachineDataSet


class View(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.img1 = PhotoImage(file='giphy.gif')
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='搜尋', font=('', 24)).grid(row=1, stick=W, pady=10)
        Label(self, text='').grid(row=2,stick=W,pady=10)