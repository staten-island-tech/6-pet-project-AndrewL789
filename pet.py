
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
        playz = [
            {
                'act':'running',
                'hpn': 25
            },
            {
                'act': 'walking',
                'hpn': 5
            },
            {
                'act' :"yang'n",
                'hpn': 30
            },
            {
                'act':'getting wasted',
                'hpn' : -30
            },
            {
                'act':'singing',
                'hpn': -50
            }
        ]
        c1 = False
        for goo in playz:
            if action.lower() == goo['act'].lower():
                c1 = True
        if c1 == False:
            print('invalid action')
        elif c1 == True:
            for grah in playz:
                if action.lower() == grah['act'].lower():
                    self.__hapiness += grah['hpn']
                    if grah['hpn'] > 0:
                        boom = 'increased'
                    elif grah['hpn'] < 0:
                        boom = 'decreased'

                    print(f"{self.name} is {action.lower()}, his happiness has {boom} by {grah['hpn']}!! ")
    def status(self):
        print(f"{self.name}'s current happiness is {self.__hapiness}!!")
yang = petpetpet('Xiyang', 50)
done = False
while done == False:
    grah = input('interact :')
    if grah == "done":
        done = True
        yang.status()
    elif grah == "status":
        yang.status()
    elif grah !="done":
        yang.play(grah)
    

