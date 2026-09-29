def deleteK(head, k):
    if head is None or k == 1:
        return None

    prev = head
    curr = head.next
    pos = 2

    while curr is not None:
        if pos % k == 0:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next

        pos += 1

    return head

## Time: O(n)
## Space: O(1)