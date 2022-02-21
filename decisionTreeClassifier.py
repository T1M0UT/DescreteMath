# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# from sklearn.datasets import load_iris
# from sklearn.model_selection import cross_val_score
# from sklearn.tree import DecisionTreeClassifier
# from sklearn import tree
# from sklearn.model_selection import train_test_split
#
#
# class Node:
#
#     def __init__(self, X, y, gini):
#         self.X = X
#         self.y = y
#         self.gini = gini
#         self.feature_index = 0
#         self.threshold = 0
#         self.left = None
#         self.right = None
#
#
# class MyDecisionTreeClassifier:
#
#     def __init__(self, max_depth):
#         self.max_depth = max_depth
#
#     def gini(self, groups, classes):
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
#     def build_tree(self, X, y, depth=0):
#         # create a root node
#
#         # recursively split until max depth is not exeeced
#
#         pass
#
#     def fit(self, X, y):
#         # basically wrapper for build tree
#
#         pass
#
#     def predict(self, X_test):
#         # traverse the tree while there is left node
#         # and return the predicted class for it,
#         # note that X_test can be not only one example
#
#         pass
#
# from sklearn.datasets import load_iris
# tree_ = MyDecisionTreeClassifier(6)
# print(tree_.gini([[[1, 1], [1, 0]], [[1, 1], [1, 0]]], [0, 1]))
# print(tree_.gini([[[1, 0], [1, 0]], [[1, 1], [1, 1]]], [0, 1]))
#
