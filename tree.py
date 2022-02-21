"""
Tymur Krasnianskyi
Yaryna Fialko
Descrete Math Lab 1
18.02.2022
"""
from numpy import inf


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
    def my_kostil_get_split(dataset):
        # TODO: Get rid of extra lines - refactor
        class_values = list(set(row[-1] for row in dataset))
        b_index, b_value, b_score, b_groups = inf, inf, inf, None
        for index in range(len(dataset[0]) - 1):
            for row in dataset:
                groups = test_split(index, row[index], dataset)
                gini = MyDecisionTreeClassifier.gini(groups, class_values)
                if gini < b_score:
                    b_score = gini
                    _, b_value, _ = index, row[index], groups
        threshold = b_value
        best_gini = b_score
        return best_gini, float(threshold)

    # Select the best split point for a dataset
    def get_split(self):
        class_values = list(set(row[-1] for row in self.dataset))
        best_index, b_value, best_gini, b_groups = inf, inf, inf, None
        if len(self.dataset) < 1:
            return
        for index in range(len(self.dataset[0]) - 1):
            for row in self.dataset:
                groups = test_split(index, row[index], self.dataset)
                gini = MyDecisionTreeClassifier.gini(groups, class_values)
                if gini < best_gini:
                    best_gini = gini
                    best_index, b_value, b_groups = index, row[index], groups
        if best_gini == 0.0:
            self.to_terminal()
            return
        self.feature_index = best_index
        self.left = Node(b_groups[0], self.target, best_gini)
        # self.left.feature_index = b_index
        self.left.threshold = b_value
        self.right = Node(b_groups[1], self.target, best_gini)
        # self.right.feature_index = b_index
        self.right.threshold = b_value

    # Create a terminal node value
    def to_terminal(self, group=None):
        # TODO: now this probably doesn't work: check and rewrite
        if group:
            outcomes = [row[-1] for row in group]
        else:
            outcomes = [row[-1] for row in self.dataset]

        if not outcomes:
            self.outcome = 999
            return
        self.outcome = max(set(outcomes), key=outcomes.count)

    # Create child splits for a node or make terminal
    def split(self, max_depth, min_size, depth):
        """

        """
        # if self.gini == 0.0:
        #     self.to_terminal()
        #     return
        # if round(self.left.gini, 1) <= 0.0:
        #     self.left.to_terminal()
        #     return
        # if round(self.right.gini, 1) <= 0.0:
        #     self.right.to_terminal()
        #     return
        if self.gini == 0.0:
            self.to_terminal()

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
        # count all samples at split point
        n_instances = float(sum([len(group) for group in groups]))
        # sum weighted Gini index for each group
        gini = 0.0
        for group in groups:
            size = float(len(group))
            # avoid divide by zero
            if size == 0:
                continue
            score = 0.0
            # score the group based on the score for each class
            for class_val in classes:
                p = [row[-1] for row in group].count(class_val) / size
                score += p * p
            # weight the group score by its relative size
            gini += (1.0 - score) * (size / n_instances)
        return gini

    def split_data(self, X, y) -> tuple[int, int]:
        # test all the possible splits in O(N^2)
        # return index and threshold value
        pass

    def build_tree(self, dataset, target):
        # create a root node

        # recursively split until max depth is not exeeced
        gini, threshold = Node.my_kostil_get_split(dataset)
        self.root = Node(dataset, target, gini)
        self.root.threshold = threshold
        self.root.get_split()
        self.root.split(self.max_depth, self.min_size, 1)

    def fit(self, X, y):
        # basically wrapper for build tree
        pass

    def predict(self, X_test):
        # traverse the tree while there is left node
        # and return the predicted class for it,
        # note that X_test can be not only one example
        pass

    # Print a decision tree
    def print(self):
        self.print_tree(self.root)

    def print_tree(self, node: Node, depth=0):
        if not node:
            return
        # if node.outcome:
        #     print('%s[Terminal Node %s]' % (depth * '  ', node.outcome))
        # elif node:
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





# dataset = [[2.771244718, 1.784783929, 0],
#            [1.728571309, 1.169761413, 0],
#            [3.678319846, 2.81281357, 0],
#            [3.961043357, 2.61995032, 0],
#            [2.999208922, 2.209014212, 0],
#            [7.497545867, 3.162953546, 1],
#            [9.00220326, 3.339047188, 1],
#            [7.444542326, 0.476683375, 1],
#            [10.12493903, 3.234550982, 1],
#            [6.642287351, 3.319983761, 1]]
# tree = build_tree(dataset, 10)
# print_tree(tree)

tree = MyDecisionTreeClassifier(10, 1)
my_ds, my_tg = [[[1, 1], [1, 0]], [[1, 1], [1, 0]]], [0, 1]
import dataset_reader
ds = dataset_reader.reading_file("iris.csv")
tree.build_tree(ds, [0, 1, 2])
tree.print()
