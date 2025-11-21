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

def create_all_tables():
    tables = [
        (
            "CREATE TABLE PERROS ("
            "id_perro INTEGER PRIMARY KEY,"
            "nombre VARCHAR(60),"
            "edad NUMBER(10),"
            "historial_vacunas VARCHAR(100)"
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
            "tratamientos VARCHAR(200),"
            "fecha_consulta VARCHAR(100),"
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
        historial_vacunas:str
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
        tratamientos:str,
        fechaconsulta:datetime,
        idPerro:int,
        idGato:int,
        idAve:int,
):
    sql = (
        "INSERT INTO HISTORIAL_MEDICO (id_historial, observaciones, tratamientos, fechaconsulta, idPerro, idGato, idAve)"
        "VALUES (:id_historial, :observaciones, :tratamientos, :fechaconsulta, :idPerro, :idGato, :idAve)"
    )
    parametros = {
        "id_historial": id_historial,
        "observaciones": observaciones,
        "tratamientos": tratamientos,
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

def read_perro_by_id(id_perro):
    sql = (
        "SELECT * FROM PERROS WHERE id_perro = :id_perro"
    )

    parametros = {"id_perro": id_perro}

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

def read_gato_by_id(id_gato):
    sql = (
        "SELECT * FROM GATOS WHERE id_gato = :id_gato"
    )

    parametros = {"id_gato": id_gato}

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

def read_ave_by_id(id_ave):
    sql = (
        "SELECT * FROM AVES WHERE id_ave = :id_ave"
    )

    parametros = {"id_ave": id_ave}

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

def read_HMedico_by_id(id_historial):
    sql = (
        "SELECT * FROM GATOS WHERE id_historial = :id_historial"
    )

    parametros = {"id_historial": id_historial}

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
        binds["historial_vacunas"] = historial_vacunas       
    if not sets:         
        print("No hay campos para actualizar.")         
        return      
    sql = f"UPDATE PERROS SET {", ".join(sets)} WHERE id_perro =: id_perro"      
    with get_connection() as conn:         
        with conn.cursor() as cur:             
            cur.execute(sql, binds)             
            conn.commit()             
        print(f"Perro con id={id_perro} actualizada.") 

def update_gatos(id_gato, nombre: Optional[str], edad: Optional[int], esterilizado: Optional[str]):
    sets = []
    binds = {"id_gato": id_gato}

    if nombre is not None:         
        sets.append("nombre =: nombre")         
        binds["nombre"] = nombre   
    if edad is not None:         
        sets.append("edad =: edad")         
        binds["edad"] = edad   
    if esterilizado is not None:         
        sets.append("esterilizado =: esterilizado")         
        binds["esterilizado"] = esterilizado       
    if not sets:         
        print("No hay campos para actualizar.")         
        return      
    sql = f"UPDATE GATOS SET {", ".join(sets)} WHERE id_gato =: id_gato"      
    with get_connection() as conn:         
        with conn.cursor() as cur:             
            cur.execute(sql, binds)             
            conn.commit()             
        print(f"Gato con id={id_gato} actualizada.")

def update_aves(id_ave, nombre: Optional[str], edad: Optional[int], control_vuelo: Optional[str], tipo_jaula: Optional[str]):
    sets = []
    binds = {"id_ave": id_ave}

    if nombre is not None:         
        sets.append("nombre =: nombre")         
        binds["nombre"] = nombre   
    if edad is not None:         
        sets.append("edad =: edad")         
        binds["edad"] = edad   
    if control_vuelo is not None:         
        sets.append("control_vuelo =: control_vuelo")         
        binds["control_vuelo"] = control_vuelo    
    if tipo_jaula is not None:         
        sets.append("tipo_jaula =: tipo_jaula")         
        binds["tipo_jaula"] = tipo_jaula      
    if not sets:         
        print("No hay campos para actualizar.")         
        return      
    sql = f"UPDATE AVES SET {", ".join(sets)} WHERE id_ave =: id_ave"      
    with get_connection() as conn:         
        with conn.cursor() as cur:             
            cur.execute(sql, binds)             
            conn.commit()             
        print(f"Ave con id={id_ave} actualizada.") 

def update_HMedico(id_historial, observaciones: Optional[str], tratamientos: Optional[str], fechaconsulta: Optional[str], idPerro, idGato, idAve):
    sets = []
    binds = {"id_historial": id_historial, "idPerro": idPerro, "idGato": idGato, "idAve": idAve}

    if observaciones is not None:         
        sets.append["observaciones"] = observaciones 
        sets.append =("observaciones =: observaciones")
    if tratamientos is not None:         
        sets.append["tratamientos"] = tratamientos 
        sets.append =("tratamientos =: tratamientos")                  
    if fechaconsulta is not None:         
        sets.append("fecha_consulta =: fecha_consulta")         
        binds["fecha_consulta"] = fechaconsulta
    if not sets:         
        print("No hay campos para actualizar.")         
        return      
    sql = f"UPDATE HMEDICO SET {", ".join(sets)} WHERE id_historial =: id_historial"      
    with get_connection() as conn:         
        with conn.cursor() as cur:             
            cur.execute(sql, binds)             
            conn.commit()             
        print(f"Historial médico con id={id_historial} actualizado")

def delete_perros(id_perro: int):
    sql = (
        "DELETE FROM PERROS WHERE id_perro = :id_perro"
    )

    parametros = {"id_perro": id_perro}
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado. \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_gatos(id_gato: int):
    sql = (
        "DELETE FROM GATOS WHERE id = :id_gato"
    )

    parametros = {"id_gato": id_gato}
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado. \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_aves(id_ave: int):
    sql = (
        "DELETE FROM AVES WHERE id = :id_ave"
    )

    parametros = {"id_ave": id_ave}
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado. \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def delete_historial(id_historial: int):
    sql = (
        "DELETE FROM HISTORIAL_MEDICO WHERE id = :id_historial"
    )

    parametros = {"id_historial": id_historial}
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado. \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")

def menu_perros():
    while True:
        os.system("cls")
        print(
            """
            ╔====================================================╗
            |               MENÚ PERROS                          |
            ======================================================
            |1. CREAR PERRO.                                     |
            |2. LEER PERROS.                                     |
            |3. LEER PERRO POR ID.                               |
            |4. MODIFICAR PERRO.                                 |
            |5. ELIMINAR PERRO.                                  |
            |0. VOLVER AL MENÚ PRINCIPAL.                        |
            ╚====================================================╝
            """
        )
        opcion = input("Selecciona una opción [1-5, 0 para salir]: ")
       
        if opcion == "0":
            os.system("cls")
            print("Adiós")
            input("Presiona ENTER para continuar...")
            break
        elif opcion == "1":
            try:
                id_perro = int(input ("Ingrese el ID del perro: "))
                nombre = input("Ingresa el nombre del Perro: ")
                edad = int(input("Ingresa la edad del perro: "))
                historial_vacunas = input("Ingresa su historial de vacunas (año-mes-dia). Ej: 2025-12-10: ")
                create_perro(id_perro, nombre, edad, historial_vacunas)
            except ValueError:
                print ("Ingresaste un valor no númerico.")            
            input("Presiona ENTER para continuar.")

        elif opcion == "2":
            read_perro()
            input("Presiona ENTER para continuar.")

        elif opcion == "3":
            try:
                id_perro = int(input("Ingrese el id numerico del perro: "))
                read_perro_by_id(id_perro)
            except ValueError:
                print("Ingresaste un valor no númerico")

        elif opcion == "4":
            try:
                id_perro = int(input("Ingrese el id numerico del perro: "))
                print("⚠️ Sólo digite cuándo quiera modificar el dato")
                nombre = input("Ingrese nombre del perro: ")
                edad = input("Ingrese edad del perro: ")
                historial_vacunas = input("Ingresa su historial de vacunas (año-mes-dia). Ej: 2002-12-30: ")
                if len(nombre.strip()) == 0:
                    nombre = None
                if len(edad.strip()) == 0:
                    edad = None
                if len(historial_vacunas.strip()) == 0:
                    historial_vacunas = None
                update_perros(id_perro,nombre,edad,historial_vacunas)
            except ValueError:
                print("Ingresaste un valor no númerico")

            input("Presione ENTER para continuar...")
        elif opcion == "5":
            try:
                id_perro = int(input("Ingrese el id numerico del perro: "))
                delete_perros(id_perro)
            except ValueError:
                print("Ingresaste un valor no númerico")

            input("Presione ENTER para continuar...")
        else:
            print("Opción inválida.")
            input("Presione ENTER para continuar...")
            break


def main():
    while True:
        os.system("cls")
        print(
            """
            ╔====================================================╗
            |               CRUD CON ORACLE SLQ                  |
            ======================================================
            |1. APLICAR ESQUEMA EN LA BASE DE DATOS.             |
            |2. TABLA PERROS.                                    |
            |3. TABLA GATOS.                                     |
            |4. TABLA AVES.                                      |
            |5. TABLA HISTORIAL MÉDICO.                          |
            |0. SALIR.                                           |
            ╚====================================================╝
            """
        )
        opcion = input("Selecciona una opción [1-5, 0 para salir]: ")

        if opcion == "0":
            print("Adiós")
            input("Presiona ENTER para continuar...")
            break
        elif opcion == "1":
            create_all_tables()
        elif opcion == "2":
            menu_perros()
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        else:
            print("Opción inválida.")
            input("Presione ENTER para continuar...")
            break


if __name__ == "__main__":
    main()
