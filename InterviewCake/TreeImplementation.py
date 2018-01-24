class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root

    def insert(self, t):
        new = Node(t)
        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:
                if t < node.key:
                    if node.left is None:
                        node.left = new
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new
                        break
                    node = node.right

    def in_order(self, root):
        if root is None:
            return
        self.in_order(root.left)
        print root.key,
        self.in_order(root.right)

    def pre_order(self, root):
        if root is None:
            return
        print root.key,
        self.pre_order(root.left)
        self.pre_order(root.right)

    def post_order(self, root):
        if root is None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print root.key,

    def search(self, node, t):
        if node is None:
            return False
        else:
            if node.key == t:
                return True
            elif node.key < t:
                return self.search(node.right, t)
            else:
                return self.search(node.left, t)

    def level_by_level(self):
        this_level = [self.root]
        while this_level:
            next_level = list()
            for n in this_level:
                print n.key,
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            print
            this_level = next_level

    def height_of_tree(self, node):
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            left_height = self.height_of_tree(node.left)
            right_height = self.height_of_tree(node.right)

            # Use the larger one
            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    def min_value_in_tree(self, root):
        if root.left is None:
            return root.key
        else:
            return self.min_value_in_tree(root.left)

    def max_value_in_tree(self, root):
        if root.right is None:
            return root.key
        else:
            return self.max_value_in_tree(root.right)

    def is_super_balanced(self, root):
        if root is None:
            return True

        depths = []

        nodes = []
        nodes.append((self.root, 0))

        while len(nodes):
            node, depth = nodes.pop()

            if not node.left and not node.right:
                if depth not in depths:
                    depths.append(depth)

                if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                    return False
            else:
                if node.left:
                    nodes.append((node.left, depth + 1))
                if node.right:
                    nodes.append((node.right, depth + 1))
        return True

    def valid_binary_search_tree(self, root, low=-float('inf'), high=float('inf')):
        if not root:
            return True

        if root.key >= high or root.key <= low:
            return False

        return (self.valid_binary_search_tree(root.left, low, root.key) and self.valid_binary_search_tree(root.right,
                                                                                                          root.key,
                                                                                                          high))

    def largest(self, root):
        current = root
        while current:
            if not current.right:
                return current.key
            current = current.right

    def second_largest(self, root):
        if root is None or (root.left is None and root.right is None):
            return "Error"

        current = root

        while current:
            if current.left and not current.right:
                return self.largest(current.left)

            if current.right and not current.right.left and not current.right.right:
                return current.value

            current = current.right



r = BinarySearchTree()
r.insert(10)
r.insert(20)
r.insert(12)
r.insert(3)
r.insert(7)
r.insert(1)
r.insert(5)

print "InOrder              :  ", r.in_order(r.root)
print "PreOrder             :  ", r.pre_order(r.root)
print "PostOrder            :  ", r.post_order(r.root)
print "Is 7 in Tree?        :  ", r.search(r.root, 7)
print "Is 11 in Tree        :  ", r.search(r.root, 11)
print "Height of the Tree   :  ", r.height_of_tree(r.root)
print "Level By Level Tree  :"
print r.level_by_level()
print "Minimum value in Tree:  ", r.min_value_in_tree(r.root)
print "Maximum value in Tree:  ", r.max_value_in_tree(r.root)
print "Is Super Balanced    :  ", r.is_super_balanced(r.root)
print "Is Binary Tree       :  ", r.valid_binary_search_tree(r.root)
print "Second Largest in BST:  ", r.second_largest(r.root)
