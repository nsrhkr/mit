def findPaiment(loan, r, m):
    """
    loanとrをfloat型とし、mをint型とする
    mヶ月で返済する場合の毎月の返済額を返す
    """
    return loan*((r*(1+r)**m)/((1+r)**m-1))


class Mortgage(object):
    """
    異なる種類の住宅ローンを構築するための抽象クラス
    """

    def __init__(self, loan, annRate, nonths):
        """
        loanとannRateをfloat型とし、monthsをint型とする
        借入額loan、返済月数months、年利annRateの
        住宅ローンを新たに生成する
        """
        self.loan = loan
        self.rate = annRate/12
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = findPayment(loan, self.rate, month)
        self.legend = None  # 住宅ローンの種類（サブクラスで用いる）

    def makePayment(self):
        """
        返済を行う
        """
        self.paid.append(self.payment)
        resuction = self.payment - self.outstanding[-1]*self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)

    def getTotalPaid(self):
        """
        これまでに支払った総額を返す
        """
        return sum(self.paid)

    def ___str___(self):
        return self.legend


class Fixed(Mortgage):
    def __init__(self, loan, r, month):
        Mortgage.__init__(self.loan, r, months)
        self.legend = 'Fixed, ', + str(round(r*100, 2)) + '%'


class FixedWithPts(Mortgage):
    def __init__(self, loan, r, month, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = ptsself.paid = [loan*(pts/100)]
        self.legend = 'Fixed, ' + str(round(r*100, 2)) + '%, '\
            + str(pts)+' points'

