def factl(n):
    """
    n > 0を整数と仮定
    n!を返す
    """
    result = 1
    while n > 1:
        result = result * n
        n -=1
    return result

def factR(n):
    """
    n > 0を整数と仮定
    n!を返す
    """
    if n == 1:
        return n
    else:
        return n*factR(n - 1)

# フィボナッチ再帰
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

def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))

def is Palindrome(s):
    """
    sを文字列と仮定
    sが回文ならTrueを返し、それ以外ならFalseを返す
    ただし、句読点、空白、大文字・小文字は無視する
    """

    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in s:
                if c in 'abcdefghijklmnopqrstuvwxyz':
                    letters = letters + c
        return letters

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

