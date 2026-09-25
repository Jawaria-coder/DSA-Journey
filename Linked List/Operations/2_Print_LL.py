def printList(node):

    while node is not None:

        print(node.data, end="")
        if node.next is not None:
            print("->", end="")
        node = node.next
    print()

# Time: O(n)
# Space: O(1)