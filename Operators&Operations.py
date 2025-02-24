# Operations & Operators in PYTHON

# 1. Arithmetic Operations
# 2. Assignment
# 3. Comparision
# 4. Logical
# 5. Bitwise
# 6. Identity
# 7. Membership

#Arithmetic Operations
num1 = 13
num2 = 2

add = num1 + num2
print(add)

subs = num1 - num2
print(subs)

mul = num1 * num2
print(mul)

div = num1 / num2
print(div)


print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)


#Modulus -> % -when you need the remainder
mod = num1%num2 
print(mod)

#check if a number is even or odd
# if number%2==0 -> it is a even
# if number%2==1 -> it is a odd


#Floor Division -> when you don't want decimal value in division result
num1 = 11
num2 = 3
print(num1/num2)   #it gives decimal value - float
print(num1//num2)  # it gives non-decimal value - integer
#calculate time
distance = 452.13
speed_km_per_h = 7
time = distance // speed_km_per_h
print(time)

#Exponentiation -> for power - 2^3 => 8
num1 = 2
power = 3
print(num1 ** power)

#calculate area of square - (side ^ 2)
side = 45
area = side ** 2 
print(area)
