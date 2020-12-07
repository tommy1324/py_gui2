from View import *
from tkinter import *


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('500x400')
        self.createPage()

    def createPage(self):
        self.page = View(self.root)
        self.page.pack()