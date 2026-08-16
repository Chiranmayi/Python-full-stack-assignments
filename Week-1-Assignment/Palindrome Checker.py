def is_palindrome(text): 
    cleaned = text.replace(" ", "").lower() 
    return cleaned == cleaned[::-1] 

tests = ["level", "Hello", "racecar", "A man a plan a canal Panama"] 

for t in tests: 
    print(is_palindrome(t))