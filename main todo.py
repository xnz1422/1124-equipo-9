# 1- Dado un string, escribir una funcion que cambie todos los espacios por guiones.
def reemplazar_espacios(cad): return cad.replace(' ', '-')
print(reemplazar_espacios('Probando reemplazo de espacios'))

# 2- Cambiar Mayusculas por Minusculas. (Ejemplo: "Hola Mundo" -> "hOLA mUNDO"). Tiene como limite 100 caracteres.
def maymin(str1):
    str2 = ''
    limite = 100
    for i in str1[:limite]:
        if i.isupper(): str2 += i.lower()
        elif i.islower(): str2 += i.upper()
        else: str2 += i
    #str2 += str1[limite:]
    return str2

print(maymin('ConvirtiendO MaYúsculas en Minúsculas y viceversa! (012.345,6)'))

# 3- Los strings son inmutables, escribir una funcion que reciba un string, un indice y una letra a modificar de ese string y que devuelve el string modificado.
def reemplazar_caracter(st, ind, car): return st[:ind] + car + st[ind+1:]
print(reemplazar_caracter('abcdef', 3, 'z'))

# 4- Escribir una funcion que reciba un string con nombre y apellido y devuelva un string con el nombre y apellido pero con capitalizacion(primera letra mayuscula).
def capitalizar(cad): return cad.title()
print(capitalizar('fAbian garcia'))

# 5- Escribir una funcion que reciba N numeros, los cuales representan la puntuacion de un concurso, y esta devuelve la puntuacion del subcampeon. (ejemplo de ingreso de datos... [2,6,10,10,7,5,6], debe devolver 7)
def subcampeon(puntos): return list(set(puntos))[-2]
print(subcampeon([2, 6, 10, 10, 7, 5, 6]))

# a- Escribir una funcion que recibe un numero entero y imprima por salida estandar(usando print) un triangulo de numeros de altura igual al numero ingresado.
def triangulo_old(altura):
    for i in range(1, altura+1):
        cad = ''
        for j in range(1, i+1):
            cad += str(i)
        print(cad)

triangulo_old(5)

def triangulo(altura):
    for i in range(1, altura+1):
        for j in range(1, i+1):
            print(i,end='')
        print()

triangulo(5)

# b- Escribir una funcion que reciba un string(el cual representara el nombre de una empresa) y devuelve por salida estandar(usando print) los 3 caracteres mas usados en un orden descendiente.
def mas_usados(cad):
    cad = cad.lower()
    dic = {}
    for i in cad:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for i in range(3):
        print(dic[i][0],dic[i][1])

mas_usados('Cuenta letras')
