from OOPpractice import Warrior, Mage

class Archer(Warrior):
    def __init__(self,health = 100, stamina = 100 , arrows = 20):
        super().__init__(health, stamina)
        self.arrows = arrows
    def introduce(self):
        super().introduce()
        print('------------')
        print(f'Arrows: {self.arrows}')
        print('------------')
    def attack(self,target):
        target.health -= 3
        self.arrows -= 1
        print(f' {self.__class__.__name__} used a bow against the {target.__class__.__name__} \n health of {target.__class__.__name__} has been lowered to {target.health} \n'
              f'there are {self.arrows} left in the Archers quiver')


unit1 = Archer()
unit2 = Archer()

print(unit1.__dict__)



class Alchimist(Mage):
    def __init__(self, health = 100 , mana = 60, flaks = 10):
        super().__init__(health,mana)
        self.flaks = flaks

    def introduce(self):
        super().introduce()
        print('------------')
        print(f'flakes: {self.flaks}')
        print('------------')
    def attack(self, target):
        target.health -= 10
        self.health -=3
        self.flaks -= 1
        print(f'{self.__class__.__name__} attacked {target.__class__.__name__} with a Flack of flame,\n'
              f'but barns himself in the process.'
              f'{target.__class__.__name__} healths dropped to {target.health}'
              f'{self.__class__.__name__} health dropped to {self.health}'
              f'there are {self.flaks} alchemy flakes left in the Archimists invetory/')
