# # 総当たりを用いた平方根の近似
# x = 123456
# epsilon = 0.01
# step = epsilon**2
# numGuesses = 0
# ans = 0.0
# while abs(ans**2 - x) >= epsilon and ans*ans <= x:
#     ans += step
#     numGuesses += 1
# print('numGuesses =', numGuesses)
# if abs(ans**2 - x) >= epsilon:
#     print('Failed on square root of', x)
# else:
#     print(ans, 'is close to square root of', x)

# 立方根の近似解のための二分法
x = 24
epsilon = 0.01
numGuesses = 0
low = min(-1.0, x)
high = max(1.0, x)
print(low, high)
ans = (high + low)/2.0
i = 0
while abs(ans**2 - x) >= epsilon:
    i += 1
    print(i, 'low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)