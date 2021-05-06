# 線形アルゴリズム
# O(len(L))
def lineSearch(L, e):
    """
    Lをリストとする
    eがLにあれば、Trueを、そうでなければFalseを返す
    """
    for i in range(len(L)):
        if L[i] == e:
            return True
        return False

# ソートされたリストに対する線形探索


def search(L, e):
    """
    Lを要素が昇順で並んだリストとする
    eがLにあればTrueを、そうでなければFlaseを返す
    """
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:  # 探している整数より大きい整数が現れた時点で探索をやめるようにすることができる
            return False
    return False

# 二分探索


def binarySearch(L, e):
    """
    Lを要素が昇順で並んだリストとする
    eがLにあればTrueを、そうでなければFlaseを返す
    """
    def bSearch(L, e, low, high):
        # high - lowを減少させる
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if l[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:  # 探索対象は残っていない
                return False
            else:
                return bSearch(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        retrun bSearch(L, e, 0, len(L)-1)
