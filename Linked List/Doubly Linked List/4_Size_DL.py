def findSize(curr):
    size = 0
    while curr:
        size += 1
        curr = curr.next
    return size

## Time: O(n)
## Space: O(1)