# DATA HIDING
# ===========

#Achieve using Access Modifiers - 3 types - 1. Private 2. Protected 3. Public

#1. Private - No one can access class's member outside of a class
#2. Protected - Only child class can access member of a class
#3. Public - Everyone can access members of a class

#How to make a member of a Class - as Private Memeber
#using "_ _" double undrscore

#Syntax - no_of_ears is a member of animal class -> to make it private -> __no_of_ears


#How to make a member of a Class - as Protected Memeber
#using "_" single undrscore

#Syntax - no_of_eyes is a member of animal class -> to make it protected -> _no_of_eyes


#How to make a member of a Class - as Public Memeber
#you don't need to maunally create a public member - > BY default all members of a class are public


class animal:
    __no_of_ears = "i 'm a private member"
    _no_of_eyes = "i 'm a protected member"
    no_of_legs = "i 'm a public member"
    
    def get_ear(self):    
        print(self.__no_of_ears)
        
    def get_eye(self):
        print(self._no_of_eyes)


animal1 = animal()
animal1.get_ear()  #-> this will not give error cause get_ear() function itself part of animal class so it can access __no_of_ears which is a private member
animal1.get_eye()
print(animal1.no_of_legs)

class child_class(animal):
    
    def get_ear(self):
        print(animal.__no_of_ears)
        
    def get_eye():
        print(animal._no_of_eyes)
    
    def get_leg():
        print(animal.no_of_legs)

child_obj1 = child_class()
child_obj1.get_ear() #-> this will give error cause get_ear() function will try to access __no_of_ears which is a private member
child_obj1.get_eye() #-> this will not give error cause get_eye() function is part of child_class who inherit _no_of_eyes from animal class
child_obj1.get_leg()

class new_class():
    
    def get_ear(self):
        print(animal.__no_of_ears)
        
    def get_eye():
        print(animal._no_of_eyes)
    
    def get_leg():
        print(animal.no_of_legs)

new_obj1 = new_class()
new_obj1.get_ear()  #-> this will give error cause get_ear() function will try to access __no_of_ears which is a private member
new_obj1.get_eye() #-> this will give error cause get_eye() function try to access _no_of_eyes which is a protected member


#outside a class
print(animal.__no_of_ears)
print(animal._no_of_eyes)
print(animal.no_of_legs)
