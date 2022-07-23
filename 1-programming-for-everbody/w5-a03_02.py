# 3.2 Write a program to prompt the user for hours and rate per hour using input to
#     compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the
#     hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50
#     per hour to test the program (the pay should be 498.75). You should use input to
#     read a string and float() to convert the string to a number. Do not worry about error
#     checking the user input - assume the user types numbers properly.

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

try:
    fh = float(sh)
    fr = float(sr)

except:
    print("Error, numeric inputs only")
    quit()
    
if fh > 40 :
    regp = 40 * fr
    otp = (fh - 40) * fr * 1.5
    fullp = regp + otp
else :
    fullp = fh * fr

print('Pay: ', fullp)

