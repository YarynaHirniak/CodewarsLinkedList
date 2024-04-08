def loop_size(node):
    visited = {}
    while node not in visited:
        visited[node] = len(visited)
        node = node.next
    return len(visited) - visited[node]
