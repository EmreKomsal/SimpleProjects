#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Class Structure Demo

@author: ekomsal
"""

class Person:
    def __init__(self,name,surname,age):
        self.name = str(name)
        self.surname = str(surname)
        self.age = int(age)
        
    def introduce(self):
        print("This person is " + self.name + " " + self.surname)
        
    def howold(self):
        print( self.name +" is " + str(self.age) + " years old.")
        
class Worker(Person):
    def __init__(self, name, surname, age, salary):
        self.name = str(name)
        self.surname = str(surname)
        self.age = int(age)
        self.salary = int(salary)
        
    def howmuch(self):
        print( self.name +"'s salary is " + str(self.salary) + " dollars")
        
        
worker = Worker("Emre", "Komşal", 25, 2500)

person = Person("Ali", "Kuş", 14)

worker.howmuch()

worker.howold()

worker.introduce()

person.introduce()

person.howold()
        