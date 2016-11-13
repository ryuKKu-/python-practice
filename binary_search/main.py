from binary_search.BinaryTree import BinaryTree
from binary_search.AVLTree import AVLTree


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
    b = BinaryTree(*array)
    b.breadth_first()

    print(b.length(), '\n')
    print(b.contains(8888), '\n')

    b.delete(10)
    b.breadth_first()

    array2 = [6, 5, 4, 3, 2, 1, 7, 8, 9]
    bst = BinaryTree(*array2)
    bst.breadth_first()

    avl = AVLTree(*array2)
    avl.breadth_first()

if __name__ == "__main__":
    main()
