def separate_even_odd(numbers): 
    even = [] 
    odd = [] 
    for n in numbers: 
        if n % 2 == 0: 
            even.append(n) 
        else: 
            odd.append(n) 
    return even, odd 

even, odd = separate_even_odd([1,2,3,4,5,6,7,8,9,10]) 
print(even) 
print(odd)