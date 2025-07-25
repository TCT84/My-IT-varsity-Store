#Loop Control Statement

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break # Exists the loop if cherry is found
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
        continue # Skips cherry and moves to the iteration
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
        pass # Placeholder, no action is need for cherry
    print(fruit)  
    
count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break # Exist the loop when the count is reached -3
    
#Operators

# Addition (+)
# subtraction (-)
# Multiplication (*)
# Division (/)
# Modulus (%)
# Exponets (**)

x = 10
y = 2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(5%2)
print(x**y )
      