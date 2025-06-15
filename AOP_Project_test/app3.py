import aspectlib
from app2 import *

def logBefore():
    print("This is logBefore...")

def logAfter():
    print("This is logAfter...")

print("========== Original result ==========")
dog = Dog("Buddy")
print(dog.speak())


@aspectlib.Aspect
def Aspect_(*args, **kwargs):
    logBefore()
    yield aspectlib.Proceed
    logAfter()

aspectlib.weave(Animal.speak, Aspect_)

print("========== Weaving result ==========")
dog2 = Dog("Pudding")
print(dog2.speak())

print("========== Weaving result ==========")