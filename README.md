# Sistema de Gestión de Usuarios

## Descripción

Aplicación desarrollada en Python para registrar usuarios, validar información y almacenar datos en archivos de texto.

El sistema permite:

- Registrar usuarios.
- Buscar usuarios registrados.
- Mostrar todos los usuarios almacenados.
- Validar archivos de usuarios.
- Detectar errores en los registros.
- Generar archivos separados para registros válidos e inválidos.
- Gestionar la persistencia de la información mediante archivos de texto.

---

## Objetivo

Desarrollar una aplicación que permita:

- Registrar usuarios.
- Validar información.
- Guardar datos en archivos.
- Capturar errores mediante manejo de excepciones.
- Mostrar mensajes amigables al usuario.

---

## Funcionalidades

### 1. Registrar usuario

Permite ingresar:

- Nombre
- Edad

El sistema asigna automáticamente:

- ID
- Fecha de registro

Los datos son almacenados en el archivo:

```text
usuarios.txt
```

---

### 2. Buscar usuario

Permite buscar usuarios por nombre y mostrar:

- ID
- Nombre
- Edad
- Fecha de registro

---

### 3. Mostrar usuarios registrados

Muestra todos los usuarios almacenados en el archivo.

---

### 4. Validar archivo

Permite validar un archivo de usuarios verificando:

- Nombres vacíos.
- Edades vacías.
- Edades no numéricas.
- Edades menores o iguales a cero.
- Edades mayores a 120.
- Usuarios duplicados.

---

### 5. Crear archivo de errores

Genera automáticamente:

```text
usuarios_limpios.txt
usuarios_errores.txt
```

Donde:

- usuarios_limpios.txt contiene los registros válidos.
- usuarios_errores.txt contiene los registros inválidos junto con el motivo del error.

---

## Validaciones Implementadas

### Validación de nombre

- No permite nombres vacíos.

Ejemplo:

```text
Nombre: ""
```

Resultado:

```text
El nombre no puede estar vacío.
```

---

### Validación de edad

- No permite edades vacías.
- No permite edades no numéricas.
- No permite edades menores o iguales a cero.
- No permite edades mayores a 120.

Ejemplos:

```text
Edad: abc
Edad: -10
Edad: 0
Edad: 150
```

---

### Validación de usuarios duplicados

El sistema verifica que no existan usuarios con el mismo nombre.

Ejemplo:

```text
Carlos
Carlos
```

Resultado:

```text
Error: El usuario ya existe.
```

---

### Validación de archivo vacío

Se verifica que el archivo contenga información válida antes de procesarlo.

---

## Estructura del Proyecto

```text
Ejercicio/
│
├── usuarios.py
├── usuarios.txt
├── archivo_convertido.txt
├── usuarios_limpios.txt
├── usuarios_errores.txt
└── README.md
```

---

## Archivos Generados

### usuarios.txt

Archivo principal de almacenamiento.

Formato:

```text
Id,Nombre,Edad,Fecha de Registro,Comentarios
1,Carlos,25,2026-06-13 10:00:00,
2,Ana,30,2026-06-13 10:05:00,
```

---

### archivo_convertido.txt

Archivo generado cuando se detecta un formato diferente al esperado.

---

### usuarios_limpios.txt

Contiene únicamente registros válidos.

---

### usuarios_errores.txt

Contiene registros inválidos junto con la descripción del error detectado.

---

## Manejo de Excepciones

El sistema utiliza bloques:

```python
try:
except:
```

para controlar errores como:

- Archivo no encontrado.
- Conversión inválida de datos.
- Errores inesperados durante la lectura o escritura de archivos.

Ejemplo:

```python
try:
    with open(ARCHIVO, "r") as archivo:
        pass
except FileNotFoundError:
    print("Error: El archivo no se encontró.")
```

---

## Tecnologías Utilizadas

- Python 3
- Manejo de archivos
- Módulo datetime
- Funciones
- Condicionales
- Ciclos
- Manejo de excepciones

---

## Ejemplo de Menú

```text
=== SISTEMA DE USUARIOS ===

1. Registrar usuario
2. Buscar usuarios
3. Mostrar usuarios registrados
4. Validar un archivo
5. Crear archivo de errores
0. Terminar
```

---

## Autor

Carolina Gil

Python Senior con IA - Dev Senior Code

Módulo 4: Manejo de Archivos, Persistencia y Validación