def validate_password(password): 
    errors = [] 
    if len(password) < 8: 
        errors.append("Password must be at least 8 characters long.") 
    if not any(ch.isupper() for ch in password): 
        errors.append("Password must contain at least one uppercase letter.") 
    if not any(ch.islower() for ch in password): 
        errors.append("Password must contain at least one lowercase letter.") 
    if not any(ch.isdigit() for ch in password): 
        errors.append("Password must contain at least one digit.") 
    special_chars = "!@#$%^&*" 
    if not any(ch in special_chars for ch in password): 
        errors.append("Password must contain at least one special character (!@#$%^&*).") 
    return { 'is_valid': len(errors) == 0, 'errors': errors } 

print(validate_password("weak")) 
print(validate_password("Weak123")) 
print(validate_password("MySecure@1"))