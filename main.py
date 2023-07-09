# Constants
RED = 'RED'
BLACK = 'BLACK'


# Node class for Red-Black tree
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.color = RED  # Initialize all nodes as RED by default


# Red-Black tree class
class RedBlackTree:
    def __init__(self):
        self.root = None

    # Perform a left rotation on the given node
    def _left_rotate(self, node):
        right_child = node.right_child
        node.right_child = right_child.left_child

        if right_child.left_child is not None:
            right_child.left_child.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left_child:
            node.parent.left_child = right_child
        else:
            node.parent.right_child = right_child

        right_child.left_child = node
        node.parent = right_child

    # Perform a right rotation on the given node
    def _right_rotate(self, node):
        left_child = node.left_child
        node.left_child = left_child.right_child

        if left_child.right_child is not None:
            left_child.right_child.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right_child:
            node.parent.right_child = left_child
        else:
            node.parent.left_child = left_child

        left_child.right_child = node
        node.parent = left_child

    # Insert a new node with the given key and value into the tree,
    # following the Red-Black tree insertion rules.
    def insert(self, key, value):
        new_node = Node(key, value)
        self._insert_helper(new_node)
        self._insert_fixup(new_node)

    # Helper method for insertion operation. It finds the appropriate
    # position for the new_node based on its key and inserts it into
    # the tree.
    def _insert_helper(self, new_node):
        current = self.root
        parent = None

        while current is not None:
            parent = current
            if new_node.key < current.key:
                current = current.left_child
            else:
                current = current.right_child

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left_child = new_node
        else:
            parent.right_child = new_node

    # After inserting a new node, this method adjusts the tree's colors
    # and structure to maintain the Red-Black tree properties
    def _insert_fixup(self, node):
        while node != self.root and node.parent.color == RED:
            if node.parent == node.parent.parent.left_child:
                uncle = node.parent.parent.right_child

                if uncle is not None and uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right_child:
                        node = node.parent
                        self._left_rotate(node)

                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left_child

                if uncle is not None and uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left_child:
                        node = node.parent
                        self._right_rotate(node)

                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._left_rotate(node.parent.parent)

        self.root.color = BLACK

    # Search for a node with the given key in the tree and return its value,
    # or return None if the key is not found.
    def search(self, key):
        current = self.root

        while current is not None:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left_child
            else:
                current = current.right_child

        return None

    # Delete a node with the given key from the tree, if it exists.
    def delete(self, key):
        node = self.search_node(key)
        if node is not None:
            self._delete_node(node)

    # Delete the specified node from the tree, adjusting the structure
    # and colors of the remaining nodes to maintain the Red-Black tree
    # properties.
    def _delete_node(self, node):
        if node.left_child is None or node.right_child is None:
            deleted_node = node
        else:
            deleted_node = self._successor(node)

        if deleted_node.left_child is not None:
            child = deleted_node.left_child
        else:
            child = deleted_node.right_child

        if child is not None:
            child.parent = deleted_node.parent

        if deleted_node.parent is None:
            self.root = child
        elif deleted_node == deleted_node.parent.left_child:
            deleted_node.parent.left_child = child
        else:
            deleted_node.parent.right_child = child

        if deleted_node != node:
            node.key = deleted_node.key
            node.value = deleted_node.value

        if deleted_node.color == BLACK:
            self._delete_fixup(child, deleted_node.parent)

    # After deleting a node, this method adjusts the tree's colors
    # and structure to maintain the Red-Black tree properties.
    def _delete_fixup(self, node, parent):
        while node != self.root and (node is None or node.color == BLACK):
            if node == parent.left_child:
                sibling = parent.right_child

                if sibling.color == RED:
                    sibling.color = BLACK
                    parent.color = RED
                    self._left_rotate(parent)
                    sibling = parent.right_child

                if (sibling.left_child is None or sibling.left_child.color == BLACK) and \
                        (sibling.right_child is None or sibling.right_child.color == BLACK):
                    sibling.color = RED
                    node = parent
                    parent = node.parent
                else:
                    if sibling.right_child is None or sibling.right_child.color == BLACK:
                        sibling.left_child.color = BLACK
                        sibling.color = RED
                        self._right_rotate(sibling)
                        sibling = parent.right_child

                    sibling.color = parent.color
                    parent.color = BLACK
                    sibling.right_child.color = BLACK
                    self._left_rotate(parent)
                    node = self.root
            else:
                sibling = parent.left_child

                if sibling.color == RED:
                    sibling.color = BLACK
                    parent.color = RED
                    self._right_rotate(parent)
                    sibling = parent.left_child

                if (sibling.right_child is None or sibling.right_child.color == BLACK) and \
                        (sibling.left_child is None or sibling.left_child.color == BLACK):
                    sibling.color = RED
                    node = parent
                    parent = node.parent
                else:
                    if sibling.left_child is None or sibling.left_child.color == BLACK:
                        sibling.right_child.color = BLACK
                        sibling.color = RED
                        self._left_rotate(sibling)
                        sibling = parent.left_child

                    sibling.color = parent.color
                    parent.color = BLACK
                    sibling.left_child.color = BLACK
                    self._right_rotate(parent)
                    node = self.root

        if node is not None:
            node.color = BLACK

    # Find and return the successor node of the given node in the tree,
    # i.e., the node with the smallest key greater than the given node's key.
    def _successor(self, node):
        if node.right_child is not None:
            current = node.right_child
            while current.left_child is not None:
                current = current.left_child
            return current

        current = node.parent
        while current is not None and node == current.right_child:
            node = current
            current = current.parent
        return current

    # Search for a node with the given key in the tree and return it,
    # or return None if the key is not found.
    def search_node(self, key):
        current = self.root

        while current is not None:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left_child
            else:
                current = current.right_child

        return None

    # Get all records in sorted order
    def get_all_records_sorted(self):
        records = []
        self._inorder_traversal(self.root, records)
        return records

    # Perform an inorder traversal, appending each node's key-value pair to `records`.
    def _inorder_traversal(self, node, records):
        if node is not None:
            self._inorder_traversal(node.left_child, records)
            records.append((node.key, node.value))
            self._inorder_traversal(node.right_child, records)


