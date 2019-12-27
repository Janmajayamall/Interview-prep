class Node():

    def __init__(self, val):
    
        self.val=val
        self.frequency=0
        self.left_count=0
        self.right_count=0
        self.left=None
        self.right=None
    
class BST():

    def __init__(self, root_node=None):

        self.root_node=root_node
        self.traverselist=[]
    
    def traverse(self, node):

        if node==None:
            return 
        
        self.traverse(node.left)
        self.traverselist.append(node.val)
        self.traverse(node.right)

        
        return
        
    def add(self, curr_node, node):

        if curr_node==None:
            self.root_node=node
            return 

        if node.val==curr_node.val:

            curr_node.frequency+=1
            return 
        
        else:
            
            if node.val>curr_node.val:

                curr_node.right_count+=1

                if curr_node.right!=None:
                    self.add(curr_node.right, node)
                else:
                    curr_node.right=node
                    return 

            else:
                curr_node.left_count+=1

                if curr_node.left!=None:
                    self.add(curr_node.left, node)
                else:
                    curr_node.left=node
                    return
        
        return
    
    def find_rank(self, val):
        
        curr_node=self.root_node
        counter=0
        while(curr_node!=None):
            # print('start')
            # print(curr_node.val)
            # if curr_node.right!=None:
            #     print(curr_node.right.val, curr_node.right_count)
            # if curr_node.left!=None:
            #     print(curr_node.left.val, curr_node.left_count)
            # print('end')

            if curr_node.val==val:
                return curr_node.left_count+counter+(curr_node.frequency)
            
            if curr_node.val>val:
                curr_node=curr_node.left
            else:
                counter+=(curr_node.left_count+1)
                curr_node=curr_node.right
        
        return -1
    


bst = BST()
vals = [5, 1, 4, 4, 5, 9, 7, 13, 3]
for i in vals:
    node=Node(i)
    bst.add(bst.root_node, node)

bst.traverse(bst.root_node)
print(bst.traverselist)

print(bst.find_rank(1))
print(bst.find_rank(3))
print(bst.find_rank(4))
