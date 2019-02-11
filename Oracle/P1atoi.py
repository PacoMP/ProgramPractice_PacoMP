def my_atoi(c='0'):
    c = list(c)
    value = 0
    #R2 se agrega la condición para determinar el signo
    sign = -1 if c[0] == '-' else 1


    for letter in c:
        if letter == '.' and c[c.index(letter)+1].isdigit():
            break
        if letter.isdigit():
            value = value*10
            value = value + int(letter)-int('0')
        elif letter != '-':
            return err("1")


    if (value*sign) not in range(-32768,32767+1):
        return err("2")
    else:
        return (value*sign)


def err(error):
    return {
        "1" : "Not a valid number",
        "2" : "Int Overflow",
    }[error]



###########################MAIN######################################
#4 byte -32,768 to 32,767
 #test1
assert my_atoi("5") == 5

 #test2
assert my_atoi("-2") == -2

#test3
print("Test 32767 : " , my_atoi("32767"))
#test4
print("Test -32767 : " , my_atoi("-32767"))
#test5
print("Test aksndhf : " , my_atoi("aksndhf"))
#test6
print("Test -32767.123 : " , my_atoi("-32767.123"))
#test7
print("Test 32768 : " , my_atoi("32768"))
#test8
print("Test -32768 : " , my_atoi("-32768"))
#test9
print("Test -32769 : " , my_atoi("-32769"))
#test10 asumiendo que cada numero menor a 0 debe ser 0
print("Test .97384732 : " , my_atoi(".97384732"))
#test11
print("Test -3de4 : " , my_atoi("-3de4"))
#test12
print("Test 354.de4 : " , my_atoi("354.de4"))


print("Finish.")
