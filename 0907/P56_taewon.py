from collections import deque
def levelOrder(root):
    node = []
    root = deque(root)

    # 원소가 없을때
    if len(root) == 0:
        return node

    node.append([root.popleft()])

    # 원소가 한개일때
    if len(root) == 0:
        return node
        
    while len(root) != 0:
        temp = []
        a = root.popleft()
        b = root.popleft()
        if a != 'null': temp.append(a)
        if b != 'null': temp.append(b)
        if len(temp) > 0:
            node.append(temp)
    return node