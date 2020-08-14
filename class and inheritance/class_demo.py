class Animal:

    #Initialization, not construction, constucton is done by __new__
    #self: conventional variable stores object itself
    #def __init__(self, name ,legs, eye):

    def __init__(self, name ,legs, eye):
        self.legs = legs
        self.eye = legs
        self.name = name
        print("Called automatically.")
    
    def walk(self, speed): #Class funcs.
        print("OBJ self: ", id(self))
        print("I walk with", self.legs, "legs", "speed: ", speed)
    
    def sleep(self):
        print("I sleep with eyes closed")

    def feeding_type(self):
        print("Not sure at this point")

Dog = Animal("Dog",4,2)
Horse = Animal("Horse",4,2)
Snake = Animal("Snake",0,2)

#"Fast")
print("-------")
animals = [Dog, Horse, Snake]
for a in animals:
    a.sleep()
    a.feeding_type()
#    a.walk("Slow")




class Mammal(Animal, AnotherAnimal):
    def __init__(self, name ,legs, eye):
        super(Mammal, self).__init__(name, legs, eye)

    def feeding_type(self):
        print("Breast fed milk")




m= Mammal("Whale", 0, 2)
h = Mammal("Humans", 2, 2)


# list_of_animals = [Dog, Horse, Snake, m]
# for a in list_of_animals:
#     print("-----------------")
#     print("I am a:", a.name, type(a), dir(a))
#     print("Legs: ", a.legs, "Eyes: ", a.eye, "Walk Type:", a.walk("fast"))

