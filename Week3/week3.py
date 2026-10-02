height = float (input ("Please enter rectangle height: " ))
width = float (input ("Please enter rectangle width: " ))
rectangle_area= height * width
print ("Your rectangle area is :" , rectangle_area)


mile = float(input("Please enter mile:"))
gallon = float (input("Please enter gallon:"))
MPG = mile / gallon
print  ("MPG :" , MPG)

#
fahrenheit = float(input("Enter fahrenheit degree: "))
celsius = float(fahrenheit - 32)/ 1.8
print("celsius:", celsius )

starting_day = int (input("Enter your starting day of the vacation( Begin 0 = Sunday to 6 = Saturday ) :"))
vacation_length = int (input("Enter the length of the vacation:"))
vacation_end_day = (starting_day + vacation_length ) % 7
print("your vacations ends on the day",vacation_end_day)

import math
radious = float(input("Enter circle radious:"))
circumfrense = 2*math.pi*radious
print ("circumfrense :",circumfrense)

birth_year = int(input("enter your birth year:"))
your_age = 2024 - birth_year
print( "your age is:",your_age)

