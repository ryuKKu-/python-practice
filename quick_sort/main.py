from quick_sort.QuickSort import QuickSort


def main():
    array = [12, 13, 1, 9, -4, 643, 12031, -12312, 2, 403]
    numbers = array[:]  # deep copy

    qs = QuickSort(numbers)
    output = qs.sort()

    print(array, '\n', output)

if __name__ == "__main__":
    main()