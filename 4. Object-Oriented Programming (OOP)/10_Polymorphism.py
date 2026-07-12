#POLYMORPHISIM
#=============

# Refers to usage of same object(function / operator) in different ways

# To achieve POLYMORPHISIM in Python, we can use following ways;
# 1. Operator Overloading
# 2. Function Overloading
# 3. Function Overriding
# 4. Duck Function

#Operator Overloading
#--------------------

# we can use '+' operator in different ways -1. to perform addition 2.to perform concatination
add = 5+6
print(add)

join = "Hello" + "Everyobne"
print(join)

# we can use '*' operator in different ways -1. to perform multiplication 2.to perform repeatition of a string
mul = 5*6
print(mul)

repeat = "Hello" * 2
print(repeat)



#Function Overloading - (though python don't allow but we can use "some jugaad" )
#-------------------------------------------------------------------------------
class new_class():
    
    def get_ear(self, is_hurt, is_dirty=None):
        
        if is_hurt == True:
            print("Put some bandages")
        
        if is_dirty == True:
            print("Go clean them!")
            
        
    def get_eye():
        print(animal._no_of_eyes)
    
    def get_leg():
        print(animal.no_of_legs)

new_obj1 = new_class()
new_obj1.get_ear(True) 
new_obj1.get_ear(True, is_dirty=True) 



# Function Overiding
#-------------------
class animal:
    __no_of_ears = "i 'm a private member"
    _no_of_eyes = "i 'm a protected member"
    no_of_legs = "i 'm a public member"
    
    def get_ear(self):    
        print(self.__no_of_ears)
        
    def get_eye(self):
        print(self._no_of_eyes)


animal1 = animal()
animal1.get_ear()


class child_class(animal):
    
    def get_ear(self, is_cold_outside):
        if is_cold_outside == True:
            print("need to cover ears")
        
    def get_eye():
        print(animal._no_of_eyes)
    
    def get_leg():
        print(animal.no_of_legs)

child_obj1 = child_class()
child_obj1.get_ear(True)






