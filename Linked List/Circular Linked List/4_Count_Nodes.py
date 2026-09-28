def countNodes(head):

    curr = head
    count = 0

    if (head == None) :
        return 0
    
    while True :
        curr = curr.next
        count += 1
        if (curr == head):
            break
    
    return result

# Time: O(n)
# Space: O(1)