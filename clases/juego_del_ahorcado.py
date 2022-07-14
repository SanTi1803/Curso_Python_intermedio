#Random:permite obtener distintos numeros o letras de modo aleatorio. 
import random
#Time: provee funciones relacionadas con el tiempo.
import time
#Os:provee funciones para interactuar con el sistema operativo:
import os

def read_data(filepath = "./archivos/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
        return  words


def run():
    print ("Juego del ahorcado:")
    time.sleep(1)
    print ("El objetivo del juego es adivinar la palabra secreta.")
    print ("Tienes 10 vidas. Pierdes una vida cada que te equivocas.")
    time.sleep(2)

#Selecciono una palabra random de la otra función y con
#random.choice el programa elige una palabra al azar.
    data = read_data(filepath = "./archivos/data.txt")
    palabra_secreta = random.choice(data)

#defino las vidas
    vidas = 10
    lista_palabras_adivinadas = []
#almaceno las palabras adivinadas en una lista vacia
    print("_" * len(palabra_secreta))
#len: Devuelve el número de caracteres.

    while True:
        guesses_word = input("Ingresa una letra: ").strip().upper()
        #.strip: elimina los caracteres vacios
        #.upper: convierte las letras en mayúsculas.
        #.isnumeric: Comprueba si todos los caracteres son numericos o no (True or False)


        if(guesses_word.isnumeric()):
            print("Por favor, ingrese una letra.")
        else:
            if guesses_word.upper() in lista_palabras_adivinadas:
                print("Ya intentaste con esa letra, intenta con otra.")
            else:
                lista_palabras_adivinadas.append(guesses_word)
                if guesses_word.upper() in palabra_secreta:
                    print("Felicidades, adivinaste una letra!")
                    
                else:
                    vidas -= 1
                    print("Te haz equivocado de letra.")
                    print("Tienes " + str(vidas) + " vidas")       
                
            if vidas == 0:
                print("Perdiste!, te quedaste sin vidas")
                break

            estado_actual = ""
            palabra_errada = 0
            for words in palabra_secreta:
                if words in lista_palabras_adivinadas:
                    estado_actual += words
                else:
                    estado_actual += "_"
                    palabra_errada += 1
            print(estado_actual)

            if palabra_errada == 0:
                print("Felicidades, adivinaste la palabra!!")
                print("La palabra secreta es: " + palabra_secreta)
                break   


if __name__ == "__main__":
    run()