s = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]

class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class buildtree:

    def __init__(self):
        self.idx = -1
        self.root = None

    def build(self,s):
        self.idx += 1
        if s[self.idx] == -1:
            # print(-1,"@@")
            return None
        k = Node(s[self.idx])
        # print(k,k.data,"***")

        k.left = self.build(s)
        k.right = self.build(s)

        return k

    # preorder traveral
    def printtree(self,root):
        # print("**")
        if root == None:
            # print(-1)
            return
        print(root.data)
        self.printtree(root.left)
        self.printtree(root.right)


    #postorder traversal
    def postorder(self,root):
        if not root:
            # print(-1)
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

    def inorder(self,root):
        if root == None:
            # print(-1)
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)



o = buildtree()
root = o.build(s)
# o.printtree(root)
# o.postorder(root)
o.inorder(root)

