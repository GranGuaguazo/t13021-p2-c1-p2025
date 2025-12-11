import oracledb,  bcrypt, requests, os
from dotenv import load_dotenv

incoming_psw = input("Ingrese su contraseña: ").encode("UTF-8")

salt = bcrypt.gensalt(rounds=12)

hashed_psw = bcrypt.hashpw(incoming_psw, salt)
print(f"Su contraseña hasheada es: {hashed_psw}")

confirmed_psw = input("Ingrese nuevamente su contraseña: ").encode("UTF-8")

if bcrypt.checkpw(confirmed_psw, hashed_psw):
    print("Contraseña correcta.")
else:
    print("Contraseña incorrecta.")