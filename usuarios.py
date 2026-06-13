import datetime

ARCHIVO = "usuarios.txt"
cabecera = ["Id", "Nombre", "Edad", "Fecha de Registro", "Comentarios"]

def menu():
    return """

    === SISTEMA DE USUARIOS ===
    1. Registrar usuario
    2. Buscar usuarios
    3. Mostrar usuarios registrados
    4. Validar un archivo
    5. Crear archivo de errores
    0. Terminar
"""

def validaciones_nombre(nombre):
    # Validación para evitar nombres vacíos
    if nombre == "":
        print("El nombre no puede estar vacio.")
        return False
    return True

def validaciones_edad(edad_texto):
    # Validación para evitar vacios o espacios en blanco en la edad
    if edad_texto == "":
        print("La edad no puede estar vacía.")
        return False
    try:
        edad = int(edad_texto)
    except ValueError:
        print("Error: La edad debe ser un número válido.")
        return False

    # Validación para edades negativas, no numéricas o mayores a 120
    if edad <= 0 or edad > 120:
        print("La edad no puede ser negativa, cero o mayor a 120.")
        return False
    return True

def validacion_duplicados(nombre, nombre_archivo):
    try:
        # Validación para evitar usuarios duplicados
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            next(archivo)  # Saltar la cabecera
            for linea in archivo:
                dato = linea.split(",")
                nombre_registro = dato[1].strip()
                if nombre_registro.lower() == nombre.lower():
                    print("Error: El usuario ya existe.")
                    return False
        
    except FileNotFoundError:
        return True  # Si el archivo no existe, no hay usuarios registrados, por lo que no hay duplicados, se devuelve True para permitir registrar el nuevo usuario.
    except PermissionError:
        print("Error: No tiene permiso para acceder al archivo.")
        return False  # Si no se tiene permiso para acceder al archivo, se devuelve False para evitar registrar un usuario potencialmente duplicado sin una verificación adecuada.
    except Exception as error:
        print(f"Error inesperado: {error}") # Si ocurre un error inesperado al verificar duplicados, se asume que no se pudo realizar la validación correctamente, por lo que se devuelve False para evitar registrar un usuario potencialmente duplicado sin una verificación adecuada.
        return False

    return True

