#Abaco grupo4, Awakelab

tablero = { '49': ' |-----|' , '50': '  |-----|' , '51': ' |-----|' , '52': ' |-----|' , '53': ' |-----|' , '54': ' |-----|' , 
            '43': ' |-----|' , '44': '  |-----|' , '45': ' |-----|' , '46': ' |-----|' , '47': ' |-----|' , '48': ' |-----|' , 
            '37': ' |-----| ' , '38': ' |-----|' , '39': ' |-----|' , '40': ' |-----|' , '41': ' |-----|' , '42': ' |-----|' , 
            '31': ' |-----| ' , '32': ' |-----|' , '33': ' |-----|' , '34': ' |-----|' , '35': ' |-----|' , '36': ' |-----|' , 
            '25': ' |-----| ' , '26': ' |-----|' , '27': ' |-----|' , '28': ' |-----|' , '29': ' |-----|' , '30': ' |-----|' , 
            '19': ' |-----| ' , '20': ' |-----|' , '21': ' |-----|' , '22': ' |-----|' , '23': ' |-----|' , '24': ' |-----|',
            '13': ' |-----| ' , '14': ' |-----|' , '15': ' |-----|' , '16': ' |-----|' , '17': ' |-----|' , '18': ' |-----|',
            '7': ' |-----| ' , '8': ' |-----|' , '9': ' |-----|' , '10': ' |-----|' ,'11': ' |-----|' ,'12': ' |-----|',
            '1': ' |-----|' , '2': '  |-----|' , '3': ' |-----|' , '4': ' |-----|' ,'5': ' |-----|' ,'6': ' |-----|'}
#print(tablero)
tablero_play = []
for play in tablero:
    tablero_play.append(play)

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def print_tab_inicial(tab):
    clear()
    print("\n Abaco : \n")
    print(' +----+   +----+   +----+   +---+    +--+     +--+')
    print('|' +tab['49']+"9CM" + '|   ' + '|' +tab['50']+"9DM" + '|   ' + '|' + tab['51']+"9UM" + '|   ' + '|' + tab['52']+"9C" + '|   ' + tab['53']+ '|' "9D" + '|' +tab['54']+ '    ' + '|' "9U" + '|   ' )
    print('|' +tab['43']+"8CM" + '|   ' + '|' +tab['44']+"8DM" + '|   ' + '|' + tab['45']+"8UM" + '|   ' + '|' + tab['46']+"8C" + '|   ' + tab['47']+ '|' "8D" +   '|' +tab['48']+ '    ' + '|' "8U" + '|   ' )
    print('|' +tab['37']+"7CM" + '|   ' + '|' +tab['38']+"7DM" + '|   ' + '|' + tab['39']+"7UM" + '|   ' + '|' + tab['40']+"7C" + '|   ' + tab['41']+ '|' "7D" +   '|' +tab['42']+ '    ' + '|' "7U" + '|   ' )
    print('|' +tab['31']+"6CM" + '|   ' + '|' +tab['32']+"6DM" + '|   ' + '|' + tab['33']+"6UM" + '|   ' + '|' + tab['34']+"6C" + '|   ' + tab['35']+ '|' "6D" + '|'  +tab['36']+ '    ' + '|' "6U" + '|   ' )
    print('|' +tab['25']+"5CM" + '|   ' + '|' +tab['26']+"5DM" + '|   ' + '|' + tab['27']+"5UM" + '|   ' + '|' + tab['28']+"5C" + '|   ' + tab['29']+ '|' "5D" + '|' +tab['30']+ '    ' + '|' "5U" + '|   ' )
    print('|' +tab['19']+"4CM" + '|   ' + '|' +tab['20']+"4DM" + '|   ' + '|' + tab['21']+"4UM" + '|   ' + '|' + tab['22']+"4C" + '|   ' + tab['23']+ '|' "4D" +   '|' +tab['24']+ '    ' + '|' "4U" + '|   ' )
    print('|' +tab['13']+"3CM" + '|   ' + '|' +tab['14']+"3DM" + '|   ' + '|' + tab['15']+"3UM" + '|   ' + '|' + tab['16']+"3C" + '|   ' + tab['17']+ '|' "3D" +   '|' +tab['18']+ '    ' + '|' "3U" + '|   ' )
    print('|' +tab['7']+"2CM" + '|   ' + '|' +tab['8']+"2DM" + '|   ' + '|' + tab['9']+"2UM" + '|   ' + '|' + tab['10']+"2C" + '|   ' + tab['11']+ '|' "2D" + '|'  +tab['12']+ '    ' + '|' "2U" + '|   ' )
    print('|' +tab['1']+"1CM" + '|   ' + '|' +tab['2']+"1DM" + '|   ' + '|' + tab['3']+"1UM" + '|   ' + '|' + tab['4']+"1C" +  '|   ' + tab['5']+ '|' "1D" +   '|' +tab['6']+ '    ' + '|' "1U" + '|   ' )
    print(' +----+   +----+   +----+   +----+   +--+     +--+')
    print('  U.Mi. D.M.     U.M.     Centena    Decena   Unidad')

