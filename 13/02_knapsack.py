
import random


class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name+', '+str(self.value)\
            + ', '+str(self.weight)+'>'
        return result


def maxVal(toConsider, avail):
    """
    toConsiderを品物のリスト、availを重さとする
    それらをパラメータとする0/1ナップサック問題の解である
    総価値と品物のリストからなるタプルを返す
    """
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        #右側の分岐のみを探索する
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #左側の分岐を探索する
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        #右側の分岐を探索する
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #よりよい分岐を選択
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result


def smallTest():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    val, taken = maxVal(Items, 5)
    for item in taken:
        print(item)
    print('Total value of items taken =', val)


def buildManyItems(numItems, maxVal, maxWeight):
    items = []
    for i in range(numItems):
        items.append(Item(str(i), random.randint(
            1, maxVal), random.randint(1, maxWeight)))
    return items


def bigTest(numItems):
    items = buildManyItems(numItems, 10, 10)
    val, taken = fastMaxVal(items, 40)
    print('Items Taken')
    for item in taken:
        print(item)
    print('Total value of items taken =', val)


def fastMaxVal(toConsider, avail, memo={}):
    """
    toConsiderを品物のリスト、availを重さ、
    memoは再帰呼出しによってのみ使われるとする
    それらをパラメータとする0/1ナップサック問題の解である
    総価値と品物のリストからなるタプルを返す
    """
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        #右側の分岐のみを探索する
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #左側の分岐を探索する
        withVal, withToTake =\
            fastMaxVal(toConsider[1:],
                        avail - nextItem.getWeight(), memo)
        withVal += nextItem.getValue()
        #右側の分岐を探索する
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
                                                avail, memo)
        #よりよい分岐を選択
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result

print(bigTest(40))