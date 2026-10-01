# 💊 SOLID - Principio O: Open/Closed Principle

## 📚 Descripción del tema

Este proyecto muestra de forma práctica el **principio O de SOLID**, conocido como:

> **Open/Closed Principle (Principio abierto/cerrado)**

Este principio establece que:

**Una clase debe estar abierta para su extensión, pero cerrada para su modificación.**

Esto significa que podemos agregar nuevos comportamientos a un programa sin tener que modificar constantemente el código que ya funciona.

### 🏥 Ejemplo del proyecto

El proyecto utiliza un ejemplo relacionado con un **hospital y medicamentos**.

Tenemos una clase abstracta llamada `Medicamento`, que define el método:

```python
administrar()
```

Después se crean diferentes tipos de medicamentos que heredan de esta clase:

- 💊 `Paracetamol`
- 💉 `Antibiotico`

Cada medicamento implementa su propia versión del método `administrar()`.

De esta forma, si queremos agregar un nuevo medicamento, podemos crear una nueva clase que herede de `Medicamento` sin modificar las clases existentes.

Por ejemplo:

```python
class Ibuprofeno(Medicamento):

    def administrar(self):
        print("Administrando ibuprofeno")
```

Esto permite **extender el programa sin modificar el código existente**, aplicando el principio Open/Closed.

---

## 📁 Estructura del proyecto

```text
SOLID-O/
└── Hospital/
    ├── base/
    │   └── medicamento.py
    │
    ├── medicamentos/
    │   ├── antibiotico.py
    │   └── paracetamol.py
    │
    └── main.py
```

### Archivos principales

- `base/medicamento.py` → Contiene la clase abstracta `Medicamento`.
- `medicamentos/paracetamol.py` → Contiene la clase `Paracetamol`.
- `medicamentos/antibiotico.py` → Contiene la clase `Antibiotico`.
- `main.py` → Ejecuta el ejemplo y administra los medicamentos.

---

## ▶️ Pasos para ejecutar el proyecto

### 1. Clonar o descargar el proyecto

Si el proyecto está en GitHub:

```bash
git clone URL_DEL_REPOSITORIO
```

Después entra en la carpeta del proyecto:

```bash
cd SOLID-O
```

### 2. Entrar en la carpeta `Hospital`

```bash
cd Hospital
```

### 3. Ejecutar el programa

Ejecuta:

```bash
python main.py
```

En algunos sistemas también puede ser necesario utilizar:

```bash
python3 main.py
```

### 4. Resultado esperado

Al ejecutar el programa se mostrará:

```text
Administrando paracetamol
Administrando Antibiotico
```

---

## 🧠 ¿Qué demuestra este ejemplo?

El proyecto demuestra que podemos añadir nuevos medicamentos sin modificar la clase `Medicamento` ni las clases que ya existen.

Por ejemplo, podemos crear:

```text
Medicamento
    │
    ├── Paracetamol
    ├── Antibiotico
    └── Ibuprofeno
```

Cada nueva clase puede implementar su propio comportamiento.

Esto facilita:

- La ampliación del programa.
- El mantenimiento del código.
- La reutilización de las clases.
- La reducción de modificaciones innecesarias.
- La aplicación del principio Open/Closed.

---

## 👩‍💻 Tecnologías utilizadas

- **Python 3**
- Programación orientada a objetos (POO)
- Clases abstractas
- Herencia
- Polimorfismo
- Principios SOLID

---

## 🎯 Objetivo

El objetivo de este ejercicio es comprender de manera práctica el **principio Open/Closed (OCP)** y observar cómo podemos ampliar una aplicación mediante nuevas clases sin modificar el código que ya existe.