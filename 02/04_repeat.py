# 11と12ともに割り切れる正の整数を見つける
x = 1
while True:
    if x % 11 == 0 and x % 12 == 0:
        break
    x = x + 1
print(x, 'is divisible by 11 and 12')
