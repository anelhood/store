import random
data = random.randint(0,10)
coin = 5000
i = 1
while i <= 5:
    num = input("请输入您要猜的数字：")
    num = int(num)
    if num > data:
        coin = coin - 500
        print("大了！")
        print("你猜了",i,"次了","目前金币",coin)
    elif num < data:
        coin = coin - 500
        print("小了！")
        print("你猜了",i,"次了","目前金币",coin)
    else:
        coin = coin + 1000
        print("恭喜您，猜中数字，本次幸运数字为：",num,"你猜了",i,"次了呀","剩余金币", coin )
        break # 跳出循环
    i = i + 1
print ("你的次数已用完，请重新开始")