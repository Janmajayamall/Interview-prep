# class node(head, tail):
#   self.head=head
#   self.tail=tail

def bi_node_rec(root):

  if root==None:
    return root

  right=bi_node_rec(root.node2)
  left=bi_node_rec(root.node1)

  # new_node=BiNode(root.data, None, None)
  head=None
  tail=None

  if left!=None:
    left.tail.node2=root
    root.node1=left.tail
    head=left.head
  else:
    root.node1=None
    head=root

  if right!=None:
    right.head.node1=root
    root.node2=right.head
    tail=right.tail
  else:
    root.node1=None
    tail=root

  return node(head, tail)


