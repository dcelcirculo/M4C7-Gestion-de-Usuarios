# Proyecto: Gestión de Usuarios

## Objetivo

Crear una aplicación que permita registrar, consultar y validar usuarios almacenados en archivos de texto, aplicando buenas prácticas de validación y manejo de errores.

---

## Requerimientos

### 1. Registrar usuarios ✅

- [x] Id automático
- [x] Nombre
- [x] Edad
- [x] Fecha de registro automática
- [x] Evitar usuarios duplicados

### 2. Buscar usuarios ✅

- [x] Buscar usuarios por nombre

### 3. Mostrar usuarios registrados ✅

- [x] Listar todos los usuarios almacenados

### 4. Validar archivo al momento de leerlo ✅

Validaciones implementadas:

- [x] Nombres vacíos
- [x] Edades negativas
- [x] Edades no numéricas
- [x] Edades mayores a 120 años
- [x] Usuarios duplicados

### 5. Crear archivo de errores ✅

Separación de registros válidos e inválidos:

- [x] `usuarios_limpios.txt`
- [x] `usuarios_errores.txt`

### Persistencia de datos ✅

- [x] Guardar información en archivos `.txt`

### Experiencia de usuario ✅

- [x] Mostrar mensajes amigables
- [x] Capturar y manejar errores

---

## Formato del archivo

```txt
Id,Nombre,Edad,Fecha_Registro
1,Carlos,25,2024-06-01 12:00:00
2,Ana,30,2024-06-01 12:05:00
3,Pedro,22,2024-06-01 12:10:00
```

---

## Archivos generados

### usuarios.txt

Contiene todos los usuarios registrados correctamente.

### usuarios_limpios.txt

Contiene únicamente los registros válidos encontrados durante la validación.

### usuarios_errores.txt

Contiene los registros inválidos junto con la descripción del error encontrado.

---

## Estado del proyecto

**Completado:** 100% ✅

| Funcionalidad | Estado |
|--------------|---------|
| Registrar usuarios | ✅ |
| Buscar usuarios | ✅ |
| Mostrar usuarios | ✅ |
| Validar archivo | ✅ |
| Detectar duplicados | ✅ |
| Generar archivo de errores | ✅ |
| Generar archivo limpio | ✅ |
| Persistencia en TXT | ✅ |
| Manejo de errores | ✅ |
| Mensajes amigables | ✅ |