class RedBlackTreeConsoleInterface:
    MENU_OPTIONS = {
        "1": "Add a record",
        "2": "Delete a record",
        "3": "Search for a record",
        "4": "Display all records",
        "5": "Exit"
    }

    def __init__(self):
        self.tree = RedBlackTree()

    def display_menu(self):
        print("Menu:")
        for option, description in self.MENU_OPTIONS.items():
            print(f"{option}. {description}")
        print()

    def get_menu_choice(self):
        while True:
            choice = input("Enter your choice (1-5): ")
            if choice in self.MENU_OPTIONS:
                return choice
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

    def get_record_details(self):
        name = input("Enter the name for the record: ")
        phone = input("Enter the phone number for the record: ")
        return name, phone

    def add_record(self):
        print("Add a Record")
        name, phone = self.get_record_details()
        self.tree.insert(name, phone)
        print("Record added successfully.")

    def delete_record(self):
        print("Delete a Record")
        name = input("Enter the name to delete: ")
        self.tree.delete(name)
        print("Record deleted successfully.")

    def search_record(self):
        print("Search for a Record")
        name = input("Enter the name to search: ")
        phone = self.tree.search(name)
        if phone is not None:
            print(f"Record found: Name: {name}, Phone: {phone}")
        else:
            print("Record not found.")

    def display_all_records(self):
        print("Display Records")
        sorted_records = self.tree.get_all_records_sorted()
        if sorted_records:
            for name, phone in sorted_records:
                print(f"Name: {name}, Phone: {phone}")
        else:
            print("No records found.")

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_menu_choice()

            if choice == "1":
                self.add_record()
            elif choice == "2":
                self.delete_record()
            elif choice == "3":
                self.search_record()
            elif choice == "4":
                self.display_all_records()
            elif choice == "5":
                print("Exiting...")
                break

            print()


interface = RedBlackTreeConsoleInterface()
interface.run()
