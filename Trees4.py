class Treenode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
            
    def print_tree(self):
        spaces = "  "*self.get_level()*3
        prefix = spaces+"|__"
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    def node(data):
        root = Treenode(data)
        return root

    parent11 = []
    child11 = []

    while True:
        var1 = str(input("Root:"))
        parent11.append(node(var1).data)
        
        if ord('y')==121:
            break
    i = 0
    j = 0
    while parent11:
        print(f"{parent11[i]}")
        var2 = str(input("Child:"))
        child11.append(node(parent11[i]).add_child(var2))
        print(child11[j].data)
        if ord('y')==121:
            break
        i += 1



    root1 = node("nikita")
    return parent11

if __name__ == '__main__':
    print(build_product_tree())

    


# head1 = Treenode("Chinmay","CTO")
# head1_1 = Treenode("Vishwa","Infrastructure head")
# head1_1.add_child(Treenode("Dhaval","Cloud Manager"))
# head1_1.add_child(Treenode("Abhijit","App Manager"))
# head1.add_child(head1_1)
# head2 = Treenode("Gels","Hr Head")
# head2.add_child(Treenode("Peter","Recruitment Manager"))
# head2.add_child(Treenode("Waqas","Policy Manager"))
# print(head1_1.get_level())
# head.add_child(head1)
# head.add_child(head2)

    
    
    