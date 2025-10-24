from datetime import date

class Persona:
    def __init__ (self,
                rut:str,
                nombres:str, 
                apellidos:str, 
                fecha_nacimiento:date,
                cod_area:int, 
                telefono:int
        ):
            self.rut:str = rut
            self.nombres:str = nombres
            self.apellidos:str = apellidos
            self.fecha_nacimiento:date = fecha_nacimiento
            self.cod_area:int = cod_area
            self.telefono:int = telefono

    def __str__ (self):
        return f"{self.rut} {self.nombres} {self.apellidos} {self.fecha_nacimiento} {self.cod_area} {self.telefono}"

personas = []

def persona_existe(persona_nueva: Persona)-> bool:
    for persona in personas:
        if persona.rut == persona_nueva.rut:
            print("Persona existe")
            return True
        print("Persona no existe")
        return False

def create_persona():
    rut: str = input("Ingresa el rut de la persona: ")
    nombres: str = input("Ingresa los nombres de la persona: ")
    apellidos: str = input("Ingresa los apellidos de la persona: ")
    dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
    mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
    anio_nacimiento = int(input("Ingresa el año de nacimiento: "))
    fecha_nacimiento: date = date(
    year = anio_nacimiento,
    month = mes_nacimiento,
    day = dia_nacimiento)
    cod_area: int = input("Ingresa el codigo de area del telefono de la persona: ")
    telefono: int = input("Ingresa el telefono de la persona: ")
    persona = Persona(
        rut=rut,
        nombres=nombres,
        apellidos=apellidos,
        fecha_nacimiento=fecha_nacimiento,
        cod_area=cod_area,
        telefono=telefono
    )

    if persona_existe(persona):
        return print (f"La persona con el rut {persona.rut} ya existe. Intente con otro rut.")
    
    personas.append(persona)
            
def read_persona():
    for persona in personas:
        print(persona)

def upate_persona():
    rut_busqueda = input("Ingrese el rut de la persona a editar: ")
    for persona in personas:
        if persona.rut == rut:
            print(f"""
            ==========================  
            ¿Que datos quiere cambiar
            ==========================
            1. Rut: {persona.rut}
            2. Nombres: {persona.nombres}
            3. Apellidos: {persona.apellidos}
            4. Fecha de nacimiento: {persona.fecha_nacimiento}
            5. Codigo de area: {persona.cod_area}
            6. Telefono: {persona.telefono}
            0. No seguir modificando.
            """
        )

            opcion = input("¿Qué dato quiere cambiar?")

            if opcion == "1":
                    rut: str = input("Ingresa el rut de la persona: ")
                    if persona_existe(persona):
                        print (f"La persona con el rut {persona.rut} ya existe. Ingrese otro rut.")
                        persona.rut = rut 
                        print("Rut modificado exitosamente.")   
            elif opcion == "2":
                nombres: str = input("Ingresa los nombres de la persona: ")
            elif opcion == "3":
                apellidos: str = input("Ingresa los apellidos de la persona: ")
            elif opcion == "4":               
                year = anio_nacimiento = int(input("Ingresa el año de nacimiento."))
                month = mes_nacimiento = int(input("Ingresa el mes de nacimiento."))
                day = dia_nacimiento = int(input("Ingresa el dia de nacimiento."))
            elif opcion == "5":
                cod_area: int = input("Ingresa el codigo de area del telefono de la persona: ")
            elif opcion == "6":
                telefono: int = input("Ingresa el telefono de la persona: ")
            elif opcion == "0":
                break
            else:
                pass

def delete_persona():
    rut_busqueda = input("Ingresa el rut de la persoa para borrar: ")
    for persona in personas:
        if persona.rut == rut_busqueda:
            print (f"Eliminando persona: {persona}")
            personas.remove(persona)
            print (f"Persona con rut {rut_busqueda} eliminada exitosamente.")


print(
    """
    ===================
    Gestor de personas
    ===================
    1. Crear persona
    2. Listar personas
    0. Salir
    """
)
opcion = input("Ingrese una opción [1-2, 0]:    ")
if opcion == "1":
    pass