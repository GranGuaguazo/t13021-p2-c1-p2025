import oracledb
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")

def get_connection():
    return oracledb.connect(user=username, password=password, dsn=dsn)


def create_schema(query):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                print(f"Tabla creada. \n {query}")
            conn.commit()
    except oracledb.DatabaseError as e:
        err = e
        print(f"No se pudo crear la tabla: {err}")

tables = [
        (
            "CREATE TABLE PERROS ("
            "id_perro INTEGER PRIMARY KEY,"
            "nombre VARCHAR(60),"
            "edad NUMBER(10),"
            "historial_vacunas DATE"
            ")"
        ),
        (
            "CREATE TABLE GATOS ("
            "id_gato INTEGER PRIMARY KEY,"
            "nombre VARCHAR(60),"
            "edad VARCHAR(10),"
            "esterilizado VARCHAR(1)"
            ")"
        ),
        (
            "CREATE TABLE AVES ("
            "id_ave INTEGER PRIMARY KEY,"
            "nombre VARCHAR(60),"
            "edad NUMBER(10),"
            "control_vuelo VARCHAR(50),"
            "tipo_jaula VARCHAR(50)"
            ")"
        ),
        (
            "CREATE TABLE HISTORIAL_MEDICO ("
            "id_historial INTEGER PRIMARY KEY,"
            "observaciones VARCHAR(100),"
            "tratamientos VARCHAR(200)"
            ")"
        ),
        (
            "CREATE TABLE MASCOTAS ("
            "id INTEGER PRIMARY KEY,"
            "especie VARCHAR(10),"
            "fecha_consulta DATE,"
            "idPerro INTEGER,"
            "idGato INTEGER,"
            "idAve INTEGER,"
            "FOREIGN KEY (idPerro) REFERENCES PERROS (id_perro),"
            "FOREIGN KEY (idGato) REFERENCES GATOS (id_gato),"
            "FOREIGN KEY (idAve) REFERENCES AVES (id_ave)"
            ")"
        )
]

for query in tables:
    create_schema(query)            


#def create_table() -> None:
    #ddl = (
    #"CREATE TABLE personas ("
    #"rut VARCHAR2(50) PRIMARY KEY,"
    #"nombres VARCHAR2(200),"
    #"apellidos VARCHAR2(200),"
    #"fecha_nacimiento DATE,"
    #"cod_area VARCHAR2(20),"
    #"numero_telefono VARCHAR2(50)"
    #")"
    #)
    #try:
    #    with get_connection() as conn:
    #        with conn.cursor() as cur:
    #            cur.execute(ddl)
    #            print("Tabla 'personas' creada.")
    #        conn.commit()
    #except oracledb.DatabaseError as e:
    #    err = e
    #    print(f"No se pudo crear la tabla: {err}")











#create_table()
#def create_persona(rut, nombres, apellidos, fecha_nacimiento, cod_area, numero_telefono):
#    sql = (
#"INSERT INTO personas (rut, nombres, apellidos, fecha_nacimiento, cod_area, numero_telefono) "
#"VALUES (:rut, :nombres, :apellidos, :fecha_nacimiento, :cod_area, :numero_telefono)"
#)
#    if fecha_nacimiento:
#        bind_fecha = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
#    else:
#        bind_fecha = None
#    with get_connection() as conn:
#        with conn.cursor() as cur:
#            cur.execute(sql, {
#        "rut": rut,
#        "nombres": nombres,
#        "apellidos": apellidos,
#        "fecha_nacimiento": bind_fecha,
#        "cod_area": cod_area,
#        "numero_telefono": numero_telefono,
#}
#        )