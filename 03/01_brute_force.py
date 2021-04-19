import math
# # 完全立方の平方根を求める
# x = int(input('Enter an integert: '))
# ans = 0
# while ans**3 < abs(x):
#     ans = ans + 1
# if ans**3 != abs(x):
#     print(x, 'is not a perfect cube')
# else:
#     if x < 0:
#         ans = -ans
#     print('Cube root of', x, 'is ', ans)

# maxVal = int(input('Enter a postive integer: '))
# i = 0
# while i < maxVal:
#     i = i + 1
# print(i)

# 二つの整数 root, pwrを表示する
# 0<pwr<6, root**pwrは入力した整数値と等しい
num = int(input('Enter a postive integer: '))
pwr = 1
root = 0
while pwr < 6:
    root = num / pwr
    if root == math.floor(root) and num == root**pwr:
        print('root:',int(root), 'pwr:', pwr)
        break
    elif pwr == 5:
        print('The integers root and pwe do not exist')
    pwr += 1