# 誤りのある回文チェックプログラム
def isPal(x):
    """
    リストxが回文ならばTrue、そうでなければFalseを返す
    """
    temp = x[:] # 修正
    temp.reverse()
    print(temp, x) # プログラムの中ほどで値を出力してみて問題を切り分けていく
    if temp==x:
        return True
    else:
        return False

def silly(n):
    """
    nを正のint型とする
    ユーザからn個の入力を受ける
    入力文字列が回文であれば'Yes'を、
    そうでなければ'No'を出力する
    """
    result = [] # 修正
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    print(result) # プログラムの中ほどで値を出力してみて問題を切り分けていく
    if isPal(result):
        print('Yes')
    else:
        print('No')

silly(2)