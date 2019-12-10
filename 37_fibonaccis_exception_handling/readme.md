# Fibonacci's Exception Handling
Remember that you have already implemented Fibonnaci numbers generator in exercise 13. Update the program by exception handling (ValueError) to inform users about incorrect, not numeric inputs. The output should be the following in case of correct and incorrect inputs:

Normal case:
```
Number of elements from Fibonacci List: 5
[1, 1, 2, 3, 5]
```

Error case:
```
Number of elements from Fibonacci List: wrong input
ERROR: invalid literal for int() with base 10: 'wrong input'
```

Use built-in "Argument" to get the exact error message: "invalid literal for int() with base 10: 'wrong input'"