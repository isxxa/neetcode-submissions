# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Planning: 
        - we are inverting a binary tree and returning its root example on the leftl
        - looking at the tree it looks like each nodes children are flipping with each other
        - node = 1 : left = 2 right = 3 should use a temp val
        - node = 1 : temp = left, left = right, right = temp
        - move to next node = 3: left = 6, right = 7
        - node = 3: temp = left, left = right, right = temp 
        - this is all recursive
        continue with left child first

        '''

        # we use root.val to get the node of the binary tree
        # val.next to get to next child, will always be left node

        '''
        temp = node.left
        node.left = node.right
        node.right = temp

        or 

        node.left, node.right = node.right, node.left
        '''

        '''
        steps: 
        1. if node is none, return none
        2. swap the nodes left and right children
        3. recursively invert the left subtree
        4. recursively invert the right subtree
        5. return the node
        '''

        if root is None: 
            return None

        #swap children
        root.left, root.right = root.right, root.left

        #recurse
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root