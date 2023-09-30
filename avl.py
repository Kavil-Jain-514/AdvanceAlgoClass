class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if node is None:
            return
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def insert(self, root, key):
        if root is None:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        self.update_height(root)

        balance = self.balance(root)

        # Left Heavy
        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        # Right Heavy
        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            min_val = self.find_min_value(root.right)
            root.key = min_val
            root.right = self.delete(root.right, min_val)

        self.update_height(root)

        balance = self.balance(root)

        # Left Heavy
        if balance > 1:
            if self.balance(root.left) >= 0:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        # Right Heavy
        if balance < -1:
            if self.balance(root.right) <= 0:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def find_min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key

    def insert_node(self, key):
        self.root = self.insert(self.root, key)

    def delete_node(self, key):
        self.root = self.delete(self.root, key)

    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def search_node(self, key):
        return self.search(self.root, key)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)

    def print_tree(self):
        self.inorder_traversal(self.root)


# Demonstration
if __name__ == "__main__":
    avl = AVLTree()

    # Insertion
    keys_to_insert = [30, 20, 40, 10, 25, 35, 50]
    for key in keys_to_insert:
        avl.insert_node(key)

    print("AVL Tree after insertions:")
    avl.print_tree()
    print()

    # Deletion
    avl.delete_node(10)
    avl.delete_node(40)

    print("\nAVL Tree after deletions:")
    avl.print_tree()
    print()

    # Searching
    search_key = 25
    result = avl.search_node(search_key)
    if result:
        print(f"Found {search_key} in the tree.")
    else:
        print(f"{search_key} not found in the tree.")
