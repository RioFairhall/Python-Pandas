#write a programme to create a funtion name- area_of_square
#take length and breadth as a input from USER

# AND CALCULATE its area = length * breadth
#then output caclulated area

def area_of_rect():
    length = float(input("Enter length of a rectangle"))
    breadth = float(input("Enter breadth of a rectangle"))
    area = length * breadth
    print(area)

area_of_rect()


#write a programme to create a funtion name- area_of_square
#take either length or breadth as a input from USER

# AND CALCULATE its area = side * side -> means (length * length) or (breadth *breadth)
#then output caclulated area

def area_of_square():
    length = float(input("Enter length of a rectangle"))
    area = length * length
    print(area)

area_of_square()
