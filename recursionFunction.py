def  fibonnaci(num):
    if num == 0 or num == 1:
        return num
    
    return fibonnaci(num - 2) + fibonnaci(num - 1)

print(fibonnaci(6))

def is_palindrome_number(num):
    # Negative numbers aren't palindromes
    if num < 0:
        return False
    
    original_num = num
    reversed_num = 0
    
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10 # Integer division
        
    return original_num == reversed_num

print(is_palindrome_number(121)) # Output: True
print(is_palindrome_number(1124211)) # Output: True
print(is_palindrome_number(123)) # Output: False
