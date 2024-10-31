# Write a functiona reverse_string(s) that takes a string as input and returns the string in reverse order.

def reverse_string(s):
    return s[::-1]
  
print(reverse_string("hello")) # olleh

# Create a function is_palindrome(s) that takes a string as input and returns True if the string is a palindrome(reads the same backwards) and False otherwise.

def is_palindrome(s):
    return s == s[::-1]
  
print(is_palindrome("hello")) # False

# Write a function fibonacci(n) that generates a list containing the first n elements of the fibonacci sequence.

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
  
print(fibonacci(10)) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
