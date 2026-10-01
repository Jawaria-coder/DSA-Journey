def removeDuplicates(head):
    curr = head

    while curr is not None and curr.next is not None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head

## Time: O(n)
## Space: O(1)