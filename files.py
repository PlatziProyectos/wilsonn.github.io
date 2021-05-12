def read():
    numbers = []
    with open("./archivos/number.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Facundo", "Miguel", "Pepe", "Christian", "Rocío"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    read() #funcion para leer
    write() #funcion para escribir colocando lo nuevo al final


if __name__ == '__main__':
    run()