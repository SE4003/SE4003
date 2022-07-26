# Trap invalid number input to avoid program crash and inform user.
# Continue loop until it is valid then break out of loop.
while True:
  number = input('What is the number to square? ')
  try:
    number = float(number)
    break
  except ValueError:
      print ("That is not a floating point number.  Try again")

number_squared = number * number
print(number, 'squared = ', number_squared)
