class Warrior:
    def __init__(self, health = 100, stamina= 100):
        self.health = health
        self.stamina = stamina
    def introduce(self):
        print('-----------')
        print(f'Class: {self.__class__.__name__}',
              f'\n Health: {self.health}',
              f'\n Stamina: {self.stamina}')
        print('------------')
unit1 = Warrior()
unit2 = Warrior()

print(unit1.__dict__)
print(unit2.__dict__)
class Mage:
    def __init__(self, health = 60, mana = 100):
        self.health = health
        self.mana = mana
    def introduce(self):
        print('-----------')
        print(f'Class: {self.__class__.__name__}',
              f'\n Health: {self.health}',
              f'\n Stamina: {self.mana}')
        print('------------')

    def heals(self):
        print('-------------')
        print(f'{self.__class__.__name__} casts a healing spell')
        self.health += 10
        self.mana -= 20
        print(f'Health of {self.__class__.__name__} has been raised to {self.health}',
              f'\n {self.__class__.__name__} has {self.mana} mana points left')

unit4 = Mage(50, 110)
unit3 = Mage()
unit3.heals()
unit3.heals(unit1)

print(unit3.__dict__)