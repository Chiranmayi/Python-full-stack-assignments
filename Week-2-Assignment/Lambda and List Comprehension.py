numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension
squares = [x * x for x in numbers]

print("Squares:", squares)


# Lambda function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)