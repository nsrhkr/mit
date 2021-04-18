# -*- coding: utf-8 -*-
# 奇数と偶数
if x%2 == 0:
    print('Even')
else:
    print('Odd')
print('Done with conditional')
# 複合論理式
if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')

# 3つの整数x, y, zの中で最も大きい奇数を表示する
# 奇数が無い場合は結果にその旨を記載
x = 1
y = 2
z = 3
if y < x and z < x:
    if x % 2 != 0:
        print('x is the largest odd number')
elif z < y:
    if y % 2 != 0:
        print('y is the largest odd number')
elif z % 2 != 0:
    print('z is the largest odd number')
else:
    print('Odd number does not exist.')
