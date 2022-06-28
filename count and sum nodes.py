class Tree:

    def __init__(self,data):

        self.data = data
        self.left = None
        self.right = None

class Build:

    def __init__(self):
        self.idx = -1
        self.count = 0
        self.sum = 0

    def build(self,s):
        self.idx += 1
        if s[self.idx] == -1:
            return None

        node = Tree(s[self.idx])

        node.left = self.build(s)

        node.right = self.build(s)

        return node

    def traverse(self,root):
        if not root:
            return None

        print(root.data)
        self.traverse(root.left)
        self.traverse(root.right)

    def countnodes(self,root):

        if not root:
            return None
        print(root, root.data, "****")
        self.count += 1
        self.countnodes(root.left)
        self.countnodes(root.right)
        return self.count

    def sumnodes(self,root):

        if not root:
            return None

        self.sum += root.data
        self.sumnodes(root.left)
        self.sumnodes(root.right)
        return self.sum


s = [1,2,3,-1,-1,5,-1,-1,4,-1,6,-1,-1]

obj = Build()

root = obj.build(s)
obj.traverse(root)

count = obj.countnodes(root)
print(count)

sum = obj.sumnodes(root)
print(sum)
