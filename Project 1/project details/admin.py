import bcrypt

#creates a hased password for admin.
#So if you try querying for admin's password, it will only give you the hashed password.
password = "123456"
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

print(hashed_password.decode('utf-8')) 
