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

    print(ll.pop_back())
    print(ll)

    ll.push_back(21412)
    ll.push_back(99)
    print(ll)
    print("Value at index 2 : %d" % ll.value_at(2))

    ll.insert_at(2, 7777)
    ll.insert_at(0, 8452)
    print(ll)

    ll.reverse()
    print(ll)

if __name__ == "__main__":
    main()
