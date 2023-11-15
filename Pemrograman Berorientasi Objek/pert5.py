
jumlahHero = 0
class Hero:
    def __init__(self,name, role, damage, health, armor):
        self.name = name
        self.role = role
        self.damage = damage
        self.health = health
        self.armor = armor
        self.jumlahHero = jumlahHero
        
    def jumlahHero(self):
        Hero.jumlahHero += 1
    
    def showInfo(self):
        print(f"{self.name} adalah hero dengan role {self.role}, damage {self.damage}, health {self.health}, dan armor {self.armor}")        
    
    
    def attack(self,enemy):
        print(f"{self.name} attacking {enemy.name}")
        enemy.health -= self.damage
        
        
    def getName(self):
        return self.name
    
    def setName(self,newName):
        self.name = newName
        return self.name
    
    @staticmethod
    def getRole():
        return "Assassin"
    
    @classmethod
    def getJumlahHero(cls,):
        return cls.jumlahHero
    @property
    def info(self):
        return self.showInfo()
    
    @property    
    def armor(self):
        pass
    
    @armor.getter
    def armor(self):
        return self.armor
    @armor.setter
    def armor(self,value):
        pass
    
class Enemy:
    def __init__(self,name,health,armor):
        self.name = name
        self.health = health
        self.armor = armor
    
    def showInfo(self,health):

        if health <= 0:
            print(f"{self.name} is dead")
        else:
            print(f"{self.name} memiliki health {self.health} dan armor {self.armor}")
        
        

hero1 = Hero("fanny","Assassin", 100, 100, 100)
enemy1 = Enemy("Dyrroth",100,100)


print(hero1.getName())

print(hero1.__dict__)
hero1.attack(enemy1)
print(enemy1.__dict__)
enemy1.showInfo(enemy1.health)

print(hero1.setName("Lancelot"))
print(hero1.__dict__)

print(Hero.getRole())
print(Hero.getJumlahHero())

        
        
    
    