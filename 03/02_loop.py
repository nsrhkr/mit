# x = 4
# for i in range(0, x):
#     print(i)

# x = 4
# for i in range(0, x):  # rangeの引数は最初だけ評価される
#     print(i)
#     x = 5

# x = 4
# for j in range(x): # rangeの引数は最初だけ評価される
#     for i in range(x): # 内側のforループのrange関数は内側のfor文に処理が移るたびに評価される
#         print(i)
#         x = 2

# # 完全立方に対する立方根を求める
# x = int(input('Enter an integer: '))
# for ans in range(0, abs(x)+1):
#     if ans**3 >= abs(x):
#         print('ans', ans)
#         break
# if ans**3 != abs(x):
#     print(x, 'is not a perfect cube')
# else:
#     if x < 0:
#         ans = -ans
#     print('Cube root of', x, 'is', ans)

total = 0
for c in '12345678':
    total = total + int(c)
print(total)

# 少数を含む文字列をコンマで分けた上、これを表示する
s = '1.23,2.4,3.123'
total = 0
for f in s.split(','):
    total = total + float(f)
print(total)