def factR(n):
    """
    n > 0を整数と仮定
    n!を返す
    """
    if n == 1:
        return n
    else:
        return n*factR(n - 1)

def fib(n):
    """
    n > 0を整数と仮定
    n番目のフィボナッチ数を返す
    """
    i = 0
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# 高階プログラミング
# def applyToEach(L, f):
#     """
#     リストLの各要素eを関数F(e)に置き換えてLを更新する
#     """
#     for i in range(len(L)):
#         L[i] = f(L[i])

# L = [1, -2, 3.33]
# print('L =', L)
# print('Apply ads to each element of L')
# applyToEach(L, abs)
# print('L =', L)
# print('Apply int to each element of L')
# applyToEach(L, int)
# print('L =', L)
# print('Apply factorial to each element of L')
# applyToEach(L, factR)
# print('L =', L)
# print('Apply Fibonnaci to each element of L')
# applyToEach(L, fib)
# print('L =', L)

# 高階関数map
# for i in map(fib, [2, 6, 4]):
#     print(i)

# L1 = [1, 28, 36]
# L2 =[2, 57, 9]
# for i in map(min, L1, L2): # mapの第一引数はn個の引数を取る関数にすることができる
#     print(i)

# 高階関数引数としてよく使われるラムダ式
L = []
for i in map(lambda x, y: x**y, [1, 2, 3, 4], [3, 2, 1, 0]):
    L.append(i)
print(L)