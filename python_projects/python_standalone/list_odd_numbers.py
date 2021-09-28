# This program will list all the odd numbers between 1 and a user provided max number

max_number = int(input("Enter a number:")) # Takes a number from user as prompt

print("User entered: " + str(max_number))

odd_numbers =  []

for i in range(1, max_number):
   if i % 2 == 1:
       odd_numbers.append(i)
     
print("odd numbers array " + str(odd_numbers))