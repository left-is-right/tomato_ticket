from time import sleep

list1 = ['(づ｡◕ᴗᴗ◕｡)づ', '(づ｡—ᴗᴗ—｡)づ', '(づ｡◕ᴗᴗ◕｡)づ', '(づ｡—ᴗᴗ—｡)づ', '(づ｡◕ᴗᴗ◕｡)づ',
         '(づ｡◕ᴗᴗ◕｡)づ', '(づ｡◕ᴗᴗ◕｡)づ', '(づ｡◕ᴗᴗ◕｡)づ', '(づ｡◕ᴗᴗ◕｡)づ', '(づ｡◕ᴗᴗ◕｡)づ']
# 第一个动态表情图的所有样式
list2 = ['u~(@_@)~*', 'u~(@_@)~*', 'u~(@_@)~*', 'u~(@_@)~*', 'u~(@_@)~*',
         'u~(@_@)~*', 'u~(—_—)~*', 'u~(@_@)~*', 'u~(—_—)~*', 'u~(@_@)~*']
# 第二个动态表情图的所有样式
while 1:
    for a, b in zip(list1, list2):
        print('\r %s %s ' % (a, b), end='')
        sleep(0.2)