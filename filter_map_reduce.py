from functools import reduce
def run():
    list_1 = [1,2,4,5,6,7,8]

    list_comprehensions = [i for i in list_1 if i % 2 != 0]
    print(list_comprehensions)

    list_filter = list(filter(lambda i:i%2!=0, list_1))
    print(list_filter)

    list_map = list(map(lambda i : i**2, list_1))
    print(list_map)

    value_reduce = reduce(lambda a,b: a*b, list_1)
    print(value_reduce)

if __name__ == '__main__':
    run()