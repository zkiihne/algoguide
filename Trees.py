


# Example problem https://leetcode.com/problems/validate-binary-search-tree/submissions/
def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkNode(node, constraintmin, constraintmax):
            val = node.val
            if val <= constraintmin or val >= constraintmax:
                return False
            if node.left != None and node.right != None:
                return min(checkNode(node.left, constraintmin, val), checkNode(node.right, val, constraintmax))
            elif node.left != None:
                return checkNode(node.left, constraintmin, val)
            elif node.right != None:
                return checkNode(node.right, val, constraintmax)
            else:
                return True
        return checkNode(root, float("-inf"), float("inf"))
