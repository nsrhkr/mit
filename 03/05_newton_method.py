# 平方根を求めるためのニュートン-ラフソン法
# x**2 -24 = 0で伍さがepsilon以下になるxを求める
epsilon = 0.01
k = 24.0
guess = k/2.0
i = 0
while abs(guess*guess-k)>=epsilon:
    guess = (((guess**2) - k)/(2*guess))
    i += 1
    print(i, 'guess =', guess)
print('Squeare root of', k, 'is about', guess)