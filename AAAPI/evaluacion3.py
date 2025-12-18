import bcrypt
import requests
from datetime import datetime
from dotenv import load_dotenv
import os
import oracledb
import sys



load_dotenv()

ORACLE_USER = os.getenv("ORACLE_USER")
ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD")
ORACLE_DSN = os.getenv("ORACLE_DSN")

class SeguridadAuth:
    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def verify_password(password: str, hash_guardado: str) -> bool:
        try:
            return bcrypt.checkpw(password.encode('utf-8'), hash_guardado.encode('utf-8'))
        except:
            return False

class IndicadorEconomico:
    def __init__(self, nombre, valor, fecha, origen="mindicador.cl"):
        self.nombre = nombre
        self.valor = valor
        self.fecha_valor = fecha
        self.fecha_consulta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.origen = origen

class ServicioIndicadores:
    BASE_URL = "https://mindicador.cl/api"
    CODIGOS = {"UF": "uf", "IVP": "ivp", "IPC": "ipc", "UTM": "utm", "Dolar": "dolar", "Euro": "euro"}
    def consultar(self, indicador: str, fecha_str: str):
        codigo = self.CODIGOS.get(indicador)
        if not codigo: return None
        url = f"{self.BASE_URL}/{codigo}/{fecha_str}"
    
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if not data.get('serie'): return None

            valor = data['serie'][0]['valor']
            fecha = data['serie'][0]['fecha'][:10]

            return IndicadorEconomico(indicador, valor, fecha)

        except requests.exceptions.RequestException as e:
            print(f"Error de conexión/API: {e}")

        except Exception as e:
            print(f"Error de procesamiento: {e}")

        return None


class GestorBD:
    def __init__(self, user, pwd, dsn):
        self.conn = None
        try:
            print(f"Conectando a Oracle DSN: {dsn}...")
            self.conn = oracledb.connect(user=user, password=pwd, dsn=dsn)
            print("Conexión a Oracle establecida.")
        except oracledb.Error as e:
            print(f"Error al conectar a la base de datos de Oracle: {e}")
            sys.exit(1)

       

    def buscar_usuario(self, username):
        if not self.conn: 
            return None
        cursor = self.conn.cursor()
        sql = "SELECT USUARIO, PASSWORD_HASH, ROL FROM USUARIOS WHERE USUARIO = :usuario"
        try:
            cursor.execute(sql, [username])
            return cursor.fetchone()
        except oracledb.Error as e:
            print(f"Error al buscar usuario en DB: {e}")
            return None
        finally:
            cursor.close()

    def log_indicador(self, indicador: IndicadorEconomico, usuario: str):
        if not self.conn: return
        cursor = self.conn.cursor()
        consulta = """
            INSERT INTO LOG_INDICADORES
            (INDICADOR, VALOR, FECHA_VALOR, FECHA_CONSULTA, USUARIO_CONSULTA)
            VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), TO_DATE(:4, 'YYYY-MM-DD HH24:MI:SS'), :5)
        """
        try:
            cursor.execute(consulta, (
                indicador.nombre,
                indicador.valor,
                indicador.fecha_valor,          
                indicador.fecha_consulta,      
                usuario
            ))
            self.conn.commit()
            print(f"\n[LOG ORACLE] El usuario '{usuario}' registró la consulta del {indicador.nombre} ({indicador.valor}) del {indicador.fecha_valor}.")

        except oracledb.Error as e:
            print(f"Error al registrar el log en Oracle: {e}")

            self.conn.rollback()

        finally:
            cursor.close()

class SistemaEcoTech:
    def __init__(self):
        self.db = GestorBD(ORACLE_USER, ORACLE_PASSWORD, ORACLE_DSN)
        self.api = ServicioIndicadores()
        self.usuario_actual = None

    def __autenticar(self):
        print("\n--- AUTENTICACIÓN ---")
        user = input("Usuario: ")
        pwd = input("Contraseña: ")
        data = self.db.buscar_usuario(user)
       
        if data and SeguridadAuth.verify_password(pwd, data[1]):
            self.usuario_actual = {'username': data[0], 'rol': data[2]}
            print(f"ACCESO CONCEDIDO: {data[0]} ({data[2]})\n")
            return True

        else:
            print("USUARIO/CONTRASEÑA INCORRECTA. Intente con un usuario existente en la DB.")
            return False


    def consultar_y_registrar(self):
        print("\n--- CONSULTA DE INDICADORES ---")
        print("Indicadores disponibles:", ", ".join(self.api.CODIGOS.keys()))
        indicador_sel = input("Seleccione indicador (Ej: UF): ").strip().upper()
        fecha_sel = input("Ingrese fecha (DD-MM-YYYY): ").strip()
       
        if indicador_sel not in self.api.CODIGOS:
            print("Indicador no válido.")
            return

        resultado = self.api.consultar(indicador_sel, fecha_sel)
        if resultado:
            print(f"Resultado: {resultado.nombre} = ${resultado.valor:,.2f} el {resultado.fecha_valor}")
            self.db.log_indicador(resultado, self.usuario_actual['username'])

        else:
            print(f"No se pudieron obtener datos para {indicador_sel} en la fecha {fecha_sel}. (Revise la fecha: DD-MM-YYYY)")

    def iniciar(self):
        print("=======================================")
        print("            SISTEMA ECOTECH            ")
        print("=======================================")

        if self.usuario_actual is None:
            if self.__autenticar():
                self.consultar_y_registrar()
       
        print("\n--- FIN DEL PROGRAMA ---")



if __name__ == "__main__":
    sistema = SistemaEcoTech()
    sistema.iniciar()