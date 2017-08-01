#---------------------------------
#版本：4.0_b1
#此为第一个GUI版本，bug颇多，发现者请联系作者！
#仅限内部学习交流使用
#----------by Michael Ge----------


import random
import os
from tkinter import *

class win:
	def __init__(self):
		#脚本路径
		self.frp=os.path.split(os.path.realpath(__file__))[0]	
		#文件名列表	
		self.fpath=os.listdir(self.frp)
		self.fpath2=[]
		self.fpath3=[]
		#方法
		self.method=2
		#多选框关联列表
		self.filecheck=[]
		#密码
		self.key=0
		self.getname()
	
	#多选根窗口
	def getname(self):

		ck=Tk()
		ck.title("文件选择")
		Label(ck,text="选择所需的文件").grid(row=0,column=0,columnspan=2,padx=10,pady=10)
		i=1
		for fo in range(0,len(self.fpath)):
			self.filecheck.append(BooleanVar())
			l=Checkbutton(ck,text=self.fpath[fo],variable=self.filecheck[-1])
			l.grid(row=i,column=0,columnspan=2,sticky=W,padx=10)
			i=i+1
		Button(ck,text="txt加密",command=self.dis1).grid(row=i,column=0,sticky=W,padx=20,pady=10)
		Button(ck,text="其他加密",command=self.dis2).grid(row=i,column=1,sticky=E,padx=20,pady=10)
		Button(ck,text="txt解密",command=self.dis3).grid(row=i+1,column=0,sticky=W,padx=20,pady=10)
		Button(ck,text="其他解秘",command=self.dis4).grid(row=i+1,column=1,sticky=E,padx=20,pady=10)
		ck.mainloop()
	
	#方法设置
	def dis1(self):
		self.method=1
		self.dis()
	def dis2(self):
		self.method=2
		self.dis()
	def dis3(self):
		self.method=3
		self.dis()
	def dis4(self):
		self.method=4
		self.dis()
	
	#选中的文件名生成
	def dis(self):
		for p in range(0,len(self.fpath)):
			if self.filecheck[p].get()==1:
				self.fpath2.append(self.fpath[p])
				self.fpath3.append("处理的"+self.fpath[p])
		if self.method==1:
			self.txte()
		elif self.method==2:
			self.oe()
		elif self.method==3:
			self.txtd()
		elif self.method==4:
			self.oe()
			
	def txte(self):
		for n in range(0,len(self.fpath2)):
			name1=self.fpath2[n]
			name2=self.fpath3[n]
			fo=open(name1,"r")
			result=open(name2,"w")
			for line in fo.readlines():
				result.write(jiami(encode(line.strip("\n")))+"\n")
			fo.close()
			result.close()
		
		
	def txtd(self):
		for n in range(0,len(self.fpath2)):
			name1=self.fpath2[n]
			name2=self.fpath3[n]
			fo=open(name1,"r+")
			result=open(name2,"w")
			for line in fo.readlines():
			   a=(jiemi(line.strip("\n")))
			   result.write(decode(a)+"\n")
			fo.close()
			result.close()
		
	def oe(self):
		for n in range(0,len(self.fpath2)):
			images_path=self.fpath2[n]
			f = open(images_path,'rb')
			filedata = f.read()
			f.close()

			file_byte_array = bytearray(filedata)
			encrypt_file_byte_array = bytearray(0)
			for byte in file_byte_array:
				byte1=byte^100
				encrypt_file_byte_array.append(byte1)
			new_images_path=self.fpath3[n]
			f2 = open(new_images_path,'wb')
			f2.write(encrypt_file_byte_array)
			f2.close()
		
	def od(self):
		pass
		
		
def encode(s):
    return (' '.join([bin(ord(c)).replace('0b', '') for c in s]))

def decode(s):
    try:
        return (''.join([chr(i) for i in [int(b,2) for b in s.split(' ')]]))
    except:
        return(s)
    
def jiami(a):
    re=[]
    l1=["000","001","010","011","100","101","110","111"]
    for x in range(0,len(a),3):
        ob=a[x:x+3]
        if ob in l1:
            ran=random.randint(0,99)
            re.append(str(((l1.index(ob)+1)*100)+ran))
        else:
            ran=random.randint(0,1)
            if ran==0:
                re.append(ob.replace(" ","s"))
            else:
                re.append(ob.replace(" ","r"))
    return("".join(re))

def jiemi(mi):
    re=[]
    l1=["000","001","010","011","100","101","110","111"]
    for x in range(0,len(mi),3):
        ob=mi[x:x+3]
        if "s" in ob:
            re.append(ob.replace("s"," "))
        elif "r" in ob:
            re.append(ob.replace("r"," "))
        else:
            if len(ob)==3:
                re.append(l1[int(ob[0])-1])
            else:
                re.append(ob)
    return("".join(re))	

#从此开始	
if __name__ == "__main__":	
	w=win()

