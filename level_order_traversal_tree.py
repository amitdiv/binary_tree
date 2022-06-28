class Tree:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Create:

    def __init__(self):
        self.idx = -1

    def build(self,s):

        self.idx += 1
        if s[self.idx] == -1:
            return None
        k = Tree(s[self.idx])
        k.left = self.build(s)
        k.right = self.build(s)

        return k

    def level_order(self,root):

        queue = []
        queue.append(root)
        while queue:
            currnode = queue.pop(0)
            currval = currnode.data
            print(currval)

            if currnode.left:
                queue.append(currnode.left)
            if currnode.right:
                queue.append(currnode.right)

s = [1,2,3,-1,-1,5,-1,-1,4,-1,6,-1,-1]
obj = Create()

root = obj.build(s)
obj.level_order(root)

