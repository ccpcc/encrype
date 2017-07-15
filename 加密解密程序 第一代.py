import random
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

while True:
    st=input("输入您所需的模式：")
    if st=="encode":
        name1=input("输入您要加密的文件路径：")
        name2=input("输入您要保存到的文件路径：")
        fo=open(name1,"r+")
        result=open(name2,"w")
        for line in fo.readlines():
           result.write(jiami(encode(line.strip("\n")))+"\n")
        fo.close()
        result.close()
        print("谢谢使用！")
        break
    elif st=="decode":
        name1=input("输入您要解密的文件路径：")
        name2=input("输入您要保存到的文件路径：")
        fo=open(name1,"r+")
        result=open(name2,"w")
        for line in fo.readlines():
           a=(jiemi(line.strip("\n")))
           result.write(decode(a)+"\n")
        fo.close()
        result.close()
        print("谢谢使用！")
        break
    elif st=="help":
        print("加密请输入 encode")
        print("解密请输入 decode")
    
    else:
        print("无效值，可以输入 help 来获取帮助")
