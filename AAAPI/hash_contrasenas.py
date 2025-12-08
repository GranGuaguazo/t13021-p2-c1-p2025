import bcrypt

password = "Inacap#2025" 
hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
print(hash_password)