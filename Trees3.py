class Treenode:
    def __init__(self,Employee,Post):
        self.Employees = []
        self.Post = []
        self.data = Employee
        self.data1 = Post
        self.parent = None

    def add_child(self,emp):
        emp.parent = self
        self.Employees.append(emp)
        self.Post.append(self.data1)

    def get_level(self):
        level = 0   
        p = self.parent
        while p:  
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = "  "*self.get_level()*2

        print(f'{spaces}{self.data} ({self.data1})')
        if self.Employees:
            for employee in self.Employees:
                employee.print_tree()

def build_Company_Tree():
    head = Treenode("Nilupal","CEO")

    head1 = Treenode("Chinmay","CTO")

    head1_1 = Treenode("Vishwa","Infrastructure head")
    head1_1.add_child(Treenode("Dhaval","Cloud Manager"))
    head1_1.add_child(Treenode("Abhijit","App Manager"))

    head1.add_child(head1_1)

    head2 = Treenode("Gels","Hr Head")
    head2.add_child(Treenode("Peter","Recruitment Manager"))
    head2.add_child(Treenode("Waqas","Policy Manager"))



    # print(head1_1.get_level())


    head.add_child(head1)
    head.add_child(head2)

    return head

root = build_Company_Tree()
root.print_tree()


    
    
    