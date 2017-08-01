import os
import sys
import random
print("__encrypt__.py")

#随机生成密匙random.randint(1, 255)
encrypt_key = random.randint(1, 255)
#加密过的标示，两个字节
have_encrypt_first_flag = 0x12
have_encrypt_second_flag = 0x34
have_encrypt_third_flag = 0x56

#images_path是需要加密的图片的绝对路径
def encrypt(images_path):
    f = open(images_path, 'rb')
    filedata = f.read()
    filesize = f.tell()
    f.close()

    file_byte_array = bytearray(filedata)

    #判断是否加密过
    if(have_encrypt_first_flag == file_byte_array[0]
        and have_encrypt_second_flag == file_byte_array[1]
        and have_encrypt_third_flag == file_byte_array[2]):
            print('this png has encrypt before!')
    else:
        encrypt_file_byte_array = bytearray(0)
        encrypt_file_byte_array.append(have_encrypt_first_flag)
        encrypt_file_byte_array.append(have_encrypt_second_flag)
        encrypt_file_byte_array.append(have_encrypt_third_flag)
        encrypt_file_byte_array.append(encrypt_key)

        for byte in file_byte_array:
            encrypt_bype = byte ^ encrypt_key
            encrypt_file_byte_array.append(encrypt_bype)

        workdir = os.path.split(images_path)[0]
        new_images_path=input("结果")

        f2 = open(new_images_path,'wb')
        f2.write(encrypt_file_byte_array)
        f2.close()
		
p=input("图片路径：")
encrypt(p)
