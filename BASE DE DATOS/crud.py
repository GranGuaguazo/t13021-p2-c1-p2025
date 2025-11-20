import oracledb
import os
from dotenv import load_dotenv
from datetime import datetime
from typing import Optional

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
        print(f"No se pudo crear la tabla: {err} \n {query}")

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


def create_perro(
        id_perro:int,
        nombre:str,
        edad:int,
        historial_vacunas:datetime
):
    sql = (        
        "INSERT INTO PERROS (id_perro, nombre, edad, historial_vacunas)"
        "VALUES (:id_perro, :nombre, :edad, :historial_vacunas)"
    )
    parametros = {
        "id_perro": id_perro,
        "nombre": nombre,
        "edad": edad,
        "historial_vacunas": historial_vacunas
    }

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,parametros)
                print(f"Dato insertado. \n {parametros}")
            conn.commit()
    except oracledb.DatabaseError as e:
        err = e
        print(f"No se pudo insertar el dato: {err} \n {parametros}")
        
        
def create_gato(
        id_gato:int,
        nombre:str,
        edad:int,
        esterilizado:str
):
    sql = (        
        "INSERT INTO GATOS (id_gato, nombre, edad, historial_vacunas)"
        "VALUES (:id_gato, :nombre, :edad, :historial_vacunas)"
    )
    parametros = {
        "id_gato": id_gato,
        "nombre": nombre,
        "edad": edad,
        "esterilizado": esterilizado
    }
    
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,parametros)
                print(f"Dato insertado. \n {parametros}")
            conn.commit()
    except oracledb.DatabaseError as e:
        err = e
        print(f"No se pudo insertar el dato: {err} \n {parametros}")


def create_ave(
        id_ave:int,
        nombre:str,
        edad:int,
        control_vuelo:str,
        tipo_jaula:str
):
    sql = (
        "INSERT INTO AVES (id_ave, nombre, edad, control_vuelo, tipo_jaula)"
        "VALUES (:id_ave, :nombre, :edad, :control_vuelo, :tipo_jaula)"
    )
    parametros = {
        "id_ave": id_ave,
        "nombre": nombre,
        "edad": edad,
        "control_vuelo": control_vuelo,
        "tipo_jaula": tipo_jaula
    }

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,parametros)
                print(f"Dato insertado. \n {parametros}")
            conn.commit()
    except oracledb.DatabaseError as e:
        err = e
        print(f"No se pudo insertar el dato: {err} \n {parametros}")


def create_HMedico(
        id_historial:int,
        observaciones:str,
        tratamientos:str
):
    sql = (
        "INSERT INTO HISTORIAL_MEDICO (id_historial, observaciones, tratamientos)"
        "VALUES (:id_historial, :observaciones, :tratamientos)"
    )
    parametros = {
        "id_historial": id_historial,
        "observaciones": observaciones,
        "tratamientos": tratamientos       
    }

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,parametros)
                print(f"Dato insertado. \n {parametros}")
            conn.commit()
    except oracledb.DatabaseError as e:
        err = e
        print(f"No se pudo insertar el dato: {err} \n {parametros}")


def create_mascotas(
        id:int,
        especie:str,
        fechaconsulta:datetime,
        idPerro:int,
        idGato:int,
        idAve:int,
):
    sql = (
        "INSERT INTO MASCOTAS (id, especie, fechaconsulta, idPerro, idGato, idAve)"
        "VALUES (:id, :especie, :fechaconsulta, :idPerro, :idGato, :idAve)"
    )
    parametros = {
        "id": id,
        "especie": especie,
        "fechaconsulta" : fechaconsulta,
        "idPerro" : idPerro,
        "idGato" : idGato,
        "idAve" : idAve
    }

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,parametros)
                print(f"Dato insertado. \n {parametros}")
            conn.commit()
    except oracledb.DatabaseError as e:
        err = e
        print(f"No se pudo insertar el dato: {err} \n {parametros}")


def read_perro():
    sql = (
        "SELECT * FROM PERROS"
    )

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql)
                print(f"Consulta a la tabla PERROS")
                for row in resultados:
                    print(row)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al mostrar datos: {err}")

def read_perro_by_id(id):
    sql = (
        "SELECT * FROM PERROS WHERE id = :id_perro"
    )

    parametros = {"id_perro": id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql,parametros)
                print(f"Consulta a la tabla PERROS")
                for row in resultados:
                    print(row)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al mostrar datos: {err}")

def read_gato():
    sql = (
        "SELECT * FROM GATOS"
    )

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql)
                print(f"Consulta a la tabla GATOS")
                for row in resultados:
                    print(row)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al mostrar datos: {err}")

def read_gato_by_id(id):
    sql = (
        "SELECT * FROM GATOS WHERE id = :id_gato"
    )

    parametros = {"id_gato": id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql,parametros)
                print(f"Consulta a la tabla GATOS")
                for row in resultados:
                    print(row)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al mostrar datos: {err}")

def read_ave():
    sql = (
        "SELECT * FROM AVES"
    )

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql)
                print(f"Consulta a la tabla AVES")
                for row in resultados:
                    print(row)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al mostrar datos: {err}")

def read_ave_by_id(id):
    sql = (
        "SELECT * FROM AVES WHERE id = :id_ave"
    )

    parametros = {"id_ave": id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql,parametros)
                print(f"Consulta a la tabla AVES")
                for row in resultados:
                    print(row)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al mostrar datos: {err}")

def read_HMedico():
    sql = (
        "SELECT * FROM HMEDICO"
    )

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql)
                print(f"Consulta a la tabla HISTORIAL MEDICO")
                for row in resultados:
                    print(row)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al mostrar datos: {err}")

def read_HMedico_by_id(id):
    sql = (
        "SELECT * FROM GATOS WHERE id = :id_historial"
    )

    parametros = {"id_historial": id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql,parametros)
                print(f"Consulta a la tabla GATOS")
                for row in resultados:
                    print(row)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al mostrar datos: {err}")

def read_mascota():
    sql = (
        "SELECT * FROM MASCOTAS"
    )

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql)
                print(f"Consulta a la tabla MASCOTAS")
                for row in resultados:
                    print(row)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al mostrar datos: {err}")

def read_mascota_by_id(id):
    sql = (
        "SELECT * FROM MASCOTAS WHERE id = :id"
    )

    parametros = {"id": id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql,parametros)
                print(f"Consulta a la tabla MASCOTAS")
                for row in resultados:
                    print(row)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al mostrar datos: {err}")

def update_perros(id_perro, nombre: Optional[str], edad: Optional[int], historial_vacunas:Optional[str]):
    sets = []
    binds = {"id_perro": id_perro}

    if nombre is not None:         
        sets.append("nombre =: nombre")         
        binds["nombre"] = nombre   
    if edad is not None:         
        sets.append("edad =: edad")         
        binds["edad"] = edad   
    if historial_vacunas is not None:         
        sets.append("historial_vacunas =: historial_vacunas")         
        binds["historial_vacunas"] = datetime.strptime(historial_vacunas, "%Y-%m-%d")       
    if not sets:         
        print("No hay campos para actualizar.")         
        return      
    sql = f"UPDATE PERROS SET {", ".join(sets)} WHERE id_perro =: id_perro"      
    with get_connection() as conn:         
        with conn.cursor() as cur:             
            cur.execute(sql, binds)             
            conn.commit()             
        print(f"Perro con id={id_perro} actualizada.") 


update_perros(
    id_perro=1,
    nombre="Gaston",
    edad=5,
    historial_vacunas="2025-01-02")