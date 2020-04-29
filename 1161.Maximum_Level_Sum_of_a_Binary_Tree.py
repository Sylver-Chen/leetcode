# Definition for a binary tree node.


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        # 由于题干要求层内元素之和，只需要遍历树一次，记录下每个节点的值与层数即可
        from collections import defaultdict

        value_dict = defaultdict(int)

        def inorder(node, level):
            if node is not None:
                inorder(node.left, level + 1)
                value_dict[level] += node.val
                inorder(node.right, level + 1)

        inorder(root, 1)
        return max(value_dict.items(), key=lambda x: (x[1], -x[0]))[0]
