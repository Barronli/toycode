from IPython.core.debugger import set_trace

class Node:    
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        return


class BinTree:
    def __init__(self, nodes):
        self.root = None
        self.build(nodes)
        return
    
    # this can be done with a queue (or queues) iteratively. 
    # Push level i nodes, then push level i+1 nodes by popping level i.
    def get_nodes_at_level(self, level):  
        if level == 0:
            return [self.root]
        
        nodes = self.get_nodes_at_level(level-1)
        if all(node == None for node in nodes):
            return nodes
        
        ret = []
        for node in nodes:
            if node == None:
                ret.extend([None, None])
            else:
                ret.extend([node.left, node.right])
        
        return ret
    
    def insert(self, node):
        if self.root == None:
            self.root = Node(node)
            return
            
        i = 0
        while True:
            nodes = self.get_nodes_at_level(i)
            none_nodes = [i for i, e in enumerate(nodes) if e == None]
            if none_nodes != []: 
                break
            i += 1
        
        nodes = self.get_nodes_at_level(i-1)
        for nodei in nodes:
            if nodei.left == None:
                nodei.left = Node(node)
                break
            elif nodei.right == None:
                nodei.right = Node(node)
                break
        return
    
    def build(self, nodes):
        #set_trace()
        for node in nodes:
            self.insert(node)
        return
    
    def print(self):
        i = 0
        while True:
            nodes = self.get_nodes_at_level(i)
            #set_trace()
            if all(none == None for none in nodes):
                break    
            print([node.value if node!=None else '_' for node in nodes])
            i += 1
        
        return
        
def invert(node):
    tmp = node.right
    node.right = node.left
    node.left = tmp

    if node.left != None:
        invert(node.left)
    if node.right != None:
        invert(node.right)

    return

if __name__ == "__main__":
    #set_trace()
    tree = BinTree([1, 2, 3, 4, 5, 6, 7, 8])
    tree.print()
    invert(tree.root)
    tree.print()
 
