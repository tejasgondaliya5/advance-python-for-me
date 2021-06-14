from abc import ABC, abstractmethod

class DefenceForce(ABC):
    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print("gun = AK47")

class Army(DefenceForce):
    def area(self):
        print("area = Land")

class AirForce(DefenceForce):
    def area(self):
        print("area = sky")

class Nevi(DefenceForce):
    def area(self):
        print("area = Water")

ar = Army()
ai = AirForce()
ne = Nevi()
print()

ar.area()
ar.gun()
print()

ai.area()
ai.gun()
print()

ne.area()
ne.gun()