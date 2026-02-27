# Subscripting
print("Hello"[0:5])

# Strings
print("123" + "345") # Concatenation

# Integer = Whole number
print(123 + 345)

# Large Integers
print(123_456_789)

# Float = Floating Point Number
print(3.1456)

# Boolean
print(True)
print(False)


print(len("12345"))

print(type(12345))
print(type(3.14))
print(type("3.14"))
print(type(True))


#Changing string summary contatination to math summary
print(int("123") + int("456"))

name_of_the_user = input("Enter your name: ")
lenght_of_the_name = len(name_of_the_user)

print(type("Numbers of letters in your name: ")) #str
print(type(lenght_of_the_name)) #int


print("Numbers of letters in your name: " + str(lenght_of_the_name))

name_of_the_user = input("Enter your name: ") # str
lenght_of_name = len(name_of_the_user) # int


print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(5 / 3)
print(5 // 3)
print(2 ** 3)

print(3 * (3 + 3) / 3 - 3)


bmi = 84 / 1.65 ** 2

print(bmi)
print(int(bmi))
print(round(bmi, 2))

# Number Manipulation

score = 0

# User scores a point
score +=1
print(score)
# score -=1
# score *=1
# score /=1



# F-strings

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your high is {height}, You are winning {is_winning} ")
