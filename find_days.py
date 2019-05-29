# 用函数实现输入某年某月某日，判断这一天是这一年的第几天？闰年情况也考虑进去
runMonth = [1, 3, 5, 7, 8, 10, 12]


def isRunNian(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def isTrueDay(year, month, day):
    if month not in runMonth:
        if month != 2 and day >= 31:
            print("睡醒了吗？{}年{}月有{}天吗！！！".format(year, month, day))
            return False
        elif month == 2 and isRunNian(year) and day > 29:
            print("睡醒了吗？{}年{}月有{}天吗！！！".format(year, month, day))
            return False
        elif month == 2 and not isRunNian(year) and day > 28:
            print("睡醒了吗？{}年{}月有{}天吗！！！".format(year, month, day))
            return False
        else:
            return True
    else:
        if day > 31:
            print("睡醒了吗？{}年{}月有{}天吗！！！".format(year, month, day))
            return False
        else:
            return True


def calDays(year, month, day):
    sum = 0
    if isRunNian(year):
        if isTrueDay(year, month, day):
            for i in range(1, month + 1):
                if i in runMonth and i != month:
                    sum += 31
                elif i == 2 and i != month:
                    sum += 29
                else:
                    sum += day


    else:
        if isTrueDay(year, month, day):
            for i in range(1, month + 1):
                if i in runMonth and i != month:
                    sum += 31
                elif i == 2 and i != month:
                    sum += 28
                else:
                    sum += day

    return sum


year = ""
month = ""
date = ""
while not year.isdigit():
    year = input("请输入年份:")
while not month.isdigit():
    month = input("请输入月份:")
while not date.isdigit():
    date = input("请输入天数:")
day = calDays(int(year), int(month), int(date))
if day == 0:
    print("byebye^-^")
else:
    print("{}年{}月{}日是第{}天".format(year, month, date, day))
