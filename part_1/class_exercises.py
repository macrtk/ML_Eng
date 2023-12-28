class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        if self.age % 10 in {2,3,4}:
            print(f"Witaj, mam na imie {self.name} i mam {self.age} lata.")
        else:
            print(f"Witaj, mam na imie {self.name} i mam {self.age} lat.")
person1 = Person("Matt",35)
person1
Person.greet(person1)