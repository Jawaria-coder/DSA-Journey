def getNode(head, k):
    position = 1

    while head is not None:
        if position == k:
            return head.data

        head = head.next
        position += 1

    return -1

# Time: O(n)
# Space: O(1)