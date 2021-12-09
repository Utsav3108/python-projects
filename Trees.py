class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if data < self.data:
            if self.left is None:
                self.left = node(data)
            else :
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = node(data)
            else:
                self.right.insert(data)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def InOrder(self,root):
        res = []
        if root:
            res = self.InOrder(root.left)
            res.append(root.data)
            res = res + self.InOrder(root.right)
        return res
    def preorder(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)
        return res
    def PostOrder(self,root):
        res = []
        if root:
            res = self.PostOrder(root.left)
            res = res + self.PostOrder(root.right)
            res.append(root.data)
        return res

    def Pop(self,root,data):
        if data in root.InOrder(root):
            n = 0
            for i in root.InOrder(root):
                if i == data:
                    root.InOrder(root).pop(n)
                    return n
                n = n + 1
        else:
            print(f"{data} not exist")



n = int(input()) - 1
root = node(int(input("root:")))
for i in range(n):
    root.insert(int(input("data:")))
print("Inorder:",root.InOrder(root))
print("Preorder:",root.preorder(root))
print("Postorder:",root.PostOrder(root))
root.PrintTree()
print("Pop at",root.Pop(root,5))
root.PrintTree()