# tuple
# t1 = ()
# t2 = (1, 'two', 3)
# print(t1)
# print(t2)

# t1 = (1, 'two', 3)
# t2 = (t1, 3)
# print(t2)
# print((t1 + t2))
# print((t1 + t2)[3])
# print((t1 + t2)[2:5])

# def intersect(t1, t2):
#     """
#     t1とt2はタプルであると仮定する
#     t1とt2両方に入っている要素を含むタプルを返す
#     """
#     result = ()
#     for e in t1:
#         if e in t2:
#             result += (e,)
#     return result

# print(intersect(t1, t2))

# list
# Techs = ['MIT', 'Caltech']
# Lvys = ['Harvard', 'Yale', 'Brown']

# Univs = [Techs, Lvys]
# Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
# print('Univs =', Univs)
# print('Univs1 =', Univs1)
# print(Univs == Univs1)
# print(id(Univs) == id(Univs1))
# print('Id of Univs =', id(Univs))
# print('Id of Univs1 =', id(Univs1))

# aliasing
# Techs.append('RPI')
# print('Univs =', Univs)
# print('Univs1 =', Univs1)

# extendやappendは副作用を持つ
# +演算子は持たない