import random
import os

CARACTER_VACIO = ""
CARACTER_ESPACIO = " "
CARACTER_SALTO_LINEA = "\n"
CARACTER_SUBGUION = "_"
CARACTER_GUION = "-"
CARACTER_PALOTE = "|"
CARACTER_DIVISION = "/"
CARACTER_BACKSLASH = "\\"
MAX_INTENTOS = 6

def read():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line)
    return words

def draw(error):
    fila = CARACTER_VACIO
    for i in range(1,21):
        fila += CARACTER_SUBGUION

    columna = CARACTER_VACIO    
    for j in range(1,10):
        columna += CARACTER_PALOTE

        if error >= 1 :
            if j <= 4 : 
                for i in range(1, (6-j)):
                    columna += CARACTER_ESPACIO
                columna += CARACTER_DIVISION 

        if error >= 2 :
            if j == 1 : 
                for i in range(1, 4):
                    columna += CARACTER_ESPACIO
                columna += CARACTER_PALOTE
        
        if error >= 3 :
            if j == 2 : 
                for i in range(1, 5):
                    columna += CARACTER_ESPACIO
                columna += CARACTER_GUION
            if j == 3 : 
                for i in range(1, 5):
                    columna += CARACTER_ESPACIO
                columna += CARACTER_PALOTE + CARACTER_ESPACIO + CARACTER_PALOTE
            if j == 4 : 
                for i in range(1, 7):
                    columna += CARACTER_ESPACIO
                columna += CARACTER_GUION

        
        if j == 5 :
            if error == 4: 
                for i in range(1, 9):
                    columna += CARACTER_ESPACIO
                columna += CARACTER_PALOTE
            if error >= 5 : 
                for i in range(1, 8):
                    columna += CARACTER_ESPACIO
                columna += CARACTER_DIVISION + CARACTER_PALOTE + CARACTER_BACKSLASH
        
        if j == 6 :
            if error >= 4 : 
                for i in range(1, 9):
                    columna += CARACTER_ESPACIO
                columna += CARACTER_PALOTE

        if error >= 6 :
            if j == 7 :
                for i in range(1, 8):
                    columna += CARACTER_ESPACIO
                columna += CARACTER_DIVISION + CARACTER_ESPACIO + CARACTER_BACKSLASH
        
        columna += CARACTER_SALTO_LINEA
    
    print(fila)
    print(columna)

def run():
    words = read()
    index = random.randint(0, (len(words)-1))
    word = words[index]
    win = False
    leter = CARACTER_VACIO
    leters = []
    intentos = 0

    while win == False:
        word_mask = CARACTER_VACIO
        if len(leter) == 1 and leter.isalpha() and leter != CARACTER_VACIO and leters.count(leter) == 0:
            leters.append(leter)

        for i in word:
            if i != CARACTER_SALTO_LINEA:
                if leters.count(i) == 0 :
                    word_mask += CARACTER_SUBGUION + CARACTER_ESPACIO
                else :
                    word_mask += i + CARACTER_ESPACIO

        if leter != CARACTER_VACIO and word_mask.count(leter) == 0 :
            intentos += 1 

        os.system("clear")
        draw(intentos)
        if word_mask.count(CARACTER_SUBGUION) > 0 :
            if intentos == MAX_INTENTOS:
                print("Perdiste!!!!!!!!!, la palabra era: " + word)
                win = True
            else:    
                print("Adivina la palabra: " + word_mask)
                leter = input("Ingresa una letra: ")
        else:
            print("Ganaste!!!!!!, la palabra es: " + word_mask)
            win = True

if __name__ == '__main__':
    run()