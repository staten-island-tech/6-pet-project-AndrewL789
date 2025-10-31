""" 
# hero oactivity 
class Hero:
    def __init__(self, name, money, status, inv):
        self.name = name
        self.money = money
        self.inv = inv
        self.status = status
    def buy(self, item):
        (self.inv).append(item)
        print(self.inv)

yangxi = Hero("YangXi", 3.99, ["Bone Cancer"], ["dirty used syringe"])
print(yangxi.inv)
yangxi.buy('air') """



#pet

class pet:
    def __init__(self, name, hapiness):
        self.name = name
        self.__hapiness = hapiness
    def play(self, thingy):
        self.__hapiness += 10
        print(f'hapiness is now {self.__hapiness} after playing {thingy}')


yang = pet('Yang', 0) 
yang.play("yang game") 