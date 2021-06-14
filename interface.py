'''
- interface concept dose not any connect to java
- python me interface no matlab abstract class ma only abstract method hoy koi concrete method na hoy tene interface kehvay 6
- EX:-  class Father(ABC):
            @abstractmethod
            def disp(self):
                pass

'''
from abc import ABC, abstractmethod
class DefenceForce(ABC):
    @abstractmethod
    def Gun(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Army(DefenceForce):
    def Gun(self):
        print("Gun = AK47, M416, M762")

    def area(self):
        print("Army area = Land")

class AirForce(DefenceForce):
    def Gun(self):
        print("Gun = kar98k, M24, AWM")

    def area(self):
        print("AirForce area = Sky")

class Navy(DefenceForce):
    def Gun(self):
        print("Gun = submarine, missaile")

    def area(self):
        print("Navy area = Sea")

army_obj = Army()
AirForce_obj = AirForce()
Navy_obj = Navy()

army_obj.Gun()
army_obj.area()
print()

AirForce_obj.Gun()
AirForce_obj.area()
print()

Navy_obj.Gun()
Navy_obj.area()
