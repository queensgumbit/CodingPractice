class Warrior:
    def __init__(self, health=100, stamina=100):
        self.__health = health
        self.__stamina = stamina

    def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.__health}',
              f'\nStamina: {self.__stamina}')
        print('---------------')

    def heals(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} накладывает повязку из',
              f'целебных трав {target.__class__.__name__}')
        self.stamina += 10
        target.health -= 20
        print(f'health of {target.__class__.__name__}got up by {target.health}',
              f'\nthe {self.__class__.__name__} are left with {self.stamina} storage of stamina')
        print('---------------')
    def _get_health(self):
        return self.__healthן

    def _set_health(self, points):
        self.__health += points
        if self.__health > 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = 0

    def attacks(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} attacks {target.__class__.__name__}')
        target.health -= 3
        print(f'health of {target.__class__.__name__} got down by {target.health}')
        print('---------------')


class Mage:
    def __init__(self, health=60, mana=120):
        self.__health = health
        self.__mana = mana

    def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.__health}',
              f'\nMana: {self.__mana}')
        print('---------------')

    def _get_health(self):
        return self.__health

    def _set_health(self, points):
        self.__health += points
        if self.__health > 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = 0

    def heals(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} gets healed',
              f'к {target.__class__.__name__}')
        target.health += 10
        self.mana -= 20
        print(f'health of {target.__class__.__name__} got up by {target.health}',
              f'\nthe {self.__class__.__name__} is left with {self.mana} mana')
        print('---------------')

    def attacks(self, target):
        print(f'{self.__class__.__name__} attacks {target.__class__.__name__}')
        target.health -= 3
        print(f'health of {target.__class__.__name__} got down by {target.health}')
        print('---------------')


'''
#for the second presentation of encapsulation
from WarriorInheritance import Warrior, Mage

class Knight(Warrior):
    def __init__(self,health = 100, armor=100, stamina=100):
        super().__init__(health, stamina)
        self.__armor = armor
        self._health = 100
    def get_health(self):
        return self._health
    def _set_health(self,points):
        self._health += points
        if self._health > 100:
            self._health = 100
        elif self._health < 0:
            self._health = 0


unit1 = Knight()
unit2 = Knight()
unit1.attack(unit2)'''