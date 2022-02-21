"""
Tymur Krasnianskyi
Yaryna Fialko
Descrete Math Lab 1
18.02.2022
"""
from numpy import inf
import dataset_reader


class Node:

    def __init__(self, dataset, target, gini):
        self.dataset = dataset
        self.target = target
        self.gini = gini
        self.feature_index = 0
        self.threshold = 0
        self.left = None
        self.right = None
        self.outcome = None

    @staticmethod
    def init_split(dataset):
        class_values = list(set(row[-1] for row in dataset))
        best_index, best_threshold, best_gini, best_groups = inf, inf, inf, None
        if len(dataset) < 1:
            return
        for index in range(len(dataset[0]) - 1):
            for row in dataset:
                groups = test_split(index, row[index], dataset)
                gini = MyDecisionTreeClassifier.gini(groups, class_values)
                if gini < best_gini:
                    best_gini = gini
                    best_index, best_threshold, best_groups = index, row[index], groups
        return best_gini, best_index, float(best_threshold), best_groups

    # Select the best split point for a dataset
    def get_split(self):
        best_gini, best_index, best_threshold, best_groups = Node.init_split(self.dataset)
        self.feature_index = best_index
        self.left = Node(best_groups[0], self.target, best_gini)
        self.left.threshold = best_threshold
        self.right = Node(best_groups[1], self.target, best_gini)
        self.right.threshold = best_threshold

    # Create a terminal node value
    def to_terminal(self, group=None):
        # TODO: now this probably doesn't work: check and rewrite
        if group:
            outcomes = [row[-1] for row in group]
        else:
            outcomes = [row[-1] for row in self.dataset]

        if not outcomes:
            return
        self.outcome = max(set(outcomes), key=outcomes.count)

    def split(self, max_depth, min_size, depth):
        """

        """
        if self.gini == 0.0:
            self.to_terminal()
            self.left = None
            self.right = None
            return

        if not self.left or not self.right:
            return

        if not self.left.dataset or not self.right.dataset:
            self.left.to_terminal(self.left.dataset + self.right.dataset)
            self.right.to_terminal(self.left.dataset + self.right.dataset)
            return

        if depth >= max_depth:
            self.left.to_terminal(), self.right.to_terminal()
            return

        if len(self.left.dataset) <= min_size:
            self.left.to_terminal()
        else:
            self.left.get_split()
            self.left.split(max_depth, min_size, depth + 1)

        if len(self.right.dataset) <= min_size:
            self.right.to_terminal()
        else:
            self.right.get_split()
            self.right.split(max_depth, min_size, depth + 1)


class MyDecisionTreeClassifier:

    def __init__(self, max_depth, min_size):
        self.max_depth = max_depth
        self.min_size = min_size
        self.root = None

    @staticmethod
    def gini(groups, classes):
        """
        A Gini score gives an idea of how good a split is by how mixed the
        classes are in the two groups created by the split.

        A perfect separation results in a Gini score of 0,
        whereas the worst case split that results in 50/50
        classes in each group result in a Gini score of 0.5
        (for a 2 class problem).
        """
        n_instances = float(sum([len(group) for group in groups]))
        gini = 0.0
        for group in groups:
            size = float(len(group))
            if size == 0:
                continue
            score = 0.0
            for class_val in classes:
                p = [row[-1] for row in group].count(class_val) / size
                score += p * p
            gini += (1.0 - score) * (size / n_instances)
        return gini

    def build_tree(self, dataset, target):
        """

        """
        gini, _, threshold, _ = Node.init_split(dataset)
        self.root = Node(dataset, target, gini)
        self.root.threshold = threshold
        self.root.get_split()
        self.root.split(self.max_depth, self.min_size, 1)

    def fit(self, X, y):
        # basically wrapper for build tree
        pass

    def predict(self, X_test):
        """
        """
        pass

    # Print a decision tree
    def print(self):
        self.print_tree(self.root)

    def print_tree(self, node: Node, depth=0):
        if not node:
            return
        if node.outcome is not None:
            print('%s[Terminal Node %s]' % (depth * '  ', node.outcome))
        else:
            print(f"{depth * '  '}[Feature {node.feature_index + 1} < {node.gini:.3f}]")
            self.print_tree(node.left, depth + 1)
            self.print_tree(node.right, depth + 1)


# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right


if __name__ == "__main__":
    tree = MyDecisionTreeClassifier(10, 1)
    my_ds, my_tg = [[[1, 1], [1, 0]], [[1, 1], [1, 0]]], [0, 1]
    ds = dataset_reader.reading_file("iris.csv")
    tree.build_tree(ds, [0, 1, 2])
    tree.print()
