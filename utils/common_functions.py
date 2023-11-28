import bcrypt


def hash_password(password): 
    byte = password.encode('utf-8')
    salt = bcrypt.gensalt() 

    return bcrypt.hashpw(byte, salt)
  


def check_password(password, userPassword):

    byte = password.encode('utf-8') 

    salt = bcrypt.gensalt() 

    hashed = bcrypt.hashpw(byte, salt)  
    userBytes = userPassword.encode('utf-8') 
    print(bcrypt.checkpw(userBytes, hashed))
    return bcrypt.checkpw(userBytes, hashed)

# Taking user entered password  
# userPassword =  'passwordabc'
# hash = bcrypt.hashpw(bytes, salt)
# # encoding user password 
  
# # checking password 
# result = bcrypt.checkpw(userBytes, hash) 