def printTab(tab):
    print(' +-----+     +-----+    +-----+    +-----+   +-----+   +-----+')
    print(tab['49']+"   "+tab['50']+"   " + tab['51']+"   "+ tab['52']+"  " + tab['53']+ "  "+tab['54'])
    print(tab['43']+"   "+tab['44']+"   " + tab['45']+"   " + tab['46']+"  "+ tab['47']+ "  "+tab['48'])
    print(tab['37']+"   "+tab['38']+"   " + tab['39']+"   " + tab['40']+"  "+ tab['41']+ "  "+tab['42'])
    print(tab['31']+"   "+tab['32']+"   " + tab['33']+"   "+ tab['34']+"  "+ tab['35']+ "  "+tab['36'])
    print(tab['25']+"   "+tab['26']+"   "+ tab['27']+"   " + tab['28']+"  "+ tab['29']+ "  "+tab['30'])
    print(tab['19']+"   "+tab['20']+"   "+ tab['21']+"   " + tab['22']+"  "+ tab['23']+ "  "+tab['24'])
    print(tab['13']+"   "+tab['14']+"   " + tab['15']+"   "+ tab['16']+"  "+ tab['17']+ "  " +tab['18'])
    print(tab['7']+"   "+tab['8']+"   " + tab['9']+"   "+ tab['10']+"  "+ tab['11']+ "  "+tab['12'])
    print(tab['1']+"   "+tab['2']+"   " +tab['3']+"   " + tab['4']+"  "+ tab['5']+ "  "+tab['6'])
    print(' +-----+     +-----+    +-----+    +-----+   +-----+   +-----+')
    print(' U.Mi.         D.M.       U.M.       CEN       DEC       UNI')


print("\n ########BIENVENIDOS AL ABA-WAKE####### \n")

ingreso = input("Ingrese algún número : ")
numero_inicial = int(ingreso)


def agregar_fichas(u,d,c,um,dm,cm):
    cont_uni=6
    cont_dec=5
    cont_cen=4
    cont_um=3
    cont_dm=2
    cont_cm=1

    for i in range(0,unidad):
        tablero[str(cont_uni)] = " XXXXXXX"
        cont_uni = cont_uni+6

    for i in range(0,decena):
        tablero[str(cont_dec)] = " XXXXXXX"
        cont_dec = cont_dec+6

    for i in range(0,centena):
        tablero[str(cont_cen)] = " XXXXXXX"
        cont_cen = cont_cen+6

    for i in range(0,unidad_mil):
        tablero[str(cont_um)] = " XXXXXX"
        cont_um = cont_um+6

    for i in range(0,decena_mil):
        tablero[str(cont_dm)] = " XXXXXXX"
        cont_dm = cont_dm+6

    for i in range(0,centena_mil):
        tablero[str(cont_cm)] = " XXXXXXX "
        cont_cm = cont_cm+6


#Codigo para descomponer el numero ingresado por el usuario
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
#Fin descomposición




agregar_fichas(unidad,decena,centena,unidad_mil,decena_mil,centena_mil)
printTab(tablero)    



def crear_lista(numero_inicial):
    numero_formateado = '{:,}' .format(numero_inicial).replace(',','.')
    return numero_formateado

resultado = crear_lista(numero_inicial)   
print (resultado)