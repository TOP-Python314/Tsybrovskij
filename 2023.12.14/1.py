def strong_password(password):
    up_chars = ''.join(chr(i) for i in range(65,91))
    low_chars = ''.join(chr(i) for i in range(97,123))
    digits = ''.join(str(i) for i in range(10))
    special_chars = '!@#$%^&*()-_=+[]{}|;:\",.<>?/`~'
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    if len(password) < 8:
        return False
    for char in password:
        if char in up_chars:
            has_upper = True
        elif char in low_chars:
            has_lower = True
        elif char in digits:
            has_digit = True
        elif char in special_chars:
            has_special = True
            
    if has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False

password = input('Введите пароль:')
res = strong_password(password)
print(res)

# Примеры:
# Введите пароль:aP3:kD_l3
# True
# Введите пароль:password
# False