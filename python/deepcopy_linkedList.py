def deepCopy(head):
    # WRITE YOUR CODE HERE
    if head == None:
        return None
    cur = head;
    new_head = None
    new_prev = None
    ht = dict()

    while (cur != None):
        new_node = ALNode(cur.value)
        new_node.arbitrary = cur.arbitrary;
        if new_prev != None:
            new_prev.next = new_node
        else:
            new_head = new_node
        ht[cur] = new_node

        new_prev = new_node
        cur = cur.next 
    new_cur = new_head

  # updating arbitrary pointer
    while new_cur != None:
        if new_cur.arbitrary != None:
            node = ht[new_cur.arbitrary]
            new_cur.arbitrary = node
        new_cur = new_cur.next

    return new_head
    pass
