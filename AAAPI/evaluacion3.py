import bcrypt
import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
USUARIO_PRUEBA = os.getenv("ORACLE_USER")
PASS_PRUEBA = os.getenv("ORACLE_PASSWORD") 
ROL_PRUEBA = os.getenv("ADMIN_ROLE")
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

class GestorSimulado:
    def __init__(self, user, pwd, rol):
        self.__hash_pass = SeguridadAuth.hash_password(pwd)
        self.usuarios_db = {
            user: {'password_hash': self.__hash_pass, 'rol': rol}
        }
    
    def buscar_usuario(self, username):
        if username in self.usuarios_db:
            data = self.usuarios_db[username]
            return (username, data['password_hash'], data['rol'])
        return None

    def log_indicador(self, indicador, usuario):
        print(f"\n[LOG SIMULADO] El usuario '{usuario}' registró la consulta del {indicador.nombre} ({indicador.valor}) del {indicador.fecha_valor}.")

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
            response = requests.get(url, timeout=5)
            response.raise_for_status() 
            data = response.json()

            if not data.get('serie'): return None
            
            valor = data['serie'][0]['valor']
            fecha = data['serie'][0]['fecha'][:10]
            
            return IndicadorEconomico(indicador, valor, fecha)

        except requests.exceptions.RequestException as e:
            print(f"❌ Error de conexión/API: {e}")
        except Exception as e:
            print(f"❌ Error de procesamiento: {e}")
        return None


class SistemaEcoTech:
    def __init__(self):
        self.db = GestorSimulado(USUARIO_PRUEBA, PASS_PRUEBA, ROL_PRUEBA)
        self.api = ServicioIndicadores()
        self.usuario_actual = None

    def __autenticar(self):
        print("\n--- AUTENTICACIÓN ---")
        user = input("Usuario: ")
        pwd = input("Contraseña: ")
        
        data = self.db.buscar_usuario(user)
        
        if data and SeguridadAuth.verify_password(pwd, data[1]):
            self.usuario_actual = {'username': data[0], 'rol': data[2]}
            print(f"🔑 ACCESO CONCEDIDO: {data[0]} ({data[2]})\n")
            return True
        else:
            print("❌ USUARIO/CONTRASEÑA INCORRECTA.")
            return False

    def consultar_y_registrar(self):
        print("\n--- CONSULTA DE INDICADORES ---")
        
        print("Indicadores disponibles:", ", ".join(self.api.CODIGOS.keys()))
        indicador_sel = input("Seleccione indicador (Ej: UF): ").strip().upper()
        fecha_sel = input("Ingrese fecha (DD-MM-YYYY): ").strip()
        
        if indicador_sel not in self.api.CODIGOS:
            print("❌ Indicador no válido.")
            return

        resultado = self.api.consultar(indicador_sel, fecha_sel)

        if resultado:
            print(f"✅ Resultado: {resultado.nombre} = ${resultado.valor:,.2f} el {resultado.fecha_valor}")
            if input("¿Desea registrar/loggear este dato? (s/n): ").lower() == 's':
                self.db.log_indicador(resultado, self.usuario_actual['username'])
        else:
            print(f"❌ No se pudieron obtener datos para {indicador_sel} en la fecha {fecha_sel}.")

    def iniciar(self):
        print("=======================================")
        print("  SISTEMA ECOTECH - INICIO RÁPIDO")
        print("=======================================")
        
        if self.__autenticar():
            self.consultar_y_registrar()
        
        print("\n--- FIN DEL PROGRAMA ---")

if __name__ == "__main__":
    sistema = SistemaEcoTech()
    sistema.iniciar()