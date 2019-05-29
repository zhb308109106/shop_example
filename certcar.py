certcar = []
qianBao = 100
goodsList = [{"name": "肥宅快乐水", "price": 8, "remain": 16}, {"name": "哇哈哈", "price": 6, "remain": 2}]


# 打印菜单
def printMenus(type):
    if type == "identity":
        print("""***********欢迎来到彬彬超市，请选择操作:***********
1.店家
2.顾客
*********************************************************""")
    elif type == "dianjia":
        print("""***********请选择操作:************************
1.添加商品
2.查看列表
3.退出
*********************************************************""")
    elif type == "guke":
        print("""***********欢迎来到彬彬超市，请选择操作:***********
1.购买东西
2.充值
3.查看购物车
4.退出
*********************************************************""")
    else:
        print()


# 打印商品
def printGoodsList():
    print("***********商品列表***********")
    if len(goodsList) == 0:
        print("没有商品，请稍后！")
    else:
        for i in goodsList[::1]:
            print("ID:{},名称:{},价格:{},库存:{}".format(goodsList.index(i) + 1, i.get("name"), i.get("price"),
                                                   i.get("remain")))
        print("*" * 30)


# 添加商品
def addGoods():
    name = input("请输入商品名称:")
    isExist = False
    for i in goodsList[::1]:
        if i.get("name") == name:
            buyin = int(input("请输入进货数:"))
            i["remain"] += buyin
            isExist = True
    if not isExist:
        price = float(input("请输入价格:"))
        buyin = int(input("请输入进货数:"))
        good = {"name": name, "price": price, "remain": buyin}
        goodsList.append(good)


# 加入购物车
def addtocar(good, chooseNum):
    purchase = {"name": good["name"], "price": good["price"],
                "purchaseNum": chooseNum, "total": chooseNum * good["price"]}
    if len(certcar) > 0:
        for i in certcar[::1]:
            if i.get("name") == purchase.get("name"):
                i["purchaseNum"] += purchase.get("purchaseNum")
                i["total"] += purchase.get("total")
                break
            else:
                certcar.append(purchase)
    else:
        certcar.append(purchase)
    goods = ""
    for index, j in enumerate(certcar):
        goods += "商品名称:{} 单价:{} 购买数量:{} 总价:{}\n".format(j.get("name"),
                                                        j.get("price"),
                                                        j.get("purchaseNum"),
                                                        j.get("total"))
    print("购物车有:\n{}".format(goods))


# 立即购买
def paynow(qianBao, chooseNum):
    goods = []
    good["remain"] -= chooseNum
    if good["remain"] == 0:
        goodsList.remove(good)
    qianBao -= chooseNum * good["price"]
    purchase = {"name": good["name"], "price": good["price"],
                "purchaseNum": chooseNum, "total": chooseNum * good["price"]}
    goods.append(purchase)
    str3 = ""
    for index, j in enumerate(goods):
        str3 += "商品名称:{} 单价:{} 购买数量:{} 总价:{}\n".format(j.get("name"),
                                                       j.get("price"),
                                                       j.get("purchaseNum"),
                                                       j.get("total"))

    print("上帝啊，你此次购买了:\n{}钱包余额为{},欢迎下次光临！".format(str3, qianBao))
    return qianBao


while True:
    printMenus("identity")
    identity = input("请选择身份:")
    if identity == "1":
        while True:
            printMenus("dianjia")
            busaction = input("请选择操作（1-3）")
            if busaction == "1":
                addGoods()
            elif busaction == "2":
                printGoodsList()
            elif busaction == "3":
                break
            else:
                print("请输入正确的操作项（eg:1）")
    elif identity == "2":
        while True:
            printMenus("guke")
            action = input("请选择操作（eg:1）:")
            if action == "1":
                printGoodsList()
                chooseOption = input("请选择商品ID(1-{}):".format(len(goodsList)))
                # 判断所选择的商品ID是否正确
                while not chooseOption.isdigit():
                    chooseOption = input("请输入正确的ID:")
                chooseOption = int(chooseOption)

                while chooseOption > len(goodsList):
                    chooseOption = input("请输入正确的ID:")
                    while not chooseOption.isdigit():
                        chooseOption = input("请输入正确的ID:")
                    chooseOption = int(chooseOption)

                if chooseOption <= len(goodsList):
                    good = goodsList[chooseOption - 1]
                    while True:
                        chooseNum = int(input("请输入购买数量(1-{}):".format(good.get("remain"))))
                        if chooseNum > good.get("remain"):
                            print("上帝啊，你购买的数量超过了超市的库存！！！")
                        else:
                            if good.get("price") * chooseNum > qianBao:
                                print("钱包余额不足了，请充值！！！")
                                break
                            else:
                                flag = True
                                while flag:
                                    isAddCart = input("加入购物车【Y/N】,选N的话立即购买:")
                                    if isAddCart.upper() == 'Y':
                                        addtocar(good, chooseNum)
                                        flag = False
                                    elif isAddCart.upper() == 'N':
                                        qianBao = paynow(qianBao, chooseNum)
                                        flag = False
                                    else:
                                        print("请输入正确的操作项（Y/N）!")
                            break

            elif action == "2":
                pay = int(input("请输入充值金额:"))
                qianBao += pay
                print("充值成功，你钱包余额为{}".format(qianBao))
            elif action == "3":
                goods = ""
                for index, j in enumerate(certcar):
                    goods += "商品名称:{} 单价:{} 购买数量:{} 总价:{}\n".format(j.get("name"),
                                                                    j.get("price"),
                                                                    j.get("purchaseNum"),
                                                                    j.get("total"))
                if goods == "":
                    print("购物车空荡荡，go shopping 吧!")
                else:
                    print("购物车有:\n{}".format(goods))
                    isJieZhang = input("是否结账【Y/N】,选N的退出:")
                    if isJieZhang.upper() == 'Y':
                        type1 = []
                        type2 = []
                        numList = {}
                        totalSum = 0
                        for i in goodsList:
                            type1.append(i.get("name"))
                        for j in certcar:
                            type2.append(j.get("name"))
                            numList[j.get("name")] = j.get("purchaseNum")
                            totalSum += j.get("total")
                        if totalSum > qianBao:
                            print("钱包余额不足了，请充值！！！")
                        else:

                            # 购物车、商店都有了
                            type4 = set(type2).intersection(set(type1))

                            # 购物车有但是商店没有了
                            type3 = set(type2).difference(set(type1))

                            for i in type4:
                                for good in goodsList[::1]:
                                    if good.get("name") == i:
                                        if good["remain"] >= numList[i]:
                                            qianBao = paynow(qianBao, numList[i])
                                        else:
                                            type3.add(good["name"])

                        str4 = ""
                        for i in type3:
                            str4 += "缺货:\n{}".format(i)
                        if len(type3) > 0:
                            print("{}\n！".format(str4, qianBao))
                        pass

                    elif isJieZhang.upper() == 'N':
                        pass

                    else:
                        print("请输入正确的操作项（Y/N）!")

            elif action == "4":
                break
                print("谢谢惠顾，欢迎再次光临!")
            else:
                print("请输入正确的操作项（eg:1）")
    else:
        print("请输入正确的操作项（eg:1）")
