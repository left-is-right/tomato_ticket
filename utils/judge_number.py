import re


def judge_int(str):
    regInt = '^0$|^[1-9]\d*$'  # 不接受09这样的为整数

    patternInt = re.compile(regInt)
    if patternInt.search(str):
        return True
    if re.search(patternInt, str):
        return True
    if re.search(regInt, str):
        return True
    if str == "":
        return True
    else:
        return False


def judge_number(str):
    regInt = '^0$|^[1-9]\d*$'  # 不接受09这样的为整数
    regFloat = '^0\.\d+$|^[1-9]\d*\.\d+$'
    regIntOrFloat = regInt + '|' + regFloat  # 整数或小数

    patternIntOrFloat = re.compile(regIntOrFloat)
    if patternIntOrFloat.search(str):
        return True
    if re.search(patternIntOrFloat, str):
        return True
    if re.search(regIntOrFloat, str):
        return True
    if str == "":
        return True
    else:
        return False


if __name__ == '__main__':
    # num = "0.1"
    # print(judge_number(num))
    str = ""
    try:
        print(int(str))
    except ValueError as e:
        print(e)
        print(0)