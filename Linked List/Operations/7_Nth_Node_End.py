def getKthFromLast(head, k):

    fast = head
    slow = head

    for i in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    if slow is not None:
        return slow.data
        
    return -1