
def shuzi():
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

shop = [
    ["机械革命",15000],
    ["HUAWEI watch",1200],
    ["MAC PC",13000],
    ["Iphone 54 plus",45000],
    ["辣条",2.5],
    ["老干妈",13],
    ["糖果",10],
    ["oppo",5000],
    ["衣服",1000],
    ["鞋子",1500],
    ["牙刷", 15],
    ["牙膏", 15],
    ["电饭煲", 1500],
    ["炸弹", 150000],
    ["c4", 150000],
    ["火鸡面", 150000],
]

def shangdian():
    import random
    money = input("请输入您的钱包余额:")
    money = int(money)
    mycart = []
    piao = random.randint(0,len(shop)-1)
    print("你的本次商品折扣序号：",shop[piao])
    you = shop[piao][1]
    print("您的享受时%.2f" %you,"优惠")
    # while True:# 永远循环
    # 展示商品
    if money >= 0:
        for index, value in enumerate(shop):  # 枚举，将角标和商品整体都打印
            print(index, "  ", value)
        # 请输入您要的商品
        chose = input("请输入您要的商品：")

        # 看是否存在
        if chose.isdigit():  # 是否能被看成数字：
            chose = int(chose)
            # 看商品是否存在
            if chose > len(shop) - 1 or chose < 0:
                print("您要的商品不存在！")
            else:
                # 看钱是否足够
                if money < shop[chose][1]:
                    print("对不起，穷鬼，余额不足，请到商城去购买！")
                else:
                    if chose == piao:
                        mycart.append(shop[chose])
                        aa = piao * shop[chose][1]
                        money -= aa
                        print("您还剩%.2f" % money)
                    else:
                        mycart.append(shop[chose])
                        money -= shop[chose][1]
                        print("您还剩%.2f" % money)

        elif chose == 'q' or chose == 'Q':
            print("欢迎下次光临！")
        else:
            print("对不起，您的输入商品不存在！别瞎弄!")
    else:
        print("输入的钱不能为负数!")
        # 打印小票
    print("下面是您的购物小条，请拿好：")
    for index, value in enumerate(mycart):
        print(index, "   ", value)
    print("您的钱包还剩：￥", money)



while True:
    print('''
        \033[1;35m\t\t\t欢迎来到系统\033[0m
        \033[1;35m----------------------------\033[0m
        \033[1;34m        1.猜数字          \033[0m
        \033[1;33m        2.买东西          \033[0m
        \033[1;32m        3.退出系统         \033[0m
        \033[1;35m-----------------------------\033[0m
    ''')
    a = input("请输入你的选择：")
    a = int(a)
    if a == 1:
        shuzi()
        break
    elif  a == 2:
        shangdian()
        break

    else:
        namelist = input("是否要退出系统：yes/no?")
        namelist = namelist.lower()
        if namelist == "yes":
            print("退出系统成功")
            break
        else:
            print("请正确输入！")



