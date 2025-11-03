
# hero oactivity 
shop = [
    {
        'name':'sword',
        'price': 2.99
    }
]

class Hero:
    def __init__(self, name, money, status, inv):
        self.name = name
        self.__money = money
        self.inv = inv
        self.status = status
    def buy(self, item):
        for grah in shop:
            if item == grah['name']:
                self.inv.append(item)
                self.__money -= grah['price'] 
                print(self.inv) 
                print(self.__money)



#yangxi = Hero("YangXi", 3.99, ["Bone Cancer"], ["dirty used syringe"])
#print(yangxi.inv)
#yangxi.buy('sword')



#pet

""" class pet:
    def __init__(self, name, hapiness):
        self.name = name
        self.__hapiness = hapiness
    def play(self, thingy):
        self.__hapiness += 10
        print(f"{self.name}'s hapiness is now {self.__hapiness} after playing {thingy}")

 """
#yang = pet('Yang', 0) 
#yang.play("yang game") 




class petpetpet:
    def __init__(self, name, hapiness):
        self.name = name
        self.__hapiness = hapiness
    def play(self, action):
        p = 10
        self.__hapiness += p
        print(f"{self.name} is {action}, his joy has surged by {p}!!!!")
        
yang = petpetpet('XiYang', 50) 
yang.play("xiyang'in") 

