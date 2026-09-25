def search_key(head, key):

    curr = head

    while curr is not None:
        if curr.data == key:
            return True
        curr = curr.next

    return False

# Time: O(n)
# Space: O(1)