
#Collection DataType
-helps to store multiple values of different datatypes

Types of Collection Datatype 

1. List
2. Tuple
3. Set
4. Dictionary


# List Syntax - use square brackets []
# <varaible_name> = [<val1>, <val2>, <val3> ...so on]

Eg-1
stud1_mark_Math = 75
stud1_mark_Science= 70
stud1_mark_Accounts = 80

stud1_marks = [75, 70, 80]
print(stud1_marks)

#Eg-2

# To create a list just use [] square brackets
shop_list = ["Egg", 4, True, "Egg" ]
print(shop_list)
print(type(shop_list))

# To create a list just use () round brackets
shop_list = ("Milk", 1, True )
print(shop_list)
print(type(shop_list))

# To create a list just use {} curly brackets
shop_list = {"Bread", 10, True, "Bread"}
print(shop_list)
print(type(shop_list))

#how to access a particular value of a colection datatype
#               0     1        2         3     -> index numbers
shop_list = ["Egg","Bread", "Butter", "Milk" ]

#Syntax-> <variable_name>[<index number>])
#EG->
print(shop_list[3])
print(shop_list[0])

#iterating each value of a list using - FOR loop
for item in shop_list:  # EXAMPLE 1
    print(item)


for item in shop_list:  # EXAMPLE 2
    if item == "Bread":
        print("dont't forget to also buy JAM!!")



#changing a particular value of a list using index number
#----------------------------------------------------------
print(shop_list)
shop_list[2]= "JAM"
print(shop_list)


#adding extra value inside already created list
#----------------------------------------------
# .append() -> helps to add value/item at the end of a list

#Syntax - <list_variable_name>.append(<value>)
#EG
#               0     1        2         3     -> index numbers
shop_list = ["Egg","Bread", "Butter", "Milk" ]
print(shop_list)
shop_list.append("JAM")
print(shop_list)



#removing specific value from a already created list
#----------------------------------------------
# .remove() -> helps to remove value/item from a list

#Syntax - <list_variable_name>.remove(<value/item_name>)

#EG
shop_list = ["Egg","Bread", "Butter", "Milk", "JAM"]
print(shop_list)
shop_list.remove("Butter")
print(shop_list)


# Deleting a already created list
#--------------------------------

#del - helps to delete a list from RAM

# syntax - del <list_variable_name>

#Eg
# shop_list = ["Egg","Bread", "Butter", "Milk", "JAM"]
# del shop_list
# print(shop_list)
#NOTE-> this will give error-> since we already deleted shop_list

#Example
try:
    shop_list = ["Egg","Bread", "Butter", "Milk", "JAM"]
    del shop_list
    print(shop_list)

except:
    print("Shop_list is deleted from RAM")

else:
    print("its not deleted")

# Write a program to create a list and then ask user wheather he wanted to sort or not
def filter():
        SHOP_LIST.sort()
        print(SHOP_LIST)
  
SHOP_LIST=input("enter list item sperated by space:").split()
usr_choice = input("Do you want to sort you list items[Yes/No]")
if usr_choice == "Yes":
    filter()
else:
    print(SHOP_LIST)    



