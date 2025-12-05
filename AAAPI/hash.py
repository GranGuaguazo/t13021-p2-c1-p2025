import oracledb
import os
from dotenv import load_dotenv
import bcrypt

load_dotenv()

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")

def get_connection():
    return oracledb.connect(user=username, password=password, dsn=dsn)

def create_table_users():
    query = (
        "CREATE TABLE USERS("
        "id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,"
        "username VARCHAR(16) NOT NULL UNIQUE"
        "password VARCHAR(64) NOT NULL"
        ")"
    )
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                print(f"Tabla creada. \n {query}")
            conn.commit()
    except oracledb.DatabaseError as e:
        err = e
        print(f"No se pudo crear la tabla: {err} \n {query}")

new_username = input("Ingresa un nombre de usuario: ")
incoming_password = input("Ingresa una contraseña: ").encode("UTF-8")
salt = bcrypt.gensalt(rounds=12)
hashed_password = bcrypt.hashpw(incoming_password, salt)

print(f"Contraseña obtenida: {incoming_password}")
print(f"Contraseña hasheada: {hashed_password}")
print(f"Largo del hash: {len(hashed_password)}")

create_table_users()

query = (
    "INSERT INTO USERS(id, username, password)"
    "VALUES(:id, :username, :password)"
)

parametros = {
    "id"= 1,
    "username" = new_username,
    "password" = password
}

try:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, parametros)
            print(f"Tabla creada. \n {query}")
        conn.commit()
except oracledb.DatabaseError as e:
    err = e
    print(f"No se pudo crear la tabla: {err} \n {query}")