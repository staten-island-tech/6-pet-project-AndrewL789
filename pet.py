
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
    def __init__(self, name, hapiness, weight, hunger, status, hpm):
        self.name = name
        self.__hapiness = hapiness
        self.__weight = weight
        self.__hunger = hunger
        self.__status = status
        self.__hpm = hpm
    def feed(self):
        found = False
        menu =[
            {
                'food' : 'cake',
                'hunger' : 20,
                'gains' : 20 
            },
            {
                'food' : 'nothing',
                'hunger' : -35,
                'gains' : 30 
            }
        ]
        print(menu)
        food = input('What to feed? :')
        for it in menu:
            if food.lower() == it['food'].lower():
                found = True
        if found == True:
            self.__hunger += it['hunger']
            self.__weight += it['gains']
            print(f"{self.name}'s hunger has now been changed by {it['hunger']}, {self.name} is now {self.__weight}lbs")
        else:
            print(f'{food} is not a valid option')
        if (self.__hunger>40) and (self.__hunger < 60):
            self.__status[1] = "fed"
            self.__hpm = 1
        elif self.__hunger >= 60:
            self.__status[1] = "fat"
            self.__hpm = 1.05
        elif self.__hunger <= 40:
            self.__status[1] = "malnourished"
            self.__hpm = 0.95
    def play(self):
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
            },
            {
                'act':'explode',
                'hpn':-9999999999999999999999999999999999999999999999999999999
            }
        ]
        print(playz)
        action = input('What to play? :')
        found = False
        for games in playz:
                    if action.lower() == games['act'].lower():
                        found = True
        if found == True:
            self.__hapiness += round(games['hpn'] * self.__hpm)
            print(f"{self.name}'s happiness has changed by {round(games['hpn'] * self.__hpm)}")
        if self.__hapiness < -1000:
            self.__status[0] = "depressed"
        else:
            self.status[0] = "happy"
    def status(self):
        print(f" {self.name}, {self.__hapiness}, {self.__hunger}, {self.__weight}lbs, {self.__status}, {self.__hpm}")
yang = petpetpet('Xiyang', 50, 80, 50, ['alive','fed'], 1.00)
done = False
while done == False:
    grah = input('interact :')
    if grah == "done":
        done = True
        yang.status()
    elif grah == "status":
        yang.status()
    elif grah == 'feed':
        yang.feed() 
    elif grah == 'play':
        yang.play()
    else:
        print('invalid action')
    