def validacion_archivo_vacio(nombre_archivo):
    # Validación para evitar archivos vacíos o con solo la cabecera
    try:
        with open(nombre_archivo, "r", encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            if len(lineas) <= 1:  # Solo la cabecera o el archivo está vacío
                print("No hay usuarios registrados.")
                return False
            return lineas
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
        return False
    except PermissionError:
        print("Error: No tiene permiso para acceder al archivo.")
        return False
    except Exception as error:
        print(f"Error inesperado: {error}")
        return False

def siguiente_id(nombre_archivo):
    try:
        # Validación para obtener el siguiente ID disponible, considerando que el archivo puede estar vacío o solo contener la cabecera
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            if len(lineas) <= 1:  # Solo la cabecera o el archivo está vacío
                return 1
            ultimo_id = int(lineas[-1].split(",")[0])  # Obtener el último ID registrado
            return ultimo_id + 1
    except FileNotFoundError:
        return 1  # Si el archivo no existe, el primer ID será 1
    except PermissionError:
        print("Error: No tiene permiso para acceder al archivo.")
        return None
    except Exception as error:
        print(f"Error al obtener el siguiente ID: {error}") # Si ocurre un error inesperado al obtener el siguiente ID, se devuelve None para indicar que no se pudo obtener un ID válido.
        return None
    

# FUNCIONES DEL MENU:

def registrar_usuario():
    nombre = input("Ingrese el nombre del usuario: ").strip()
    edad_texto = input("Ingrese la edad del usuario: ").strip()      
    
    if validaciones_nombre(nombre) and validaciones_edad(edad_texto): # Validar el nombre y la edad antes de intentar registrar al usuario
        edad = int(edad_texto) # Convertir la edad a entero después de validar que es un número válido
        
        if validacion_duplicados(nombre, ARCHIVO): # Validar que el usuario no sea duplicado antes de intentar registrar al usuario
            try:          
                with open(ARCHIVO, 'a', encoding='utf-8') as archivo:
                    if archivo.tell() == 0:  # Verificar si el archivo está vacío
                        archivo.write(
                            cabecera[0] + " ," +
                            cabecera[1] + " ," +
                            cabecera[2] + " ," +
                            cabecera[3] + " ," +
                            cabecera[4] + "\n"
                        )  # Escribir la cabecera si el archivo está vacío
                    
                    archivo.write(
                        f"{siguiente_id(ARCHIVO)}, {nombre}, {edad}, {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, \n"
                    ) # Escribir el nuevo usuario con el formato esperado (ID, Nombre, Edad, Fecha de Registro, Comentarios)
                
                print("Usuario registrado exitosamente.")
            except PermissionError:
                print("Error: No tiene permiso para acceder al archivo.")
            except Exception as error:
                print(f"Error inesperado: {error}")

def buscar_usuario():
    # Validación para evitar búsquedas con nombres vacíos o solo espacios en blanco
    usuario_buscado = input("Ingrese el nombre del usuario a buscar: ").strip().lower()
    if not usuario_buscado: # Si el nombre ingresado está vacío después de eliminar espacios en blanco, se muestra un mensaje de error y se detiene la función de búsqueda para evitar realizar una búsqueda con un nombre no válido.
        print("Error: El nombre del usuario no puede estar vacío.")
        return
    encontrado = False
    try:
        with open(ARCHIVO, "r", encoding='utf-8') as archivo: #
            next(archivo)  # Saltar la cabecera
            for linea in archivo: 
                dato = linea.split(",")
                nombre_archivo = dato[1].strip()
                if nombre_archivo.lower() == usuario_buscado:
                    print(f"Usuario encontrado: \n")
                    print(f"Id: {dato[0].strip()}")
                    print(f"Nombre: {dato[1].strip()}")
                    print(f"Edad: {dato[2].strip()}")
                    print(f"Fecha de Registro: {dato[3].strip()}")
                    encontrado = True
                    break
        if not encontrado:
            print("Usuario no encontrado.")
    except FileNotFoundError:
        print("Error: El archivo no se encontró. No hay usuarios registrados.")
    except PermissionError:
        print("Error: No tiene permiso para acceder al archivo.")
    except Exception as error:
        print(f"Error inesperado: {error}")
 
def mostrar_usuarios():
    try:
        lineas = validacion_archivo_vacio(ARCHIVO)
        if lineas:
            print("Ususarios registrados: \n")
            
            for linea in lineas[1:]:  # Saltar la cabecera
                dato = linea.split(",")
                print(f"Id: {dato[0].strip()},\nNombre: {dato[1].strip()},\nEdad: {dato[2].strip()},\nFecha de Registro: {dato[3].strip()}\n")
                
    except FileNotFoundError:
        print("Error: El archivo no se encontró. No hay usuarios registrados.")
    except PermissionError:
        print("Error: No tiene permiso para acceder al archivo.")
    except Exception as error:
        print(f"Error inesperado: {error}")

def validar_archivo():
    archivo_verificar = input("Ingrese el nombre del archivo a validar (con extensión .txt): ").strip()
    archivo_verificar = convertir_archivo(archivo_verificar)  # Convertir el archivo al formato esperado antes de validarlo
    try:
        lineas = validacion_archivo_vacio(archivo_verificar)
        if lineas:
            nombres_vistos = []  # Lista para rastrear nombres ya vistos y detectar duplicados
            for linea in lineas[1:]:  # Saltar la cabecera
                dato = linea.split(",")
                id_usuario = dato[0].strip()
                nombre = dato[1].strip()
                edad = dato[2].strip()
                
                #Validación para evitar usuarios duplicados
                if nombre.lower() in nombres_vistos:
                    print(f"ID {id_usuario}: Nombre duplicado: {nombre}.\n")
                    continue
                else:
                    nombres_vistos.append(nombre.lower())
                
                # Validaciones para nombres vacíos, edades negativas, no numéricas o mayores a 120
                if not validaciones_nombre(nombre):
                    print(f"ID {id_usuario}: Nombre: {nombre}.\n")
                elif not validaciones_edad(edad):
                    print(f"ID {id_usuario}: Edad: {edad}.\n")
                else:
                    print(f"ID {id_usuario}: {nombre} es válido.\n")
                      
                    
        
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
    except PermissionError:
        print("Error: No tiene permiso para acceder al archivo.")
    except Exception as error:
        print(f"Error inesperado: {error}")
        
def convertir_archivo(nombre_archivo):
    lineas = validacion_archivo_vacio(nombre_archivo) # Validar que el archivo no esté vacío antes de intentar convertirlo
    if lineas: # Si el archivo no está vacío, proceder con la conversión
        primera_linea = lineas[0].split(",") # Verificar si la primera línea tiene el formato esperado de la cabecera (Id, Nombre, Edad, Fecha de Registro)
        if len(primera_linea) == 3: # Si la primera línea no tiene el formato esperado, se asume que es necesario convertir el archivo
            with open("archivo_convertido.txt", "w", encoding='utf-8') as archivo_convertido: # Crear un nuevo archivo para escribir los datos convertidos
                archivo_convertido.write( # Escribir la cabecera en el nuevo archivo
                    cabecera[0] + " ," +
                    cabecera[1] + " ," +
                    cabecera[2] + " ," +
                    cabecera[3] + " ," +
                    cabecera[4] + "\n"
                )
                id_usuario = 1  # Asignar un ID secuencial a cada usuario
                for linea in lineas[1:]: # Iterar sobre cada línea del archivo original (excluyendo la cabecera)
                    archivo_convertido.write(f"{id_usuario}, {linea.strip()}, \n") # Escribir cada línea en el nuevo archivo con el formato esperado (ID, Nombre, Edad, Fecha de Registro, Comentarios)
                    id_usuario += 1 # Incrementar el ID para el siguiente usuario
            return "archivo_convertido.txt"  # Devolver el nombre del nuevo archivo convertido para su validación
        else:
            return nombre_archivo  # Si la primera línea ya tiene el formato esperado, no es necesario convertir el archivo, se devuelve el nombre original para su validación
    else:
        return nombre_archivo  # Si el archivo está vacío, se devuelve el nombre original para que la función de validación pueda manejar el caso de archivo vacío
        
def crear_archivo_errores():
    archivo_verificar = input("Ingrese el nombre del archivo a validar (con extensión .txt): ").strip()
    archivo_verificar = convertir_archivo(archivo_verificar)  # Convertir el archivo al formato esperado antes de validarlo
    try:
        lineas = validacion_archivo_vacio(archivo_verificar)
        if lineas:
            nombres_vistos = []  # Lista para rastrear nombres ya vistos y detectar duplicados
            
            # Crear los archivos de salida para datos limpios y errores
            with open("usuarios_limpios.txt", "w", encoding='utf-8') as archivo_limpio, open("usuarios_errores.txt", "w", encoding='utf-8') as archivo_errores:
                archivo_limpio.write(
                    cabecera[0] + " ," +
                    cabecera[1] + " ," +
                    cabecera[2] + " ," +
                    cabecera[3] + " ," +
                    cabecera[4] + "\n"
                )
                archivo_errores.write(
                    cabecera[0] + " ," +
                    cabecera[1] + " ," +
                    cabecera[2] + " ," +
                    cabecera[3] + " ," +
                    cabecera[4] + "\n"
                )
                
                for linea in lineas[1:]:  # Saltar la cabecera
                    dato = linea.split(",")
                    id_usuario = dato[0].strip()
                    nombre = dato[1].strip()
                    edad = dato[2].strip()
                    
                    #Validación para evitar usuarios duplicados
                    if nombre.lower() in nombres_vistos:
                        archivo_errores.write(f"{id_usuario}, {nombre}, {edad}, {dato[3].strip()}, Nombre duplicado\n")                
                        continue                
                    
                    # Validaciones para nombres vacíos, edades negativas, no numéricas o mayores a 120
                    if not validaciones_nombre(nombre):
                        archivo_errores.write(f"{id_usuario}, {nombre}, {edad}, {dato[3].strip()}, Nombre vacío\n")
                    elif not validaciones_edad(edad):
                        archivo_errores.write(f"{id_usuario}, {nombre}, {edad}, {dato[3].strip()}, Edad inválida\n")
                    else:
                        archivo_limpio.write(f"{id_usuario}, {nombre}, {edad}, {dato[3].strip()}, Registro válido\n")
                        nombres_vistos.append(nombre.lower())  
            
            with open("usuarios_limpios.txt", "r", encoding='utf-8') as usuario_limpio, open("usuarios_errores.txt", "r", encoding='utf-8') as usuario_errores:
                lineas_limpias = usuario_limpio.readlines()
                lineas_errores = usuario_errores.readlines()
                print(f"- Registros válidos: {len(lineas_limpias)-1 }\n- Registros con errores: {len(lineas_errores)-1 }\n")
            print(f"\nArchivos 'usuarios_limpios.txt' y 'usuarios_errores.txt' creados exitosamente.\n")
       
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
    except PermissionError:
        print("Error: No tiene permiso para acceder al archivo.")
    except Exception as error:
        print(f"Error inesperado: {error}")

def ejecutar_programa():
     
    while True:
        print(menu())
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            buscar_usuario()
        elif opcion == "3":
            mostrar_usuarios()
        elif opcion == "4":
            validar_archivo()
        elif opcion == "5":
            crear_archivo_errores()
        elif opcion == "0":
            print("Programa terminado.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            
if __name__ == "__main__":
    ejecutar_programa()