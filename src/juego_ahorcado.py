import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena: str) -> str:
    """
    Normaliza una cadena de texto realizando las siguientes operaciones:
        - convierte a minúsculas
        - quita espacios en blanco al principio y al final
        - elimina acentos y diéresis        
    
    Parámetros:
      cadena: cadena de texto que hay que sanear
    
    Devuelve:
      Cadena de texto con la palabra normalizada
    """
    cadena = cadena.lower().strip().replace("á","a").replace("ä", "a").replace("é", "e").replace("é", "e").replace("ë", "e").replace("í", "i").replace("ï", "i").replace("ó", "o").replace("ö", "o").replace("ú", "u").replace("ü", "u")
    return cadena




def enmascarar(palabra_secreta, letras_usadas=""):
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    res = ""
    for c in palabra_secreta:
        if c in letras_usadas:
            res += c
        else:
            res += "_"
    return res


def ha_ganado(palabra_enmascarada: str) -> bool:
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 

    Devuelve:
    - True si el jugador ha ganado, False en caso contrario
    '''

    return "_" not in palabra_enmascarada
 

def mostrar_estado(palabra_enmascarada, letras_usadas, intentos_restantes):
    print(f"Estado: {' '.join(palabra_enmascarada)}")
    if letras_usadas == "":
        print("Letras usadas: ninguna")
    else:
        print(f"Letras usadas: {letras_usadas}")
    print(f"Intentos restantes: {intentos_restantes}")

    

def pedir_letra(letras_usadas: str) -> str:
    '''solicita al jugador que introduzca una letra
    y se asegura de que la entrada proporcionada por el
    jugador sea válida
    
    Parámetros:'''
    letra = input("Introduce una letra:").lower()
    while len(letra) != 1 or not letra.isalpha() or letra in letras_usadas:
        print("Solo puedes introducir una letra")
        letra = input("Introduce otra letra, no repitas:").lower()
    

    return letra.lower()     
     
    
def jugar(palabra_secreta, numero_max_intentos = 6):
    palabra_secreta = normalizar(palabra_secreta)

    if palabra_secreta == "":
        return None
    
    
    palabra_enmascarada = enmascarar(palabra_secreta)
    intentos_restantes = numero_max_intentos
    letras_usadas = ""
   
    while intentos_restantes > 0 and not ha_ganado(palabra_enmascarada):
        mostrar_estado(palabra_enmascarada, letras_usadas, intentos_restantes) 
        letra = pedir_letra(letras_usadas)
        letras_usadas += letra 
        if letra not in palabra_secreta:
            print("La letra no está en la palabra")
            intentos_restantes -= 1
        else:
            print("La letra está en la palabra")
            palabra_enmascarada = enmascarar(palabra_secreta, letras_usadas)

    if ha_ganado(palabra_enmascarada):
        print("Enhorabuena, has ganado!")
    else: 
        print(f"Lo siento, has perdido, la palabra secreta era {palabra_secreta}")

palabra_secreta = elige_palabra()
jugar(palabra_secreta)




