from binary_search.BinaryTree import BinaryTree


def binary_search(array, key, min, max):
    """
    Naive implementation of a binary search using a ordered list
    """
    if max < min:
        return -1

    mid = (min+max)//2

    if array[mid] < key:
        return binary_search(array, key, mid+1, max)
    elif array[mid] > key:
        return binary_search(array, key, min, mid-1)
    else:
        return mid


def main():
    array = [10, 65, 85, 41, 5124, 2310, 2, 9, 1, 5, 56, 874]
    bts = BinaryTree(*array)
    bts.breadth_first()

    print(bts.length(), '\n')
    print(bts.contains(8888), '\n')

    bts.delete(10)
    bts.breadth_first()

if __name__ == "__main__":
    main()
