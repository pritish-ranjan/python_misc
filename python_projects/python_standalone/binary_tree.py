class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add data in left substree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
            # add data in right subtree
    
    def in_order_traversal(self):

        elements = []
        
        # vist the left tree

        if self.left:
            elements += self.left.in_order_traversal()
        
        # visit base node
        elements.append(self.data)

        # visit the right tree

        if self.right:
            elements += self.right.in_order_traversal() 
        
        return elements

    def search(self, val):
       
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements

    def post_order_traversal(self):
        
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
        
    def find_min(self):
        
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):

        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_sum_all_elements(self):

        left_sum = self.left.find_sum_all_elements() if self.left else 0
        right_sum = self.right.find_sum_all_elements() if self.right else 0

        return left_sum + right_sum + self.data

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    numbers_tree = build_tree(numbers)

    sorted_in_order = numbers_tree.in_order_traversal()
    numbers_tree.add_child(43)

    print("Lowest number in the tree is ", numbers_tree.find_min())

    print("Highest number in the tree is ", numbers_tree.find_max())

    print("The sum of all elements is ", numbers_tree.find_sum_all_elements())

    print("The in-order traversal of the tree is ", numbers_tree.in_order_traversal())

    print("The pre-order traversal of the tree is ", numbers_tree.pre_order_traversal())

    print("The post-order traversal of the tree is ", numbers_tree.post_order_traversal())