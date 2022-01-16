def search_parent_q(q, current_node, reduce):
    reduce = int(reduce/2)
    right_node=current_node-1
    left_node=right_node-reduce

    if(right_node == q or left_node == q):
        return current_node 
    else:
        if(q <= left_node):
            return search_parent_q(q, left_node, reduce)
        else:
            return search_parent_q(q, right_node, reduce)

def solution(h, q):
    length_q = len(q)

    if(h > 30 or h < 1):
        raise ValueError('Given heigth is invalid!')
    if(length_q > 10000 or length_q < 1):
        raise ValueError('Given list is invalid!')
    
    nodes = (2**h)-1
    output = []

    for i in range(length_q):
        if (q[i]<nodes and q[i]>0):
            output.append(search_parent_q(q[i], nodes, nodes-1))
        else:
            output.append(-1)
    return output