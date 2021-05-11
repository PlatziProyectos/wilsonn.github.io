def palindrome(string):
    assert len(string) > 0, "No se puede ingresar una cadena vacía"      
    #try:
    #    if len(string) == 0:
    #        raise ValueError("No se puede ingresar una cadena vacía")
    return string == string[::-1]
    #except ValueError as ve:
    #    print(ve)
    #    return False
    #finally:
    #    print("siempre imprimo esto")

def run():
    try:
        #print(palindrome(1))
        print(palindrome("ana"))
    except TypeError:
        print("Solo se pueden ingresar strings")    

if __name__ == '__main__':
    run()