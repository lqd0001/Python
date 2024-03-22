try:
    menu = int(input("Choose an option: \n 1.Decimal to binary \n 2.Binary to decimal\n Option : "))
    if menu <1 or menu >2:
        raise ValueError
    if menu == 1:
        dec = int(input("Input your decimal number:\n Decimal: "))
        print("Binary:{}".format(bin(dec)[2:]))
    elif menu == 2:
        binary = input("Input your binary number:\n Binary: ")
        print("Decimal: {}".format(int(binary,2)))  #int()函数参数有两个,第一个x是字符串（字符串只有数字）,第二个是进制,默认是10,可以是2-36中的整数。
except ValueError:
    print("please choose a valid option")
