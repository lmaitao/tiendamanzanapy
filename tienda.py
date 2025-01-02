#1. Imprima un mensaje, dando la bienvenida al usuario y le preguntará su nombre.

#2. Ahora el usuario deberá ingresar su nombre.

#3. Imprima mensaje, saludando al usuario por su nombre, e indicando que actualmente tiene 20 manzanas disponibles, cada una por un precio de 5 (puede ser peso, euro, dólar, etc).

#4. Imprima un mensaje, preguntando al usuario cuántas manzanas quiere comprar.

#5. Ahora el usuario deberá ingresar cuántas manzanas quiere.

#6. Imprima un mensaje indicando cuántas manzanas compró el usuario, y cuál fue el precio total.

#7. Finalmente que imprima un mensaje indicando cuántas manzanas le quedaron disponibles después de la venta.

print("+++++++++++ Bienvenido +++++++++++++++++")
print("+++++++ A la Tienda de Manzanas ++++++++")
print("+++++++++ De Luis Maita ++++++++++++++++")
print("Ingrese su nombre: ")
nombre = input()
print("Ingrese su Apellido: ")
apellido = input()
print("++++++++++++++++++++++++++++++++++++++++")
print("Bienvenido ", nombre , apellido)
print("Actualmente contamos con 20 manzanas disponibles")
print("+++++++++++++++++++++++++++++++++++++++++")
manzanas_disponibles = int(20)
print("El precio de cada unas es de 5$")
precio_manzana = int(5)
print("cuantas manzanas deseas comprar:")
manzanas_comprar = int (input())
print("+++++++++++++++++++++++++++++++++++++++++")
print("Usted compro: ", manzanas_comprar)
print("El precio a pagar es de: $ ", precio_manzana * manzanas_comprar)
print("Actualmente quedaron la cantidad de manzanas disponibles: ", manzanas_disponibles - manzanas_comprar)

