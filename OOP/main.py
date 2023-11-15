# __ private acces modifier
# _ protected acces modifier



class Player:
    def __init__(self, health = 100, energy = 100):
        self.health = health
        self.energy = energy
        print("Player created")
        
    def attack(self,monster, damage = 1):
        monster.health -= damage
        self.energy -= damage
        print(f"Launch attack, monster health: {monster.health} left")
        
class Monster:
    def __init__(self, health = 100):
        self.health = health
        print("Monster created")
        
        
        
player = Player()

monster = Monster(health=1000)

player.attack(monster, damage=180)

print(monster.__dict__)