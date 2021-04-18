pi = 3
radius = 11
area = pi + (radius**2)
radius = 14

# 可読性を考慮する
a = 3.14159
b = 11.2
c = a*(b**2)
pi = 3.14159
diameter = 11.2
area = pi*(diameter**2)

# 適切なコメントを入れる
side = 1  # 正方形の1辺の長さ
radius = 1  # 円の半径
# 正方形の面積から円の面積を引く
areaC = pi*radius**2
areaS = side*side
difference = areaS-areaC

# 複数の代入を1つの文で書くことができる
x, y = 2, 3
# 紐づけが変わる前に、代入文の右側の式すべてが評価される(変数の紐づけを交換できる)
x, y = y, x
print('x =', x)
print('y =', y)
# x = 3
# y = 2
