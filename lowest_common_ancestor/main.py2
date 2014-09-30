import sys


class Tree(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

# create the tree
leave_1 = Tree(10, None, None)
leave_2 = Tree(29, None, None)

branch_2 = Tree(20, leave_1, leave_2)
leave_3 = Tree(3, None, None)

branch_1 = Tree(8, leave_3, branch_2)
leave_4 = Tree(52, None, None)

root = Tree(30, branch_1, leave_4)


def lca(tree, value1, value2):
    if max(value1, value2) < tree.value:
        return lca(tree.left, value1, value2)
    elif min(value1, value2) > tree.value:
        return lca(tree.right, value1, value2)
    else:
        return tree.value


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    numbers = test.strip().split(' ')
    (value1, value2) = (int(numbers[0]), int(numbers[1]))
    print lca(root, value1, value2)

test_cases.close()
