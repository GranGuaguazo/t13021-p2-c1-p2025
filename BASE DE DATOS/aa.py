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