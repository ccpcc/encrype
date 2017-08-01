import random
import os
class mima:
    def __init__(self):
        pass
            
    def check(self):
        if os.path.exists(r"D:\\政治局加密系统缓存"):
             return("0")
        else:
            return("1")
         
    def conf(self):
        print("欢迎来到配置模式，输入000为不设置")
        if self.check()=="1":
            os.makedirs("D:\\政治局加密系统缓存")
        r1=input("源文件路径")
        r2=input("目标文件路径")
        fi1=open("D:\\政治局加密系统缓存\\config1.txt","w")
        try:
            fi1.write(r1)
        finally:
            fi1.close()
        fi2=open("D:\\政治局加密系统缓存\\config2.txt","w")
        try:
            fi2.write(r2)
        finally:
            fi2.close()
        print("配置完成！")
            
    def encode(self,s):
        return (' '.join([bin(ord(c)).replace('0b', '') for c in s]))

    def decode(self,s):
        try:
            return (''.join([chr(i) for i in [int(b,2) for b in s.split(' ')]]))
        except:
            return(s)
        
    def jiami(self,a):
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

    def jiemi(self,mi):
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

while True:
    st=input("输入您所需的模式：")
    ob=mima()
    if st=="encode":
        if ob.check()=="1":
            name1=input("输入您要加密的文件路径：")
            name2=input("输入您要保存到的文件路径：")
        else:
            fi1=open("D:\\政治局加密系统缓存\\config1.txt","r")
            fi2=open("D:\\政治局加密系统缓存\\config2.txt","r")
            name1=fi1.read()
            name1=name1.strip("\n")
            if name1=="000":
                name1=input("输入您要加密的文件路径：")
            name2=fi2.read()
            name2=name2.strip("\n")
            if name2=="000":
                name2=input("输入您要保存到的文件路径：")
            fi1.close()
            fi2.close()
        fo=open(name1,"r+")
        result=open(name2,"w")
        for line in fo.readlines():
           result.write(ob.jiami(ob.encode(line.strip("\n")))+"\n")
        fo.close()
        result.close()
        print("谢谢使用！")
        break
    elif st=="decode":
        if ob.check()=="1":
            name1=input("输入您要解密的文件路径：")
            name2=input("输入您要保存到的文件路径：")
        else:
            fi1=open("D:\\政治局加密系统缓存\\config1.txt","r")
            fi2=open("D:\\政治局加密系统缓存\\config2.txt","r")
            name1=fi1.read()
            name1=name1.strip("\n")
            if name1=="000":
                name1=input("输入您要解密的文件路径：")
            name2=fi2.read()
            name2=name2.strip("\n")
            if name2=="000":
                name2=input("输入您要保存到的文件路径：")
            fi1.close()
            fi2.close()
        fo=open(name1,"r+")
        result=open(name2,"w")
        for line in fo.readlines():
           a=(ob.jiemi(line.strip("\n")))
           result.write(ob.decode(a)+"\n")
        fo.close()
        result.close()
        print("谢谢使用！")
        break
    elif st=="help":
        print("加密请输入 encode")
        print("解密请输入 decode")
        print("配置请输入 config")
    elif st=="config":
        ob.conf()
    
    else:
        print("无效值，可以输入 help 来获取帮助")
