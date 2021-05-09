import matplotlib.pyplot as pylab
import random


class Location (object):
    def __init__(self, x, y):
        """
        xとyは不動小数点数
        """
        self.x, self.y = x, y

    def move(self, deltaX, deltaY):
        """
        deltaXとdeltaYは浮動小数点数
        """
        return Location(self.x+deltaX, self.y+deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox, oy = other.x, other.y
        xDist, yDist = self.x-ox, self.y-oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x)+', '+str(self.y)+'>'


class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        # Lcationクラスのmoveメソッドを用いて、新しい位置情報を得る
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


class Drunk(object):
    def __init__(self, name=None):
        """
        nameは文字列とする
        """
        self.name = name

    def ___str(self):
        if self != None:
            return self.name
        return 'Anonymous'


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)
        return random.choice(stepChoices)


def walk(f, d, numSteps):
    """
    f：Field クラスのオブジェクト
    d：Drunk クラスのオブジェクト
    numSteps：0 以上の整数
    dをnumSteps回移動し、酔歩の初期位置と最終位置との差を出力する。
    """
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))


def simWalks(numSteps, numTrials, dClass):
    """
    numSteps：0 以上の整数
    numTrials：正の整数
    dClass：Drunk のサブクラス
    numSteps 回移動する酔歩を，numTrials 回シミュレートする。
    各実験の初期位置と最終位置との差をリストにして出力する。
    """
    Homer = dClass()
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances


def drunkTest(walkLengths, numTrials, dClass):
    """
    walkLengths：0 以上の整数のシークエンス
    numTrials：正の整数
    dClass：Drunk のサブクラス
    walkLengths の各要素を酔歩の移動回数として、numTrials 回の酔歩を
    シミュレートする simWalks を実行し、結果を出力する。
    """
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print(' Mean =', round(sum(distances)/len(distances), 4))
        print(' Max =', max(distances), 'Min =', min(distances))


# 偏りつき
class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [
            (0.0, 1.0), (0.0, -2.0), (1.0, 0.0), (-1.0, 0.0)
        ]
        return random.choice(stepChoices)


class EWDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


def simAll(drunkKinds, walkLengths, numTrials):
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrials, dClass)


# simAll((UsualDrunk, ColdDrunk, EWDrunk), (100, 1000), 10)


# 出力を見やすくする
class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result


def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of', numSteps, 'steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances


def simAll1(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'r:', 'k-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of', dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle, label=dClass.__name__)
    pylab.title('Mean Distance from Origin ('
                + str(numTrials) + ' trials)')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc='best')
    pylab.semilogx()
    pylab.semilogy()

simAll1((UsualDrunk, ColdDrunk, EWDrunk),(10,100,1000,10000,100000), 100)
