def linked_list_from_string(s):
    if s == 'None':
        return None
    s = s.split(' -> ')
    s.remove('None')
    node = [int(i) for i in s]
    head = Node(node[0])
    cur = head
    for i in node[1:]:
        cur.next = Node(i)
        cur = cur.next
    return head
