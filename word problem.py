def valid(email, password):
    if type(email) != str or type(password) != str:
        return "Error: Email or password not a string"
    email.strip
    if '@' not in email:
        return "Error: Not a valid email format"
    capital = False 
    numero = False
    for i in password:
        if i == i.upper():
            capital = True
    for i in password:
        if i.isdigit():
            numero = True
    if capital == False:
        return 'Error: Needs a capital'
    if numero == False:
        return 'Error: Needs a number'
    if len(password) < 8:
        return 'Error: To short'
    return{'email':email, 'password':password}
print(valid('doodoo@babayaga.com',"pAssw0rDelam&ndo"))



                    
