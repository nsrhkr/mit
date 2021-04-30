numSuccesses = 3
numFailures = 0

# successFailureRatio = numSuccesses/numFailures # numFailuresが0だとZeroDivisionError
# print('The success/failure ratio is', successFailureRatio)
# print('Now here')

try:
    successFailureRatio = numSuccesses/numFailures # numFailuresが0だとZeroDivisionError
    print('The success/failure ratio is', successFailureRatio)
    print('Now here')
except ZeroDivisionError:
    print('No failures, so the success/failure ratio is undefined.')
print('Now here')

def sumDigits(s):
    """
    sを文字列とする
    sの中の数字の合計を返す
    例えば、sが'a2b3c'ならば5を返す
    """
    numlist = []
    total = 0
    for n in s:
        try:
            total += int(n)
        except:
            pass
    print(total)
    return total

# sumDigits('a2b3c')

# 正しく例外を処理しているが冗長
# while True:
#     val = input('Enter an integer: ')
#     try:
#         val = int(val)
#         print('The square of the number you entered is', val**2)
#         break
#     except ValueError:
#         print(Val, 'is not integer')

# 一般化
def readVal(valType, requestMsg, errorMsg):
    while True:
        val = input(requestMsg + ' ')
        try:
            return(valType(val)) # 値を返す前にvalType型に変換する
        except ValueError:
            print(val, errorMsg)

# readVal(int, 'Enter an integer:', 'is not an integer ')

def findAnEven(L):
    """
    Lをint型の要素を持つリストとする
    Lに最初に含まれる偶数を返す
    Lが偶数を含まなければValueErrorを引き起こす
    """
    for n in L:
        if n%2 == 0:
            print(n)
            return n
    raise ValueError('Even numbers do not exist.')

findAnEven([1,7,6])
findAnEven([1,3,5])