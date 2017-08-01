class AlphaBetaPruning:
    def __init__(self, game_tree):
        self.game_tree = game_tree
        self.root = game_tree.root

    @staticmethod
    def _get_successor(node):
        return node.children

    @staticmethod
    def _is_terminal(node):
        return len(node.children) == 0

    @staticmethod
    def _node_value(node):
        return node.value

    def min_value(self, node, alpha, beta):
        if self._is_terminal(node):
            return self._node_value(node)

        infinity = float('inf')
        value = infinity

        successors_state = self._get_successor(node)
        for state in successors_state:
            value = min(value, self.max_value(state, alpha, beta))
            if value <= alpha:
                return value
            beta = min(beta, value)
        return value

    def max_value(self, node, alpha, beta):
        if self._is_terminal(node):
            return self._node_value(node)

        infinity = float('inf')
        value = -infinity

        successors_state = self._get_successor(node)
        for state in successors_state:
            value = max(value, self.min_value(state, alpha, beta))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    def alpha_beta_search(self, node):
        infinity = float('inf')
        best_val = -infinity
        beta = infinity

        successors_state = self._get_successor(node)
        best_state = None
        for state in successors_state:
            value = self.min_value(state, best_val, beta)
            if value > best_val:
                best_val = value
                best_state = state
        return best_state









































