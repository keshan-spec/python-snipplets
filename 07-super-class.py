# calling a method from another class
class Animal:
    def talk(self):
        print("I am an animal")


class Dog(Animal):
    def talk(self):
        print("I am a dog")
        # calling the talk method in the super class
        super(Dog, self).talk()
        #      ^ child class
        #           ^ this object
        #                    ^ super class method


doge = Dog()
doge.talk()
