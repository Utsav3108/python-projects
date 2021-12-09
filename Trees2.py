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
    root = Treenode("Electronics")

    laptop = Treenode("Laptop")
    laptop.add_child(Treenode("MAC"))
    laptop.add_child(Treenode("Windows"))
    laptop.add_child(Treenode("Linux"))

    TV = Treenode("TV")
    TV.add_child(Treenode("Samsung"))
    TV.add_child(Treenode("Toshiba"))
    TV.add_child(Treenode("Sony"))

    Refrigeretor = Treenode("Refrigeretor")
    Refrigeretor.add_child(Treenode("Haier"))
    Refrigeretor.add_child(Treenode("Samsung"))
    Refrigeretor.add_child(Treenode("LG"))
    
    root.add_child(laptop)
    root.add_child(TV)
    root.add_child(Refrigeretor)

    return root

root = build_product_tree()
root.print_tree()



