class IntSet(object):
    """
    IntSetは整数の集合
    集合はint肩の要素からなるリストself.valsによってあらわされる。
    int型の要素はそれぞれ、リストself.valsにちょうど一度だけ現れる
    """


    def __init__(self):
        """
        整数の空集合を生成する
        """
        self.vals = []
    
    
    def insert(self, e):
        """
        eをint型とし、eをselfに挿入する
        """
        if not e in self.vals:
            self.vals.append(e)
    
    
    def member(self, e):
        """
        int型eがselfにあればTrueを、なければFalseを返す
        """
        return e in self.vals
    
    
    def remove(self, e):
        """
        eをint型とし、eをselfから削除する
        """
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    
    
    def getMembers(self):
        """
        selfが含む要素を持つリストを返す
        要素の順序に関しては何も約束できない
        """
        return self.vals[:]
    
    
    def __str__(self):
        """
        selfの文字列表現を返す
        """
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'  # -1としたのは最後のカンマを除くため


import datetime

class Person(object):

    def __init__(self, name):
        """
        「人間」を生成する
        """
        self.name = name
        try:
            lastBlank = name.index(' ')
            self.lastName = name[lastBlask + 1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        """
        selfの名前（フルネーム）を返す
        """
        return self.name

    def getLastName(self):
        """
        selfの姓を返す
        """
        return self.lastName

    def setBirthday(self, birthdate):
        """
        birthdateをdatetime.date型とする
        selfの生年月日をbirtdateと設定する
        """
        self.birthday = birthdate

    def getAge(self):
        """
        selfの現在の年齢を日単位で返す
        """
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """
        selfの名前がotherの名前と比べて
        アルファベット順で前ならばTrueを、そうでなければFalseを返す
        比較は、姓について行われるが、
        姓が同じであれば名前（フルネーム）が比較される
        """
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """
        selfの名前（フルネーム）を返す
        """
        return self.name

# me = Person('Michael Guttag')
# him = Person('Barack Hussein Obama')
# her = Person('Madonnna')
# print(him.getLastName())
# him.setBirthday(datetime.date(1961, 8, 4))
# her.setBirthday(datetime.date(1958, 8, 16))
# print(him.getName(), 'is', him.getAge(), 'days old')

