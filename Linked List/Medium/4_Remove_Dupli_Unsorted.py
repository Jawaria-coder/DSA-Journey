def removeDuplicates(head):
    if head is None:
        return head

    seen = {head.data}
    prev = head
    curr = head.next

    while curr is not None:
        if curr.data in seen:
            prev.next = curr.next
            curr = curr.next
        else:
            seen.add(curr.data)
            prev = curr
            curr = curr.next

    return head

## Time: O(n)
## Space: O(n)