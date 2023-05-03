#InajmTanvir
'''
Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking the user input - assume the user types numbers properly.
'''


hours = float(input("Please enter hours: "))
rate = float(input("Please enter a rate for per hour: "))

if hours <= 40:
    gross_pay = hours * rate
    print(gross_pay)

else:
    gross_pay = ((40 * rate) + ((hours - 40) * 1.5 * rate))  #Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
    print(gross_pay)

