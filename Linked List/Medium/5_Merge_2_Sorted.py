def sortedMerge(head1, head2):
    dummy = Node(0)
    tail = dummy

    curr1 = head1
    curr2 = head2

    while curr1 is not None and curr2 is not None:
        if curr1.data <= curr2.data:
            tail.next = curr1
            tail = curr1
            curr1 = curr1.next
        else:
            tail.next = curr2
            tail = curr2
            curr2 = curr2.next

    if curr1 is not None:
        tail.next = curr1

    if curr2 is not None:
        tail.next = curr2

    return dummy.next

## Time: O(n + m)
## Space: O(1)