def run():
    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    print(squares)

    print("Numeros entre 1 - 999999 divisibles entre 4, 6 y 9")
    mod4_3_6 = [i for i in range(1,100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(mod4_3_6)

if __name__ == '__main__':
    run()