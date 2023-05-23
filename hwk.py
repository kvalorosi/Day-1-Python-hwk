# Excercise 1
# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.
list_num = 1
while list_num**3 <= 1000:
    print(list_num**3)
    list_num += 1


# Excercise 2
# Get first prime numbers up to 100 
# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break
num = 1
for i in range(1,101):
    if i % 2 == 0:
        print("not a prime number")
    else:
        print("i")
        
        
num = 100
if num <= 100:
    for i in range(1,101):
        if num % i == 0:
            print("is not a prime number")
        else:
            print("i")



# Excercise 3
# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
age=input("How old are you? ")
if age <= "18":
    print("kids")
if age is range(18,65):
    print("adults")
else:
    print("seniors")