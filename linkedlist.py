class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def stringify(node):
    head = node
    res = ''
    while head is not None:
        res+=str(head.data)
        res+=' -> '
        head = head.next
    res+='None'
    return res 