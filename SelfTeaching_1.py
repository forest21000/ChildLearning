# print("你好")

import random

# r = random.randint(1,1000)
#
# while(1):
#     inputNumber = int(input("请输入一个数字："))
#     if inputNumber % 2 == 0:
#         print(inputNumber, "是双数")
#     else:
#         print(inputNumber, "是单数")


a = random.randint(1,100)
b = random.randint(1,100)

print("请计算：",a,"+",b,"=",end="")

bCorrect = False

count = 8

while(count<100):
    addRes = int(input())
    if addRes == a + b:
        bCorrect = True
        print("恭喜您！答对了第",count+1,"题!:)")

        a = random.randint(1, 100)
        b = random.randint(1, 100)

        print("请计算：",a, "+", b, "=",end="")

        count = count + 1

    else:
        print("不好意思，您算错了，请重新计算")

print("恭喜您答对了100题")
