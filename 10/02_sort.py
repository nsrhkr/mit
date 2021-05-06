# 選択ソート
# 計算時間はO(len(L)**2)
def selsoet(L):
    """
    Lを>を用いて比較できる要素からなるリストとする
    Lを昇順にソートする
    """
    suffixStart = 0
    while suffixStart != len(L):
        # サフィックスの各要素を見る
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                # 要素の位置を入れ替える
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1

# マージソート


def merge(left, right, compare):
    """
    leftとrightをソート済みのリストとし、
    compareを要素間の順序を定義する関数とする
    (left+right)と同じ要素からなり、
    compareに従いソートされた新たなリストを返す
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


def mergeSort(L, compare=lambda x, y: x < y):
    """
    Lをリストとし、compareとLの要素間の順序を定義する関数とする
    Lと同じ要素からなり、ソートされた新たなリストを返す
    """
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)

# Pythonにおけるソーティング（ティムソート）


def lastNameFirstName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[1] != arg2[1]:
        return arg1[1] < arg2[1]
    else:  # 姓が同じであれば、名によりソート
        return arg1[0] < arg2[0]


def firstNameLastName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[0] != arg2[0]:
        return arg1[0] < arg2[0]
    else:  # 名が同じであれば、姓によりソート
        return arg1[1] < arg2[1]


# L = ['Tom Brady', 'Eric Grimson', 'Gisele Bundchen']
# newL = mergeSort(L, lastNameFirstName)
# print('Sorted by last name =', newL)
# newL = mergeSort(L, firstNameLastName)
# print('Sorted by first name =', newL)

# Pythonのソート
L = [[1, 2, 3], (3, 2, 1, 0), 'abc']
print(sorted(L, key=len, reverse=True))
