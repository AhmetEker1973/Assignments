# num is taken as str to be able to count its digits and 
# isnumeric() method distinguishes int and float numbers since
# it returns false if any of the user-entered number's characters is  dot or comma

num = input("Please enter a positive number: ")

if num.isnumeric() == True and int(num) >= 0 :

  sum_digits = 0

  for i in num :
  
    sum_digits += int(i)**len(num)
 
  if int(num) == sum_digits :
    print(f"'{num}' is an Armstrong number")
  else :
    print(f"'{num}' is not an Armstrong number")

else :
  print(f"'{num}' is an invalid entry. Don't use non-numeric, float, or negative values!")

Please enter a positive number: 0
'0' is an Armstrong number
Please enter a positive number: 121
‘121’ is not an Armstrong number
Please enter a positive number: 6
‘6’ is an Armstrong number
Please enter a positive number: 407
‘407’ is an Armstrong number
Please enter a positive number: -153
‘-153’ is an invalid entry. Don't use non-numeric, float, or negative values!
Please enter a positive number: 153.87
‘153.87’ is an invalid entry. Don't use non-numeric, float, or negative values!
Please enter a positive number: one
‘one’ is an invalid entry. Don't use non-numeric, float, or negative values!
