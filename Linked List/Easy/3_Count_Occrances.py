def count(head, key):
    curr = head
    count = 0
    
    while curr is not None:
        if curr.data == key:
            count += 1
        curr = curr.next

    return count

## Time: O(n)
## Space: O(1)