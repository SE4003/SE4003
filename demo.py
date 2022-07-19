# demonstrations of selected features

# print a string enclosed in quotes
print('Hello SE4003')

# print a string variable
today = "July 19, 2022"
print('Hello SE4003 on', today)

se4003_students = [
"Aftel, Nora",
"Berger, Michael",
"Chan, Aaron",
"Dinh, Tam",
"Elliott, Jeffrey",
"Gomez, Patricia",
"Harris, Desmond",
"Holder, John",
"Humphries, Tabitha",
"Joram, Michael",
"Knowles, Brian",
"Kutsunai, Jonathan",
"Laake, Jacob",
"Maganahalli, Nithisha",
"Martinez de Andino, Cary",
"Mclarney, Michael",
"Meyer, Erik",
"Murray, Andrew",
"Navarrete, Nathaly",
"Pompeii, Andrew",
"Porter, Preston",
"Purakary, Joffinv",
"Rodgers, Grant",
"Torres-Martinez, Kemuel",
"Vasquez, Christopher",
]

# loop through list and assign each value to the variable 'name' in each iteration
for name in se4003_students:
  print ('Hello', name)

# get user inputs and make variable assignments
name = input('What is your first name? ')
last_name = input('What is your last name? ')
print ('Hello', name, last_name)

# square a number provided by the user and print result
# input statement gets user input
# float function converts string input into floating point number for calculations
number = float(input('What is the number to square? ')) 
number_squared = number * number
print(number, 'squared = ', number_squared)

# if else conditional statement
number = float(input('What is a number between 0 - 10? '))
if number < 5:
  print("Your number was less than 5")
else:
  print("Your number was 5 or greater")
