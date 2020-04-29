from tkinter import *
from Main.Main import Main
from Main.Sub import Sub



class Application(Main, Sub):

	def __init__(self):
		self.window = Tk()
		self.goMain()

	def goMain(self):
		self.window.destroy()
		Main.__init__(self, goSub = self.goSub)


	def goSub(self, MapName):
		self.MapName = MapName
		self.window.destroy()
		Sub.__init__(self, goMain = self.goMain, MapName = self.MapName)



if __name__ == '__main__':
	Application()
