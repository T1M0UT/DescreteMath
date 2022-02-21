# from numpy import inf
# from sklearn.datasets import load_iris
#
#
# class Node:
#
#     def __init__(self, dataset, target, gini):
#         self.dataset = dataset
#         self.target = target
#         self.gini = gini
#         self.feature_index = 0
#         self.threshold = 0
#         self.left = None
#         self.right = None
#
#     @staticmethod
#     def my_kostil_get_split(dataset):
#         # TODO: Get rid of extra lines - refactor
#         class_values = list(set(row[-1] for row in dataset))
#         b_index, b_value, b_score, b_groups = inf, inf, inf, None
#         for index in range(len(dataset[0]) - 1):
#             for row in dataset:
#                 groups = test_split(index, row[index], dataset)
#                 gini = MyDecisionTreeClassifier.gini(groups, class_values)
#                 if gini < b_score:
#                     b_score = gini
#                     _, b_value, _ = index, row[index], groups
#         threshold = b_value
#         best_gini = b_score
#         return best_gini, float(threshold)
#
#     # Select the best split point for a dataset
#     def get_split(self, dataset):
#         class_values = list(set(row[-1] for row in dataset))
#         b_index, b_value, b_score, b_groups = inf, inf, inf, None
#         for index in range(len(dataset[0]) - 1):
#             for row in dataset:
#                 groups = test_split(index, row[index], dataset)
#                 gini = MyDecisionTreeClassifier.gini(groups, class_values)
#                 if gini < b_score:
#                     b_score = gini
#                     b_index, b_value, b_groups = index, row[index], groups
#         self.left = Node(b_groups[0], self.target, b_score)
#         self.left.feature_index = b_index
#         self.left.threshold = b_value
#         self.right = Node(b_groups[1], self.target, b_score)
#         self.right.feature_index = b_index
#         self.right.threshold = b_value
#         # return {'index': b_index, 'value': b_value, 'groups': b_groups}
#
#     # Create a terminal node value
#     def to_terminal(self, group):
#         # TODO: now this probably doesn't work: check and rewrite
#         outcomes = [row[-1] for row in group]
#         return max(set(outcomes), key=outcomes.count)
#
#     # Create child splits for a node or make terminal
#     def split(self, max_depth, depth):
#         # TODO: Make OOP code out of this
#         left, right = node['groups']
#         del (node['groups'])
#
#         if not left or not right:
#             node['left'] = node['right'] = to_terminal(left + right)
#             return
#
#         if depth >= max_depth:
#             node['left'], node['right'] = to_terminal(left), to_terminal(right)
#             return
#         node['left'] = get_split(left)
#         split(node['left'], max_depth, depth + 1)
#         node['right'] = get_split(right)
#         split(node['right'], max_depth, depth + 1)
#
# class MyDecisionTreeClassifier:
#
#     def __init__(self, max_depth):
#         self.max_depth = max_depth
#         self.root = None
#
#     @staticmethod
#     def gini(groups, classes):
#         """
#         A Gini score gives an idea of how good a split is by how mixed the
#         classes are in the two groups created by the split.
#
#         A perfect separation results in a Gini score of 0,
#         whereas the worst case split that results in 50/50
#         classes in each group result in a Gini score of 0.5
#         (for a 2 class problem).
#         """
#         # count all samples at split point
#         n_instances = float(sum([len(group) for group in groups]))
#         # sum weighted Gini index for each group
#         gini = 0.0
#         for group in groups:
#             size = float(len(group))
#             # avoid divide by zero
#             if size == 0:
#                 continue
#             score = 0.0
#             # score the group based on the score for each class
#             for class_val in classes:
#                 p = [row[-1] for row in group].count(class_val) / size
#                 score += p * p
#             # weight the group score by its relative size
#             gini += (1.0 - score) * (size / n_instances)
#         return gini
#
#     def split_data(self, X, y) -> tuple[int, int]:
#         # test all the possible splits in O(N^2)
#         # return index and threshold value
#         pass
#
#     def build_tree(self, dataset, target, depth = 0):
#         # create a root node
#
#         # recursively split until max depth is not exeeced
#         gini, threshold =  Node.my_kostil_get_split(dataset)
#         self.root = Node(dataset, target, gini)
#         self.root.threshold = threshold
#         self.root.get_split(dataset)
#         # TODO: split(self.root, depth, 1)
#
#     def fit(self, X, y):
#         # basically wrapper for build tree
#         pass
#
#     # TODO: understand what predict does and implement the method
#     def predict(self, X_test):
#         # traverse the tree while there is left node
#         # and return the predicted class for it,
#         # note that X_test can be not only one example
#
#         pass
#
#     # Print a decision tree
#     def print(self):
#         self.print_tree(self.root)
#
#     def print_tree(self, node: Node, depth=0):
#         if node:
#             print('%s[X%d < %.3f]' % (depth * '  ', (node.feature_index + 1), node.gini))
#             self.print_tree(node.left, depth + 1)
#             self.print_tree(node.right, depth + 1)
#         else:
#             print('%s[%s]' % (depth * '  ', node))
#
#
# # Split a dataset based on an attribute and an attribute value
# # TODO: test_split?
# def test_split(index, value, dataset):
#     left, right = list(), list()
#     for row in dataset:
#         if row[index] < value:
#             left.append(row)
#         else:
#             right.append(row)
#     return left, right
#
#
#
#
# # dataset = [[2.771244718, 1.784783929, 0],
# #            [1.728571309, 1.169761413, 0],
# #            [3.678319846, 2.81281357, 0],
# #            [3.961043357, 2.61995032, 0],
# #            [2.999208922, 2.209014212, 0],
# #            [7.497545867, 3.162953546, 1],
# #            [9.00220326, 3.339047188, 1],
# #            [7.444542326, 0.476683375, 1],
# #            [10.12493903, 3.234550982, 1],
# #            [6.642287351, 3.319983761, 1]]
# # tree = build_tree(dataset, 10)
# # print_tree(tree)
#
# iris = load_iris()
# print(dir(iris))
# tree_ = MyDecisionTreeClassifier(6)
# my_ds, my_tg = [[[1, 1], [1, 0]], [[1, 1], [1, 0]]], [0, 1]
# tree_.build_tree(iris['data'], iris['target'])
# tree_.print()
