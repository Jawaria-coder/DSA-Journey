def is_circular(head):
    if not head:
        return True

    slow = head
    fast = head.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

# Time: O(n)
# Space: O(1)