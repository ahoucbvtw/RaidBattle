from tkinter import *
import tkinter.font as tkfont
import PIL.Image
import PIL.ImageTk
import sys, os


#建立按鈕實體物件
class button(object):
	def __init__(self, ButtonName, x, y, placewindow, goSub):
		self.ButtonName = ButtonName
		self.x = x
		self.y = y
		self.placewindow = placewindow
		self.goSub = goSub

		Font = tkfont.Font(family='新細明體', size=10, weight="bold")
		BN = Button(self.placewindow,text = self.ButtonName,font=Font)
		BN.config(bg= "skyblue")
		BN.config(width = 10,height = 1)
		BN.config(command = self.gotoSub)
		BN.place(x = self.x, y = self.y)

	def gotoSub(self):
		# print(self.ButtonName)
		self.goSub(self.ButtonName)


class Main(object):

# #建立按鈕實體物件(不知道為什麼抓取的ButtonName一直是最後創件的Button名字)

# 	def button(self, Name, place_x, place_y):
# 		self.ButtonName = Name
# 		self.x = place_x
# 		self.y = place_y

# 		Font = tkfont.Font(family='新細明體', size=10, weight="bold")
# 		BN = Button(self.window ,text = self.ButtonName,font=Font)
# 		BN.config(bg = "skyblue", activebackground = "#21b2ed")
# 		BN.config(activeforeground = "#f7f9fa")
# 		BN.config(width = 10,height = 1)
# 		BN.config(command = self.gotoSub)
# 		BN.place(x = self.x, y = self.y)

# 	def gotoSub(self):
# 		print(self.ButtonName)
# 		# self.goSub(self, MapName = self.ButtonName)


#建立主視窗
	def __init__(self, goSub):

		def resource_path(relative_path):
		#Get absolute path to resource, works for dev and for PyInstaller
			try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
				base_path = sys._MEIPASS
			except Exception:
				base_path = os.path.abspath(".")
			return os.path.join(base_path, relative_path)

		icon = resource_path("icon.ico")
		self.window = goSub
		self.window = Tk()
		self.window.iconbitmap(icon)
		self.window.title("RaidBattle") #視窗名稱
		self.window.config(background="#f0f0f0")#更該視窗背景顏色
		self.window.geometry("590x580+500+180") #視窗解析度 (x*y+視窗欲固定的畫面位置X+視窗欲固定的畫面位置Y)
		self.window.resizable(0,0)#不可以更改大⼩



#建立主視窗下的頁面

		hole = resource_path("hole.png")
		image = PIL.Image.open(hole)
		photo = PIL.ImageTk.PhotoImage(image)

		label = Label(self.window, image=photo)
		label.image = photo  # keep a reference!
		label.place(x = 15, y = 0)


		a = button("絢麗草原",165,537,self.window,goSub)
		b = button("沐光森林",72,522,self.window,goSub)
		c = button("牙牙湖之眼",6,462,self.window,goSub)
		d = button("牙牙湖東岸",8,418,self.window,goSub)
		e = button("瞭望塔舊址",40,386,self.window,goSub)
		f = button("牙牙湖西岸",55,358,self.window,goSub)
		g = button("沙塵窪地",167,150,self.window,goSub)
		h = button("巨人帽岩",140,124,self.window,goSub)
		i = button("逆鱗湖",155,25,self.window,goSub)
		j = button("拳關丘陵",435,28,self.window,goSub)
		k = button("巨人鏡池",486,73,self.window,goSub)
		l = button("巨石原野",440,185,self.window,goSub)
		m = button("橋間空地",400,256,self.window,goSub)
		n = button("機擎河岸",373,322,self.window,goSub)
		o = button("美納斯湖北岸",435,382,self.window,goSub)
		p = button("巨人凳岩",437,420,self.window,goSub)
		q = button("美納斯湖南岸",386,520,self.window,goSub)

		# a = self.button("絢麗草原",165,537)
		# b = self.button("沐光森林",72,522)
		# c = self.button("牙牙湖之眼",6,462)
		# d = self.button("牙牙湖東岸",8,418)
		# e = self.button("瞭望塔舊址",40,386)
		# f = self.button("牙牙湖西岸",55,358)
		# g = self.button("沙塵窪地",167,150)
		# h = self.button("巨人帽岩",140,124)
		# i = self.button("逆鱗湖",155,25)
		# j = self.button("拳關丘陵",435,28)
		# k = self.button("巨人鏡池",486,73)
		# l = self.button("巨石原野",440,185)
		# m = self.button("橋間空地",400,256)
		# n = self.button("機擎河岸",373,322)
		# o = self.button("美納斯湖北岸",435,382)
		# p = self.button("巨人凳岩",437,420)
		# q = self.button("美納斯湖南岸",386,520)

		self.window.mainloop()



if __name__ == '__main__':

	window = Tk()
	Main()
	window.mainloop() #確立視窗一直長在
