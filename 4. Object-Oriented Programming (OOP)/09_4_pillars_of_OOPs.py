class Tata_Cars:  #Encapsulation - class binds the variables & function into a single unit

    def __init__(self, seats, color, engine_ver, model):
        self.No_of_seats = seats
        self.car_color = color
        self.Engine = engine_ver
        self.car_model = model
    

    def Auto_Start(self):
        #Abstraction
        #-----------
        # removing Unneccessary information
        # print("Ignite system just receive petrol")
        # print("opeing chamber to come air for spark to happen")
        # print("Spark occured")
        
        #only showing what user / customer need to know
        print("Starting the Engine....")
        print("Car is started now")
        print("Ready to go for a drive :)")
        
    def AirBag(self, sudden_impact):
        if(sudden_impact == True):
            print("Opening the AirBag..")
        else:
            print("No need to do any experiment!")


#eg
car1 = Tata_Cars("5", "Black", "V10", "sport")
car2 = Tata_Cars("6", "NavyBlue", "V12", "sport")

print(car1.car_color)

print(car2.car_color)


#---------------------------------------------------------------------------------------------

#Inheritance
class <parent_class_name>:
   def __init__(self, <val1>, <val2>):
        self.<variable_name> = <val1>
        self.<variable_name> = <val2>
    
    def <function_name>(self):
        code statement1
        code statement2

class <child_class_name>(<parent_class_name>):
 




class character_base_class:
    
    def __init__(self, name, gender):
        self.character_name = name
        self.character_gender = gender
    
    def move_right(self):
        print("Moving in right direction")
    
    
    def move_left(self):
        print("Moving in left direction")

    def move_up(self):
        print("Moving in Upward direction")

    def move_down(self):
        print("Moving in Downward direction")
    

class sniper_sub_class(character_base_class):
    health_bar = 70
    
    def shoot(self):
        print("person is killed!")

    
agent41 = sniper_sub_class("agent41", "Male")
print(agent41.character_name)
agent41.move_down()
agent41.shoot()


