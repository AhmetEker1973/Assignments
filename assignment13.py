# Assignment-13 (Python - Is it a Prime Number?)
<<<<<<< HEAD
=======

>>>>>>> 051fba16b415cf74f88215f258f7057404c43cc2
sayı = int(input("Please enter a number"))

if sayı > 1 :

    divisors = range(2, sayı)
    
    for i in divisors :
        if sayı == 2 :
            print(f"{sayı} is a prime number")
            break
        elif sayı % i == 0 :
            print(f"{sayı} is not a prime number")
            break 
    else :
        print(f"{sayı} is a prime number")
  
else :
    print("Invalid entry. Please enter a positive number greater than 1!")

Please enter a number: 9
9 is not a prime number
Please enter a number: 1
Invalid entry. Please enter a positive number greater than 1!
Please enter a number: 25
25 is not a prime number
