prev = None
curr = head

while curr is not None:
    nextNode = curr.next

    curr.next = curr.prev
    curr.prev = nextNode

    prev = curr
    curr = nextNode

return prev

## Time: O(n)
## Space: O(1)