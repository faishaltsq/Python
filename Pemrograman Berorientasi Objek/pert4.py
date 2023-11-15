class Hero:
    def __init__(self,name, health, attackpower):
        self.__name = name
        self.__health = health
        self.__damage = attackpower
        
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    def getDamage(self):
        return self.__damage
    
    def diserang(self, value):
        self.__health -= value
        
    def change(self, newDamage):
        self.__name = newDamage
        
        

hero1 = Hero("Sniper", 100, 10)


print(hero1.getName())
print(hero1.getHealth())
print(hero1.getDamage())
print(hero1.__dict__)
        
hero1.diserang(5)
print(hero1.__dict__)

hero1.change(10)
print(hero1.__dict__)