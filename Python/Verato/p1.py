list = list(range(2000,3201))
#print(list)
for number in list:
    if (number%17 ==0):
        if number%5 is not 0:
            print(number,end = ',')
