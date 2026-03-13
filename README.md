# 📦 Gestión de Inventario

Programa de consola en Python que gestiona el inventario de productos, validando las entradas numéricas y calculando el costo total por producto.

---

## 📋 Descripción

El programa guía al usuario a ingresar el nombre, precio y cantidad de un producto. Valida que el precio y la cantidad sean valores numéricos y mayores a cero mediante bucles con manejo de excepciones. Finalmente, calcula el costo total y muestra un resumen formateado.

---

## ⚙️ Requisitos

- Python 3.x

No requiere librerías externas.

---

## 🚀 Uso

Ejecuta el script desde la terminal:

```bash
python inventario.py
```

El programa solicitará los siguientes datos de forma interactiva:

| Campo    | Tipo    | Descripción                  |
|----------|---------|------------------------------|
| Nombre   | Texto   | Nombre del producto          |
| Precio   | Decimal | Precio unitario del producto |
| Cantidad | Entero  | Cantidad de unidades         |

---

## 💡 Ejemplo de ejecución

```
Ingrese el nombre del producto: Arroz
Ingrese el precio del producto: $2.500
Ingrese la cantidad del producto: 4

Producto: Arroz | Precio: $2.500 | Cantidad: 4 | Total: $10.000
```

---

## 🔒 Validación de datos

El programa aplica dos validaciones independientes, una para el precio y otra para la cantidad. Cada una verifica dos condiciones:

1. Que el valor ingresado sea numérico. Si no lo es, muestra un error y vuelve a solicitarlo:

```
Ingrese el precio del producto: $abc
Error: Ingresar solo valores numericos
Ingrese el precio del producto: $
```

2. Que el valor sea mayor a cero. Si es negativo o cero, muestra un error y vuelve a solicitarlo:

```
Ingrese el precio del producto: $-5
Error: Ingrese un valor valido.
Ingrese el precio del producto: $
```

El bucle se repite hasta que se ingresen valores válidos en ambos campos.

---

## 📊 Diagrama de Flujo

![Diagrama de flujo](docs/diagramagestioninventario.png)

---

## 🧠 Lógica del programa

```
1. Solicitar nombre del producto
2. Repetir hasta obtener un precio válido:
   a. Solicitar precio (float)
   b. Si no es numérico → mostrar error y reintentar
   c. Si es menor o igual a cero → mostrar error y reintentar
3. Repetir hasta obtener una cantidad válida:
   a. Solicitar cantidad (int)
   b. Si no es numérica → mostrar error y reintentar
   c. Si es menor o igual a cero → mostrar error y reintentar
4. Calcular: costo_total = precio × cantidad
5. Mostrar resumen formateado
```

---

## 📁 Estructura del proyecto

```
proyecto/
├── docs/
│   └── diagramagestioninventario.png  # Diagrama de flujo del programa
├── .gitignore
├── inventario.py                      # Script principal
├── LICENSE
└── README.md
```

---

## 👤 Autor

Edgar Corzo, Dylan Castillo, Jefferson Cacerez.