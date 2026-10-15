def calculate_sum(): 
  global sum, number1, number2
  number1 = float(input("Enter first number: "))
  number2 = float(input("Enter second number: "))
  sum = number1 + number2 

def calculate_difference(): 
  global difference
  difference = number1 - number2

calculate_sum()
calculate_difference()
print(number1)
print(number2)
print(sum)
print(difference)
