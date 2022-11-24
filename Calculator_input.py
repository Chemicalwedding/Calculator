#Creating a calculator
#first you need an input from a user, once received the following definitions are required
# a. chop up the string in parts
# b. variables in the input
# c. Variables in the result or outcome
# d. showing the expert
import math
request1  = float(input('please share your value you want to process through the calc?'))
request2  = float(input('please share an applicable value in this calc?'))
calcpower = input("How do you calculate both values? (+)").strip()
list_of_floats = [request1, request2]
if calcpower == '+':
	power = math.fsum(list_of_floats)
if calcpower == '-':
	power = request1 - request2
if calcpower == '*':
	power = request1 * request2
if calcpower == '/':
	power = request1 / request2
if calcpower == 'tan':
  power = math.atan2(request1, request2)
	
print("output is:", "", power)