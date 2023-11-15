class Hero:
    def __init__(self, health, damage, armor, role):
        self.armor = armor
        self.health = health
        self.damage = damage
        self.role = role
        
    def attack(self, enemy):
        enemy.health -= self.damage
        print(self.name + " menyerang " + enemy.name)
        
    def printInfo(self):
        print("Hero health: " + str(self.health))
        
class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
        
    def info(self):
        print("enemy health: " + str(self.health))
        
    def attack(self, hero):
        hero.health -= self.damage - hero.armor
        hero.armor -= self.damage
        print(self.name + " menyerang " + hero.name)
        

hero = Hero(100, 20, 50, "melee")
enemy = Enemy(100, 30)

hero.name = "sniper"
enemy.name = "monster"

hero.attack(enemy)
hero.attack(enemy)
enemy.info()

enemy.attack(hero)
enemy.attack(hero)
hero.printInfo()
        
        