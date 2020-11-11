#Abaco grupo4, Awakelab
print("########BIENVENIDOS AL ABA-WAKE####### \n")
numero_separado = []
ingreso = input("Ingrese algún número (se recomienda utilizar nùmero entero) : ")
numero_inicial = int(ingreso)

centena_mil = numero_inicial//100000
resto = numero_inicial%100000
decena_mil = resto//10000
resto_dec = resto%10000
unidad_mil = resto_dec//1000
resto_mil = resto_dec%1000
centena = resto_mil//100
resto_centena = resto_mil%100
decena = resto_centena//10
unidad = resto_centena%10

print ("el numero es :")
print("unidad: ",unidad)
print("decena: ",decena)
print("centena: ",centena)
print("unidad de mil :",unidad_mil)
print("decena de mil : ",decena_mil)
print("centena de mil : ",centena_mil)

     