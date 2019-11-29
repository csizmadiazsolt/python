#!/usr/bin/python3

def fibonacci(number):
  fibonacci_list = [1, 1]

  for i in range(0,number-2):
    list_lenght = len(fibonacci_list)
    new_element = fibonacci_list[list_lenght-2] + fibonacci_list[list_lenght-1]

    fibonacci_list.append(new_element)

  return fibonacci_list

number_of_elements = int(input("Number of elements from Fibonacci List: "))
print(fibonacci(number_of_elements))