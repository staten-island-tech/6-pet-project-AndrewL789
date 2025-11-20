
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
    def __init__(self, name, hapiness, weight, hunger, status, hpm, hp, maxhp):
        self.name = name
        self.__hapiness = hapiness
        self.__weight = weight
        self.__ideal = weight
        self.__hunger = hunger
        self.__status = status
        self.__hpm = hpm
        self.__hp = hp 
        self.__maxhp = maxhp
        self.__maxhpog = maxhp
    def feed(self):
        found = False
        menu =[
            {
                'food' : 'cake', 'hunger' : 20,'heal' : 3.5 
            },
            {
                'food' : 'nothing', 'hunger' : -35,'heal' : 0
            },
            {
                'food' : "nothing'er", 'hunger' : -1000000, 'heal' :0
            },
            {
                'food' : 'granola bar', 'hunger' : 5,'heal' : 5
            },
            {
                'food' : 'tree', 'hunger' : 1,'heal' : -10
            },
            {
                'food' : 'cement', 'hunger' : 0,'heal' : 1
            },
            {
                'food':'mason', 'hunger':2000000,'heal': 1000000
            }
        ]
        for food in menu:
            print(f"{food['food']} : hunger; {food['hunger']} : heal; {food['heal']} ")
        food = input('What to feed? :')
        for it in menu:
            if food.lower() == it['food'].lower():
                found = True
                if found == True:
                    self.__hunger += it['hunger']
                    return(f"{self.name} has devoured {it['food']}, {self.name}'s hunger has now been changed by {it['hunger']}, {self.name} is now {self.__weight}lbs")
        if found == False:
            return(f'{food} is not a valid option')
    def play(self):
        playz = [
            {
                'act':'running', 'hpn': 25, 'dmg': 0
            },
            {
                'act': 'walking', 'hpn': 5, 'dmg' : 0
            },
            {
                'act' :"yang'n", 'hpn': 30, 'dmg' : 0 
            },
            {
                'act':'getting wasted', 'hpn' : -30, 'dmg':0
            },
            {
                'act':'singing', 'hpn': -5, 'dmg': 5
            },
            {
                'act':'instant depression', 'hpn': -500, 'dmg':0
            },
            {
                'act':'instant joy' , 'hpn' : 500, 'dmg':0
            },
            {
                'act':'explode', 'hpn':-10000000, 'dmg':330
            }
        ]
        for play in playz:
            print(f"{play['act']} : hapiness ; {play['hpn']}")
        action = input('What to play? :')
        found = False
        for games in playz:
            if action.lower() == games['act'].lower():
                found = True
                self.__hapiness += games['hpn'] * self.__hpm
                self.__hp -= games['dmg']
                return(f"{self.name}'s happiness has changed by {games['hpn'] * self.__hpm}")
        if found == False:
            return(f"{action} is not a valid action")
    def status(self):
        return(f" {self.name}, happiness:{self.__hapiness}, hunger:{self.__hunger}/100, {self.__weight}lbs, {self.__status}, {self.__hpm}x, {self.__hp}/{self.__maxhp}hp")
    def begin(self):
            while self.__status[2] == 'alive':
                grah = input('interact :')
                if grah.lower() == "kill":
                    self.__hp = 0
                    self.__hapiness = 0
                elif grah.lower() == "status":
                    print(self.status())
                elif grah.lower() == 'feed':
                    print(self.feed()) 
                elif grah.lower() == 'play':
                    print(self.play())
                else:
                    print('invalid action')



                while self.__hunger >=100:
                        self.__hunger-=100
                        self.__weight += 1 
                while self.__hunger < 0:
                    self.__hunger += 100
                    self.__weight -= 1


    #turn these into functions cuz this is horrifying <---- 
                if (self.__weight >= self.__ideal * 0.95) and (self.__weight <= self.__ideal * 1.05):
                    self.__status[1] = "fed"
                    self.__hpm = 1
                elif (self.__weight > self.__ideal * 1.05) and (self.__weight <= self.__ideal * 1.5):
                    self.__status[1] = "fat"
                    self.__hpm = 1.05
                elif self.__weight < (self.__ideal * 0.95):
                    self.__status[1] = "malnourished"
                    self.__hpm = 0.95
                elif self.__weight > (self.__ideal * 1.5):
                    self.__status[1] = "REALLY FAT"
                    self.__hpm = 1.5

                if (self.__hapiness < -100) and (self.__hapiness >=-999):
                    self.__status[0] = "depressed"
                    self.__maxhp = self.__maxhpog * 0.65
                elif self.__hapiness < -999:
                    self.__status[0] = "dead inside"
                    self.__maxhp == self.__maxhpog * 0.1
                elif (self.__hapiness >= -100) and (self.__hapiness <= 150):
                    self.__status[0] = "happy"
                    self.__maxhp == self.__maxhpog 
                elif self.__hapiness > 151:
                    self.__status[0] = 'jumping with joy'
                    self.__maxhp = self.__maxhpog * 1.25
                
                if self.__hp > self.__maxhp:
                    self.__hp = self.__maxhp
                


                if self.__hp <= 0:
                    self.__status[2] = 'dead'
                if self.__weight <= 0:
                    self.__status[2] = 'dead'
                if self.__status[2] == 'dead':
                    print(f"{self.name} has died")
                    self.status()
yang = petpetpet('Xiyang', 50, 80, 50, ['happy','fed', 'alive'], 1.00, 100,100)
yang.begin()