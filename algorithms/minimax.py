class MiniMax:
    def __init__(self, game_tree):
        self.game_tree = game_tree
        self.root = game_tree.root
        self.current_node = None
        self.successors = []

    @staticmethod
    def _get_successor(node):
        return node.children

    @staticmethod
    def _is_terminal(node):
        return len(node.children) == 0

    @staticmethod
    def _node_value(node):
        return node.value

    def min_value(self, node):
        if self._is_terminal(node):
            return self._node_value(node)

        infinity = float('inf')
        min_value = infinity

        successors_state = self._get_successor(node)
        for state in successors_state:
            min_value = min(min_value, self.max_value(state))
        return min_value

    def max_value(self, node):
        if self._is_terminal(node):
            return self._node_value(node)

        infinity = float('inf')
        max_value = -infinity

        successors_state = self._get_successor(node)
        for state in successors_state:
            max_value = max(max_value, self.min_value(state))
        return max_value

    def minimax(self, node):
        best_val = self.max_value(node)

        successors = self._get_successor(node)
        best_move = None
        for elem in successors:
            if elem.value == best_val:
                best_move = elem
                break
        return best_move














