#Archivo principal que echa a andar el Aba-wake.




import abaco as a

print("""
 $$$$$$\  $$\                         $$\      $$\           $$\                 
$$  __$$\ $$ |                        $$ | $\  $$ |          $$ |                
$$ /  $$ |$$$$$$$\   $$$$$$\          $$ |$$$\ $$ | $$$$$$\  $$ |  $$\  $$$$$$\  
$$$$$$$$ |$$  __$$\  \____$$\ $$$$$$\ $$ $$ $$\$$ | \____$$\ $$ | $$  |$$  __$$\ 
$$  __$$ |$$ |  $$ | $$$$$$$ |\______|$$$$  _$$$$ | $$$$$$$ |$$$$$$  / $$$$$$$$ |
$$ |  $$ |$$ |  $$ |$$  __$$ |        $$$  / \$$$ |$$  __$$ |$$  _$$<  $$   ____|
$$ |  $$ |$$$$$$$  |\$$$$$$$ |        $$  /   \$$ |\$$$$$$$ |$$ | \$$\ \$$$$$$$\ 
\__|  \__|\_______/  \_______|        \__/     \__| \_______|\__|  \__| \_______|
                                                                                                                                                                                                                                                 
""")
print("""El ábaco es un instrumento de cálculo que podemos encontrar 
en muchas casas o escuelas. Está formado por cuentas de madera, 
metal o piedras que están ensartadas en varias barras de madera o metal, 
fijadas en una base. Cada una de las barras representa las unidades,
las decenas, las centenas, las unidades de millar, las decenas de millar,
las centenas de millar...
Es sin duda, una de las calculadoras más antiguas que conocemos 
y que ha llegado hasta nuestros días.""")
print("""Hoy te traemos el Aba-wake digital para que conozcas la forma mas divertida de aprender,
¿Estás preparado?""")
print("""
┌─┐┌─┐┌┬┐┌─┐┌┐┌┌─┐┌─┐┌┬┐┌─┐┌─┐┬
│  │ ││││├┤ ││││  ├┤ ││││ │└─┐│
└─┘└─┘┴ ┴└─┘┘└┘└─┘└─┘┴ ┴└─┘└─┘o
""")
lista=[]
i=0
res=""
print("Recuerda que la práctica hace al maestro, es buena idea que sigas intentando.")
print("""Puedes conocer el numero contando la cantidad de X que hay en cada tabla.
           Te recomiendo seguir intentando para que entiendas bien como funciona este método.""")
while res !="SALIR":
    #utilizamos factores condicionales para indicar al usuario 
    # los pasos a seguir en caso de que quisiera seguir aprendiendo.
    ingreso = input("Ingrese algún número : ")
    a.abaco(ingreso)
    lista_final = a.crear_lista(ingreso)
    res1=input("Si desea terminar la ejecución, escriba salir, de lo contrario presione cualquier tecla :\n")
   
    res =res1.upper()
print ("Los números ingresados por el usuario son : \n")
for num in lista_final:
    print(num)

print("Gracias por jugar y aprender con Aba-Wake.")
print("Recuerda que puedes colaborar con nosotros en https://github.com/jccabellog/abaco_grupo4.git")
print("""
  .-_'''-.   .-------.       ____        _______  .-./`)    ____       .-'''-. .---.  
 '_( )_   \  |  _ _   \    .'  __ `.    /   __  \ \ .-.') .'  __ `.   / _     \\   /  
|(_ o _)|  ' | ( ' )  |   /   '  \  \  | ,_/  \__)/ `-' \/   '  \  \ (`' )/`--'|   |  
. (_,_)/___| |(_ o _) /   |___|  /  |,-./  )       `-'`"`|___|  /  |(_ o _).    \ /   
|  |  .-----.| (_,_).' __    _.-`   |\  '_ '`)     .---.    _.-`   | (_,_). '.   v    
'  \  '-   .'|  |\ \  |  |.'   _    | > (_)  )  __ |   | .'   _    |.---.  \  : _ _   
 \  `-'`   | |  | \ `'   /|  _( )_  |(  .  .-'_/  )|   | |  _( )_  |\    `-'  |(_I_)  
  \        / |  |  \    / \ (_ o _) / `-'`-'     / |   | \ (_ o _) / \       /(_(=)_) 
   `'-...-'  ''-'   `'-'   '.(_,_).'    `._____.'  '---'  '.(_,_).'   `-...-'  (_I_)  
                                                                                      
""")