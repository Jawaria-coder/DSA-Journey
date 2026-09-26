### 1. Deletion at Front
def del_head(head):

    if head is None:
        return None

    temp = head
    head = head.next

    if head is not None:
        head.prev = None

    return head


### 2. Deletion at End
def del_last(head):

    if head is None:
        return None
    if head.next is None:
        return None


    curr = head
    while curr.next is not None:
        curr = curr.next

    if curr.prev is not None:
        curr.prev.next = None

    return head

### 3. Deletion at Given Pos(1-based index)
def delPos(head, x):
    
    if head is None:
        return head  

    curr = head

    for i in range(1, x):
        if curr is None:
            return head  
        curr = curr.next

    if curr is None:
        return head  

    if curr.prev is not None:
        curr.prev.next = curr.next

    if curr.next is not None:
        curr.next.prev = curr.prev

    if head == curr:
        head = curr.next

    del curr 
    return head