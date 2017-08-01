class GameNode:
    def __init__(self, name, value=0, parent=None):
        self.name = name
        self.value = value
        self.parent = parent
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


class GameTree:
    def __init__(self):
        self.root = None

    def build_tree(self, root_pos, positions):
        self.root = root_pos

