import random

r = random.randint(1,1000)

while(1):
    inputNumber = int(input("请输入一个数字："))
    if inputNumber % 2 == 0:
        print(inputNumber, "是双数")
    else:
        print(inputNumber, "是单数")