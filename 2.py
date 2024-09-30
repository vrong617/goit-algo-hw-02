from collections import deque

def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    d = deque(s)
    
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True
  
test_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(test_string):
    print(f"'{test_string}' is a palindrome.")
else:
    print(f"'{test_string}' is not a palindrome.")
