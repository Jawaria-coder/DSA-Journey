class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


def count_nodes(head):
    count = 0
    curr = head

    while curr is not None:
        count += 1
        curr = curr.next

    return count

# Time: O(n)
# Space: O(1)