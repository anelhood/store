import random
# 准备数据
bank = {} # 空的数据库
bank_name = "中国工商银行昌平回龙观支行"


def bank_addUser(account,username,password,country,province,street,door):
    # 是否已满
    if len(bank) > 100:
        return 3
    # 是否存在
    if username in bank:
        return 2
    # 正常开户
    bank[username] = {                           #1
        "account":account,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":1000,
        "bank_name":bank_name
    }
    return 1




# 用户的开户操作

def addUser():
    global bank
    username = input("请输入用户名：")
    password = input("请输入密码：")
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")

    account = random.randint(6214850200000001,6214850200000501)
    print(account)

    status = bank_addUser(account,username,password,country,province,street,door)
    if status == 3:
        print("对不起，该银行用户已满，请携带证件到其他银行办理!")
    elif status == 2:
        print("对不起，该用户已开户，请不要重复开户！别瞎弄！")
    elif status == 1:

        print("恭喜正常开户！以下是您的个人信息：")
        info = '''
            ------------个人信息------------
            用户名:%s
            银行卡号：%s
            密码：*****
            国籍：%s
            省份：%s
            街道：%s
            门牌号：%s
            余额：%s
            开户行名称：%s
        '''
        print(info % (username,account,country,province,street,door,bank[username]["money"],bank_name))

#取钱3.取钱（传入值：用户的账号，用户密码，取钱金额。返回值：整型值
# （0：正常，1：账号不存在，2：密码不对，3：钱不够）） a)业务逻辑：
# 先根据账号信息来查询该用户是否存在，若不存在，则返回代号1，
# 若存在，则继续判断密码是否正确，若不正确，则返回代号2。
# 若账号密码都正确，则继续判断当前用户的金额是否满足要取出的钱，若不满足，则返回代号3，
# 若满足，则将该用户的金额减去。
def deposit():
    global addUser
    for i in bank.keys():
        get_account = input("请输入银行卡号:")
        print("你输入的卡号：", get_account)
        get_password = input("请输入密码:")

        get_account = int(bank[i]["account"])

        if get_account == get_account and get_password == bank[i]["password"]:

            gets_money = int(input("请输入你的取款金额"))
            print(gets_money)

            if gets_money > bank[i]["money"]:
                print("卡内余额不足！无法取出")
            elif gets_money <= bank[i]["money"]:
                bank[i]["money"]  = bank[i]["money"]- gets_money
                print("取款成功","目前余额{}".format(bank[i]["money"]))
            else:
                print("输入非法！请正确输入！")

        elif get_account != get_account and get_password == bank[i]["password"]:
            print("用户输入错误！")
        elif get_account == get_account and get_password != bank[i]["password"]:
            print("用户密码输入错误！")

        else:
            print("该用户不存在")

def adddeposit():
    global addUser
    for i in bank.keys():
        get_account = input("请输入银行卡号:")
        print("你输入的卡号：", get_account)
        get_password = input("请输入密码:")

        get_account = int(bank[i]["account"])

        if get_account == get_account and get_password == bank[i]["password"]:

            gets_money = int(input("请输入你的存金额"))
            print(gets_money)

            if gets_money + bank[i]["money"] > 1000000000:
                print("卡内最多只能存取1000000000")

            elif gets_money <= 1000000000 - bank[i]["money"] :
                bank[i]["money"] = bank[i]["money"] + gets_money
                print("存款成功","目前余额{}".format(bank[i]["money"]))
            else:
                print("输入非法！请正确输入！")

        elif get_account != get_account and get_password == bank[i]["password"]:
            print("用户输入错误！")
        elif get_account == get_account and get_password != bank[i]["password"]:
            print("用户密码输入错误！")

        else:
            print("该用户不存在")


#查询5.查询账户功能（传入值：账号，账号密码，返回值：空）a)业务逻辑：
# 先根据账号判断用户库是否存在该用户，若不存在则打印提示信息：该用户不存在。
# 否则继续判断密码是否正确。若不正确则打印相对应的错误信息。
# 若账号和密码都正确，则将该用户的信息都打印出来，比如：
# 当前账号：xxxx,密码:xxxxxx,余额：xxxx元，用户居住地址：xxxxxxxxxxxxx，当前账户的开户行：xxxxxxxxxx.
def find_addUser():
    global addUser

    for i in bank.keys():
        get_account = input("请输入银行卡号:")
        print("你输入的卡号：",get_account)
        get_password = input("请输入密码:")

        get_account = int(bank[i]["account"])
        if get_account == get_account and get_password == bank[i]["password"]:

            print("登录成功！,下面显示该用户信息：")
            info = '''
                        ------------个人信息------------
                        用户名:%s
                        银行卡号：%s
                        密码：%s
                        国籍：%s
                        省份：%s
                        街道：%s
                        门牌号：%s
                        余额：%s
                        开户行名称：%s
                    '''
            print(info % (i,bank[i]["account"],bank[i]["password"],bank[i]["country"], bank[i]["province"], bank[i]["street"], bank[i]["door"], bank[i]["money"], bank_name))

        elif get_account !=  get_account  and get_password == bank[i]["password"]:
            print("用户输入错误！")
        elif get_account ==  get_account and get_password != bank[i]["password"]:
            print("用户密码输入错误！")

        else:
            print("该用户不存在")

# 转账
def transfer():
    number = input("请输入您要转账的账号：")
    uname = input("请输入您要转账的用户名：")
    money = int(input("请输转账金额："))
    for i in bank.keys():
        if i == uname:
            bank[i]['money'] = bank[i]['money'] + money
            print(uname,'用户的帐户余额为',bank[i]['money'])# 转账
def transfer():
    number = input("请输入您要转账的账号：")
    uname = input("请输入您要转账的用户名：")
    money = int(input("请输转账金额："))
    for i in bank.keys():
        if i == uname:
            bank[i]['money'] = bank[i]['money'] + money
            print(uname,'用户的帐户余额为',bank[i]['money'])
            break
            break


def welcome():
    print("----------------------------------------")
    print("-       中国工商银行账户管理系统V1.0    -")
    print("----------------------------------------")
    print("-                1.开户                -")
    print("-                2.取钱                -")
    print("-                3.存钱                -")
    print("-                4.转账                -")
    print("-                5.查询                -")
    print("-                6.Bye!                -")
    print("-------------------------------------- -")
# 入口程序
while True:
    welcome()
    # 输入用户的业务逻辑
    chose = input("亲输入您的业务：")
    if chose == "1":
        addUser()
    elif chose == "2":
        deposit()
    elif chose == "3":
        adddeposit()
    elif chose == "4":
        transfer()
    elif chose == "5":
        find_addUser()
    elif chose == "6":
        break
    else:
        print("输入非法，别瞎弄！重新输入!")







































