import bcrypt

incoming_psw = input("Ingrese su contraseña: ").encode("UTF-8")

salt = bcrypt.gensalt(rounds=12)

hashed_psw = bcrypt.hashpw(incoming_psw, salt)
print(f"Su contraseña hasheada es: {hashed_psw}")