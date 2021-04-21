# # 関数の利用
# def maxVal(x, y):
#     if x > y:
#         return x
#     else:
#         return y

# def isIn(x, y):
#     if (x in y) or (y in x) :
#         return True
#     else:
#         False

# print(isIn('hoge', 'hogehoge'))

def printName(firstName, lastName, reverse=False):
    if reverse:
        print(lastName + ', '+ firstName)
    else:
        print(firstName, lastName)

printName(lastName='Hanako', firstName='Yamada', reverse=True)
# キーワード引数のあとにキーワード引数でないものを書くとエラー
# printName('Hanako', firstName='Yamada', True)