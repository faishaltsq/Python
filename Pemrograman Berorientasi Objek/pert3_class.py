class Hero:
    jumlah_hero = 0
    def __init__(self, name,jenis,health,armor,damage):
        self.name = name
        self.jenis = jenis
        self.health = health
        self.armor = armor
        self.damage = damage
        
        Hero.jumlah_hero += 1
        print("membuat hero dengan nama: " + name)
    
    def void(self):
        print("hei, nama saya adalah", self.name)
        
    def healthup(self,up):
        self.health += up
        
    def gethealth(self):
        return self.health

hero1 = Hero("sniper","ranged",100,10,15)
print(Hero.jumlah_hero)
hero2 = Hero("axe","melee",100,15,10)
print(Hero.jumlah_hero)
hero3 = Hero("sven","melee",1000,5,20)
print(Hero.jumlah_hero)
hero4 = Hero("luna","ranged",100,1,25)
print(Hero.jumlah_hero)

hero1.void()
hero1.healthup(10)

print(hero1.__dict__)   
print(hero2.__dict__)   
print(hero3.__dict__)   
print(hero4.__dict__)   

        


