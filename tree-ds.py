class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None
    # insert data in to tree
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    # print the tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    # tree traversal algorithms
    def inorder_traversal(self,root):
        inorder=[]
        if root:
            inorder=self.inorder_traversal(root.left)
            inorder.append(root.data)
            inorder=inorder+self.inorder_traversal(root.right)
        return inorder
    def preorder_traversal(self,root):
        preorder=[]
        if root:
            preorder.append(root.data)
            preorder=preorder+self.preorder_traversal(root.left)
            preorder=preorder+self.preorder_traversal(root.right)
        return preorder
    def postorder_traversal(self,root):
        postorder=[]
        if root:
            postorder=self.postorder_traversal(root.left)
            postorder=postorder+self.postorder_traversal(root.right)
            postorder.append(root.data)
        return postorder
root=Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(f"Inorder traversal {root.inorder_traversal(root)}")
print(f"Preorder traversal {root.preorder_traversal(root)}")
print(f"Postorder traversal {root.postorder_traversal(root)}")