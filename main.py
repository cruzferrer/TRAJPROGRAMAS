def e1():
  sul = float(input("Ingresa el sueldo: "))
  aum = sul * 0.15 if sul < 4000 else sul * 0.08
  sul_aum = sul + aum
  print(f"El sueldo del trabajador es de {sul_aum}")


def e2():
  edad = int(input("ingrese la edad de la persona: "))
  precio_jug = 50
  precio_pagar = precio_jug * 0.75 if edad < 10 else precio_jug
  print(
    f"El cliente {'es un niño y' if edad < 10 else 'no es un niño y'} debe pagar {precio_pagar} soles."
  )


def e3():
  m = input("Ingrese el mes (minúsculas): ")
  im = float(input("Ingrese el importe: "))

  des = 0.15 if m == "octubre" else 0
  im_descuento = im * (1 - des)

  print(
    f"{'Se aplicó un descuento del 15%.'if des > 0 else 'No se aplicó ningún descuento.'} El importe a pagar es:{im_descuento}"
  )


def e4():
  n = int(input("Ingrese un número entero menor a 10: "))

  while n >= 10:
    n = int(input("Ingrese un número válido, menor a 10"))

  print("El número ingresado es:", n)


def e5():
  n = int(input("Ingrese un número entero entre 0 y 20: "))

  while n < 0 or n >= 20:
    n = int(input("Ingrese un número válid, entre 0 y 20: "))

  print("El número ingresado es:", n)


def e6():
  i = 0
  n = int(input("Ingrese un número entero entre 0 y 20: "))
  i += 1

  while n < 0 or n >= 20:
    n = int(input("Ingrese un número válido, entre 0 y 20: "))
    i += 1

  print("El número es:", n)
  print("Se contaron", i, "números.")


def e7():
  n = int(input("Ingrese un número entero positivo: "))
  suma = sum(range(1, n + 1))

  print("La suma de los", n, "primeros números enteros positivos es:", suma)


def e8():
  suma = sum(int(input("Ingrese un número: ")) for _ in iter(input, "0"))

  print("La suma de los números ingresados es:", suma)


def e9():
  s = 0

  while True:
    nee = int(input("Ingrese un número: "))
    s += nee
    if s > 100:

      print("La suma total es:", s)


def e10():
  n = input("Ingrese su nombre: ")
  h_r = float(input("Ingrese cantidad de horas trabajadas: "))
  h_e = float(input("Ingrese cantidad de horas extras trabajadas: "))
  his = int(input("Ingrese cantidad de hijos: "))

  pago_h_n = 10
  pago_h_e = 1.5 * pago_h_n
  monto_h_n = h_r * pago_h_n
  monto_h_e = h_e * pago_h_e
  bonificacion_his = his * 0.5

  pago_to = monto_h_n + monto_h_e + bonificacion_his

  print("Nombre:", n)
  print("Monto por horas normales:", monto_h_n)
  print("Monto por horas extras:", monto_h_e)
  print("Bonificación por hijos:", bonificacion_his)
  print("Pago total:", pago_to)


print("CODIGO DE FERRER PARRA CRUZ RICARDO 4IV9")
print("Elija una opción:")
print("1. Calcular el aumento del sueldo")
print("2. Calcular los precios en el parque de diversiones")
print("3. Calcular el precio con descuento en la tienda")
print("4. Número menor que 10")
print("5. Número entre 0 y 20")
print("6. Número entre 0 y 20 con contador")
print("7. Suma de los primeros números 'n' positivos")
print("8. Suma de los números hasta ingresar '0'")
print("9. Suma superior a 100")
print("10. Pago de trabajador")

opcion = int(input("Opción seleccionada: "))

if opcion == 1:
  e1()
elif opcion == 2:
  e2()
elif opcion == 3:
  e3()
elif opcion == 4:
  e4()
elif opcion == 5:
  e5()
elif opcion == 6:
  e6()
elif opcion == 7:
  e7()
elif opcion == 8:
  e8()
elif opcion == 9:
  e9()
elif opcion == 10:
  e10()
else:
  print("Elija una opción entre 1 y 10: ")
