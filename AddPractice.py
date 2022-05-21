import random

a = random.randint(1,100)
b = random.randint(1,100)

print("请计算：",a,"+",b,"=",end="")

bCorrect = False

count = 0

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
