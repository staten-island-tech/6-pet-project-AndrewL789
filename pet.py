
# hero oactivity 
class Hero:
    def __init__(self, name, money, status, inv):
        self.name = name
        self.money = money
        self.inv = inv
        self.status = status

yangxi = Hero("YangXi", 3.99, "Bonce Cancer", "dirty used syringe")

print(yangxi)