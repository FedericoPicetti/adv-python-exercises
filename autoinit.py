"""Implements a metaclass (AutoInit) that detects the names of the constructor's arguments and  automatically initializes the corresponding fields with the actual values passed to the constructor."""
from inspect import signature
class AutoInit(type):
  def __init__(Class, classname, bases, attr):
    par = iter(signature(Class.__init__).parameters)
    def newinit(self, *args):
      
      next(par) #discard the 'self' name
      for arg in  args:
        kw = next(par)
        print(kw, arg)
        setattr(self, kw, arg)
    Class.__init__ = newinit


if __name__ == '__main__':
  class Person(metaclass=AutoInit):
    def __init__(self, name, age): pass

  class Circle(metaclass=AutoInit):
    def __init__(self, x, y, ray): pass

  class Car(metaclass=AutoInit):
    def __init__(self, model, color, plate, year):pass
  a_person = Person('John', 25)
  a_circle = Circle(0, 0, 3.14)
  a_car = Car('Ford Ka', 'Blue', 'AF329SZ', 1999) 

  print("A Person of name :- {}, and age :- {}."
      .format(a_person.name,a_person.age))
  print("A Circle centered in <{},{}>, and ray {}."
      .format(a_circle.x,a_circle.y, a_circle.ray))
  print("A {} {} whose plate is {} and was registered in {}."
      .format(a_car.color,a_car.model,a_car.plate,a_car.year))
