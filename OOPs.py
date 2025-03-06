#define class:
    #information about "the object itself"
    
    #information about "what a object can do" 

#create object based on Class

#-----------------------------------------------

class Tata_Cars:
    #information about "the object (car) itself" using variables
    No_of_seats = 5
    car_color = "Red"
    Engine = "V12"
    
    #information about "what a object(car) can do" 
    def Auto_Start(self):
        print("Starting the Engine....")
        print("Car is started now")
        print("Ready to go for a drive :)")
        
    def AirBag(self, sudden_impac):
        if(sudden_impact == True):
            print("Opening the AirBag..")
        else:
            print("No need to do any experiment!")

#creating a Object
#Syntax -> #<object_name> = <class_name>()

#eg
car1 = Tata_Cars()

#how to access info about the object
# use .<variable_name>
# use .<fucntion_name>()

#Eg
print(car1.car_color)
print(car1.Engine)
print(car1.Auto_Start())
print(car1.AirBag(True))



#Constructor
#============

class Tata_Cars:
    #information about "the object (car) itself" using variables
    
    #constructor -its a special type of function created by Python itself
    #             to assign variable with initial values at time when 
    #             objects are being created
    
    # def __init__(self, <val1>, <val2>):
    #   self.<variable_name> = <val1>
    #   self.<variable_name> = <val2>


    def __init__(self, seats, color, engine_ver, model):
        self.No_of_seats = seats
        self.car_color = color
        self.Engine = engine_ver
        self.car_model = model
    
    #information about "what a object(car) can do" 
    def Auto_Start(self):
        print("Starting the Engine....")
        print("Car is started now")
        print("Ready to go for a drive :)")
        
    def AirBag(self, sudden_impact):
        if(sudden_impact == True):
            print("Opening the AirBag..")
        else:
            print("No need to do any experiment!")

#creating a Object
#Syntax -> #<object_name> = <class_name>()

#eg
car1 = Tata_Cars("5", "Black", "V10", "sport")
car2 = Tata_Cars("6", "NavyBlue", "V12", "sport")
#how to access info about the object
# use .<variable_name>
# use .<fucntion_name>()

#Eg
print(car1.car_color)
print(car1.Engine)
print(car1.car_model)

print(car2.car_color)
print(car2.Engine)
print(car2.car_model)
