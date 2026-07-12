#why to use Dictionary
#---------------------

stud1_math_marks = 70
stud1_science_marks = 80
stud1_english_marks = 75

student1_marks = [70, 80, 75]  # this is a list

# dictionary = { <key>:<value>}

student2_marks = {"math":70, "science":80, "english":75}
print(student2_marks)
print(type(student2_marks))\



# i want to create a list to store student's names
student_enrolled = ["rahul", "yash", "suraj"]

#hey, can store some information about sutdents
student1 = {"name":"rahul", "age":21, "address":"Pune", "mob_no":8904562074}
student2 = {"name":"yash", "age":21, "address":"Pune", "mob_no":8904562074}
student3 = {"name":"sauraj", "age":21, "address":"Pune", "mob_no":8904562074}

#you can store other collection datatype inside a dictionary
student1 = {"name":"rahul", "age":21, "address":"Pune", "mob_no":[8904562074, 7894850231]}

#you can store other dictionary inside a dictionary
student_details  = {
                    "student1":{"SrNO": 1 , "Email": "some_mail_id@domain.com", "MobileNO":[8978456310,9852034517]},
                    "student1":{"SrNO": 1 , "Email": "some_mail_id@domain.com", "MobileNO":[8978456310,9852034517]}
                }
    
print(student_details)



#how to access values of a specific key - stored inside a dictionary
#-------------------------------------------------------------------

# using .get()
# dictionary_var_name.get("<key_name>")

#EG
student1 = {"name":"rahul", "age":21, "address":"Pune", "mob_no":8904562074}

print(student1.get("address"))

#EG2
student_details  = {
                    "student1":{"SrNO": 1 , "Email": "some_mail_id@domain.com", "MobileNO":[8978456310,9852034517]},
                    "student2":{"SrNO": 1 , "Email": "some_mail_id@domain.com", "MobileNO":[8978456310,9852034517]}
                }

print(student_details.get("student1").get("Email"))
    # -------------------------------
    #                 |
    #                 v
    #  -----------------------------------------------------------------------------------
    # |                                                                                  |
print({"SrNO": 1 , "Email": "some_mail_id@domain.com", "MobileNO":[8978456310,9852034517]}.get("Email"))



print({"SrNO": 1 , "Email": "some_mail_id@domain.com", "MobileNO":[8978456310,9852034517]}.get("MobileNO")[0])






#how to access all keys - stored inside a dictionary
#-------------------------------------------------------------------

# using .keys()
# dictionary_var_name.keys()

#EG
student1 = {"name":"rahul", "age":21, "address":"Pune", "mob_no":8904562074}
print(student1.keys())



#how to iterate on a dictionary
#------------------------------
student_details  = {
                    "student1":{"SrNO": 1 , "Email": "some_mail_id@domain.com", "MobileNO":[8978456310,9852034517]},
                    "student2":{"SrNO": 1 , "Email": "some_mail_id@domain.com", "MobileNO":[8978456310,9852034517]},
                    "student3":{"SrNO": 1 , "Email": "some_mail_id@domain.com", "MobileNO":[8978456310,9852034517]},
                    "student4":{"SrNO": 1 , "Email": "some_mail_id@domain.com", "MobileNO":[8978456310,9852034517]},
                    "student5":{"SrNO": 1 , "Email": "some_mail_id@domain.com", "MobileNO":[8978456310,9852034517]}
                }
# traditionally we use print() to show value of specific key on by one
# print(student_details.get("student1"))
# print(student_details.get("student2"))
# print(student_details.get("student3"))
# print(student_details.get("student4"))
# print(student_details.get("student5"))

# instead we can use loop
# for <var_name> in <dictionary_variable_name>:
#     .get(var_name)
#     var_name= key_name


#EG
for key in student_details:
    print(student_details.get("student2"))
    
#or

for key in student_details:
    print(student_details[key])

#EG2
student1 = {"SrNO": 1 , "Email": "some_mail_id@domain.com", "MobileNO":[8978456310,9852034517]}
for key in student1:
    print(student1.get(key))
    



