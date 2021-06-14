'''
--> Abstract Class :
- abstract class ma beetween perantheses ABC apvi pade tethi te abstract class bane.
  EX:- class Father(ABC):    this is abstract class

- abstract class is called meta class.

- abstract class no object create na thay

--> Abstract method :
- abstract method ma koi definition na lakhava ni hoy
- abstract method ma khali pass lakhi java deva nu.
  EX:-  class Father(ABC):

            @abstractmethod
            def disp(self):
                pass
--> Concrete method :
- abstract class ni andar method ne define kari daiye tene concrete method kehavay
  EX:- class Father(ABC):

           @abstractmethod
           def disp(self):
               pass

           def show(self):
               print("concrete Method")

'''

from abc import ABC, abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):                      # this is abstract method
        pass

    def show(self):                     # this is normal or concrete method
        print("concrete method")

class Son(Father):                       # this is inheritance for abstrect class
    def disp(self):                      # this line is difiend abstract method
        print("child class")
        print("Defining Abctract method")

c = Son()                               # create object
c.disp()                                # call abstract method
print()

c.show()                                # call concrete method
