def array():
    arr = [12, 2, 4, 40012]

    print(arr)
    print("Array size : %r" % len(arr))
    print("Item at index 2 : %r" % arr[2])
    print("Index of 12 : %r" % arr.index(12))

    arr.pop()
    arr.reverse()
    print("Reversed : %r " % arr)

    arr.append(12421)
    arr.sort()
    print("Sorted : %r" % arr)

    foo = arr.copy()
    arr.clear()
    print("Copy & clean : ", arr, foo)

    arr = [45, 685, -45, 12, 1987, foo]
    print(arr, arr[-1])

    arr.extend(foo)
    print(arr, arr[-1])
    print('\n\n')


def list_comprehensions():
    arr = [1, 2, 3, 4]
    print("List comprehensions : ", [x ** 2 for x in arr])
    print('\n\n')


def sets():
    a = set('maefmzemlkflkzflkmrgmkln')
    b = set('abaksneja')

    print(a, b)
    print("letters in a but not in b : %r " % (a - b))
    print("letters in either a or b : %r " % (a | b))
    print("letters in both a and b : %r " % (a & b))
    print("letters in a or b but not both : %r " % (a ^ b))
    print('\n\n')


def dictionnary():
    data = {'Foo': 'Bar', 'Baz': 'Test', 'Luc': 'ryuK'}
    print(data)

    del data['Foo']
    data['Rap'] = 'God'

    print("Get item by key Luc : %s" % data.get('Luc'))

    data.setdefault('names', []).append('Hello')
    data.setdefault('names', []).append(',')
    data.setdefault('names', []).append('World !')

    for x, y in data.items():
        print("Key : %s, Value : %s" % (x, y))

    for i, j in enumerate(['a', 'b', 'c']):
        print(i, j)


def main():
    array()
    list_comprehensions()
    sets()
    dictionnary()

if __name__ == "__main__":
    main()
