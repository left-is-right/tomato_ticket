import decimal

list1 = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖', '拾']
list2 = ['元', '拾', '佰', '仟', '万']


def num_2_cn(money):
    money_cn = ''
    try :
        for i in range(0, len(money)):
            if int(money[i]) != 0:
                money_cn += list1[int(money[i])] + list2[len(money) - i - 1]
            else:
                if money_cn[-1] != "零":
                    money_cn += "零"

        if money_cn[-1] == "零":
            money_cn = money_cn[0:len(money_cn) - 1] + "圆整"
        else:
            money_cn = money_cn + "整"
    except ValueError:
        print(money)
        return ""

    return money_cn


if __name__ == '__main__':

    money = str(int(input("请输入金额:")))  # 预防输入0开头的数字

    print(num_2_cn(money))

