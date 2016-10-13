from linked_list.LinkedList import LinkedList


def main():
    ll = LinkedList()
    print(ll.is_empty())

    ll.push_front(12)
    ll.push_front(23)
    print(ll)

    ll.push_front(53)
    ll.push_back(0)
    print(ll)

    print(ll.pop_front())
    print(ll)

    print(ll.front())
    print(ll.back())

if __name__ == "__main__":
    main()
