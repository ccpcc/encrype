def op(images_path):
    f = open(images_path,'rb')
    filedata = f.read()
    f.close()

    file_byte_array = bytearray(filedata)
    encrypt_file_byte_array = bytearray(0)
    for byte in file_byte_array:
        byte1=encode(byte)
        encrypt_file_byte_array.append(byte1)
    new_images_path=input("结果")
    f2 = open(new_images_path,'wb')
    f2.write(encrypt_file_byte_array)
    f2.close()

def encode(a):
    try:
        a=a^23
        return(a)
    except:
        return(a)
    
p=input("路径")
op(p)
