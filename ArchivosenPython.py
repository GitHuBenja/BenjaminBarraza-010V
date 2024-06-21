secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
num = 0
while num == 0:
    number = int(input("ingrese un numero :"))
    if number == secret_number:
        print("Bien hecho mmuggle, eres libre")
        num = 1      
    else:
       print("mal, estas en un buble")
       num = 0