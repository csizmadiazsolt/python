#!/usr/bin/python3

number = int(input("Enter a number: "))
potential_divisors = range(1,int(number/2))
divisors = []

for divisor in potential_divisors:
  if number % divisor == 0:
    divisors.append(divisor)
	
divisors.append(number)

print(*divisors, sep=', ')