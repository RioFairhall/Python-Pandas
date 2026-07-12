# #WRITe A CODE - to check if a user can vote

usr_age = 7
if (usr_age>18):
    print("yOU CAN VOTE")

# #Write a program - to check if a user have DL lisence
#                  - if user have DL lisence - print - "you can go"

usr_have_dl = input("Do you have DL [Yes / No]:")
if (usr_have_dl == "Yes"):
    print("You can go")
else:
    print("either give ₹5000 or go for 3 months of imprisonment")
    

#write a program- to check percentage of a student
#                 - if student percentage is greater than 90 - print - "well done"
#                 - if student percentage is less than 90 - print - "keep going"

# condition - "percentage > 90"
# condition become true - print("well done")
# condition become false- print("keep going")

percentage = float(input("Enter your percentage:"))

if (percentage >= 90):
    print("well done")

elif (percentage<90 and percentage>=70):
    print("almost there, you can do it!!")

else:
    print("keep going")
