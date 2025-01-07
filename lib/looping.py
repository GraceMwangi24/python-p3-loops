#!/usr/bin/env python3

def happy_new_year():
    countdown = 10 
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print ("Happy New Year!")
    # code goes here!
    pass

def square_integers(int_list):
    return [num ** 2 for num in int_list ]
    # code goes here!
    pass

def fizzbuzz():
    for number in range (1,101):
        if number % 3 == 0 and number % 5 == 0:
            print  ("FizzBuzz")
        elif number % 3 ==0 :
            print ("Fizz")
        elif number % 5 == 0:
            print ("Buzz")
        else:
            print(number)        

    # code goes here!
    pass
