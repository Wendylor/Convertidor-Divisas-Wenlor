#Este programa va convertir pesos Colombianos que el usuario ingrese a Dolares,Yuanes,Euro y pesos Mexicanos


#Ingresamos los valores de cada moneda a pesos colombianos

valor_dolares = 3295.51
valor_euros = 3763.00
valor_yuanes = 484.44
valor_mexicano = 187.84

print("Bienvenido y Bienvenida a Wenlor, convertidor de divisas de pesos colombianos a las siguentes divisas: Dolares,Yuanes,Euros y pesos Mexicanos")
print("ingrese su nombre")
nombre = input()

print("Bienvenido y Bienvenida", nombre)

#Importante que cuando ingreso el valor a cambiar de pesos colombianos, debo hacerlo sin puntos y comas. porque lo toma como un decimal y queda mal la opearacion
print("Por favor ingrese la cantidad de pesos colombianos que desea usted convertir con nuestro programa")
pesos = input()

#Importante que convirtamos el dato str sobre los pesos que el usuario ingresa a dato tipo float o si no, no podemos hacer la division
pesos = float(pesos) 

print(pesos, "pesos colombianos equivalen a:")
print(pesos / valor_dolares, "dolares")
print(pesos / valor_euros, "euros")
print(pesos / valor_yuanes, "yuanes")
print(pesos / valor_mexicano, "pesos mexicanos")

#tenemos el resultado de divisas que el usuario desea cambiar, entonces le agradecemos por probar nuestro programa

print("Gracias por usar nuestro convertidor de divisas")
print("Si desea volver a tener un resultado diferente, solamente cambie el valor a ingresar de pesos colombianos")