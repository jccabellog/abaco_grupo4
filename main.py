import abaco as a

print("\n ######## BIENVENIDOS AL ABA-WAKE ####### \n")
lista=[]
i=0
res=""
while res !="SALIR":
    ingreso = input("Ingrese algún número : ")
    a.abaco(ingreso)
    lista_final = a.crear_lista(ingreso)
    res1=input("Si desea terminar la ejecución, escriba salir, de lo contrario presione cualquier tecla :\n")
    res =res1.upper()
print ("Los números ingresados por el usuario son : \n")
for num in lista_final:
    print(num)
