a=int(input("Enter your height in cm: ")) # Accepting height in cm from user
print("Your height is ", ((a/2.54)//12), "ft ", ((((a/2.54)/12)-((a/2.54)//12))*12), "inches.")

# In ((a/2.54)//12), height in cm is converted in inches first and then floor divided by 12 to 
# convert into feet without decimal part, which gives the whole number part of feet as output.
 
# The ((((a/2.54)/12)-((a/2.54)//12))*12) can be broken into two parts, ((a/2.54)/12) and ((a/2.54)//12).

# In ((a/2.54)/12), height in cm is directly converted from cm to feet with the decimal part, by dividing 
# the input by 2.54 and then again diving the result by 12.
 
# In ((a/2.54)//12), height in cm is converted in inches first and then floor divided by 12 to convert 
# into feet without decimal part, which gives the whole number part of feet as output. 

# Both of these expressions are subtracted to given the decimal part of the height in feet, which 
# is then multiplied by 12 to convert it into inches.

# Thus the entire program gives the answer into two parts, in feet and in inches. 

# This approach has been done for this problem to reduce memory consumption through excessive 
# usage of variables, resulting in the program to run fast while also keeping the file size small.