from merge_sort.MergeSort import MergeSort


def main():
    array = [12, 13, 1, 9, -4, 643, 12031, -12312, 2, 403]
    numbers = array[:]  # deep copy

    ms = MergeSort(numbers)
    output = ms.sort()

    print("%r\n%r" % (array, output))

if __name__ == "__main__":
    main()
