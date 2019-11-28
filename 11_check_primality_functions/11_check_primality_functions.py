#!/usr/bin/python3

def is_number_of_divisors_more_than_one(number):
  potential_divisors = range(1,int(number/2))
  count = 0

  for divisor in potential_divisors:
    if number % divisor == 0:
      count += 1
    if count > 1:
      return True

  return False

def is_prime(number):
  if(is_number_of_divisors_more_than_one(number)):
    print(str(number) + " isn't prime!")
  else:
    print(str(number) + " is prime!")

the_number = int(input("Enter a number: "))

is_prime(the_number)