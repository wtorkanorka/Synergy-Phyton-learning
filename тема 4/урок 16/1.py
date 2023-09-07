# 1 https://github.com/wtorkanorka/Synergy-Phyton-learning.git
class Cassa(object):
    money = 0

    def __init__(self, m):
        self.money = m

    def top_up(self, x):
        self.money += x

    def count_1000(self):
        return self.money // 1000

    def take_away(self, x):
        if self.money >= x:
            self.money -= x
        else:
            print("не хватает в кассе денег")
