class Hero:
    def __init__(self,name,health):
        self.__name = name
        self.__health = health

    @property
    def name(self):
        pass

    @name.getter
    def name(self):
        return self.__name

class Hero_intelligent(Hero):
    def __init__(self,name,health,mind):
        super().__init__(name,health)
        self.mind = mind

budi = Hero("Budi",100)
zhask = Hero_intelligent("Zhask",100,100)
print(zhask.__dict__)
print(budi.__dict__)