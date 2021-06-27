import random

# 1.商品
shop = [
    ["机械革命", 15000],
    ["辣条", 2.5],
    ["辣条1", 5],
    ["辣条2", 10],
    ["电脑", 7000],
    ["HUAWEI watch", 1200],
    ["MAC PC", 13000],
    ["Iphone 54 plus", 45000],
    ["老干妈", 13],
    ["特仑苏", 58],
    ["金典", 60],
    ["游戏机", 20000],
    ["按摩椅", 4500],
    ["干吃面", 2],
    ["钓鱼竿", 200],
    ["大白毛绒玩具", 350],
]


#随机生成数字
def suiji():
    print("猜数字游戏开始！")
    data = random.randint(0, 20)
    i = 0
    com = 5000

    while i <= 10:
        print("目前金币：", com)
        num = input("请输入你的数字：")

        num = int(num)
        i = i + 1

        if num < data:
            com = com - 500
            print("小了", "目前金币剩余", com)
        elif num > data:
            com = com - 500
            print("大了", "目前金币剩余", com)
        else:
            com = com + 1000
            print("恭喜你，猜中了，您的猜的数字为：", num, "您猜了", i, "次了！""目前金币剩余", com)
            break
    print("你的次数已用尽！Bye！！！")



# 够买商品
def goumai():
    print("欢迎来到昌平商城")
    money = input("请输入您的钱包余额:")
    money = int(money)

    # 3.准备一个空的购物车
    mycart = []
    piao = random.randint(0,1)
    if piao == 0:
        print("恭喜你得到了电脑9折优惠劵！")
    else:
        print("恭喜你得到了辣条5折优惠劵！")

    # 买东西
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
            if chose > len(shop) - 1 or chose<0:
                print("您要的商品不存在！")
            else:
                # 看钱是否足够
                if  money >= shop[chose][1]:
                    mycart.append(shop[chose][0])
                    if piao == 1 and shop[chose][0].find("辣条")>= 0:
                        money -= shop[chose][1] * 0.5
                        print("购买成功，商品金额为:{}".format(shop[chose][1]), '您的当前余额剩余:', money, '元')

                    elif piao == 0 and shop[chose][0].find('电脑') >= 0:
                        money -= shop[chose][1] * 0.9
                        print("购买成功，商品金额为:{}".format(shop[chose][1]), '您的当前余额剩余:', money, '元')
                    else:
                        #剩余价钱
                        money -= shop[chose][1]
                        print("购买成功，商品金额为:{}".format(shop[chose][1]), '您的当前余额剩余:', money, '元')
                else:
                    print("对不起，穷鬼，余额不足，请到商城去购买！")
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


def tuichu():
    namelist = input("亲，你确认要回到界面（yes/no）?")
    namelist = namelist.lower()
    if namelist == "yes" or "YES":
        print("恭喜你成功退出")
    else:
        print("输入有误重新输入！")

while True:
    print('''
            \033[1;35m\t\t\t欢迎来到gogogo超市\033[0m
            \033[1;34m---------------------------------\033[0m
            \033[1;32m\t\t\t 1.猜数字游戏\033[0m
            \033[1;31m\t\t\t  2.够买商品 \033[0m
            \033[1;30m\t\t\t  3.退出系统 \033[0m
            \033[1;34m---------------------------------\033[0m
        ''')
    a = input("请输入你的选择：")
    # a = int(a)

    if a == "1":
        suiji()
        break
    elif a == "2":
        goumai()
        break
    elif a == "3":
        tuichu()
        break
    else:
        print("输入有误！正确输入你的选项：")



