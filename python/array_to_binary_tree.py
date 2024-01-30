from typing import List
from typing import Optional

# Solution explanation:

# This solution uses a binary tree algorithm to organize items. The execution time is O(n), but it can be O(n log n) because of tree complexity

class TreeNode:
    def __init__(self, val=int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root: TreeNode):
        self.root = root

    def __insert__(self, parent: TreeNode, child: TreeNode):
        if parent is None: return child
        if child.val < parent.val: parent.left = self.__insert__(parent=parent.left, child=child)
        else: parent.right = self.__insert__(parent=parent.right, child=child)
        return parent

    def append(self, child: TreeNode):
        self.__insert__(parent=self.root, child=child)

    def getRoot() -> TreeNode: 
        return self.root

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        binaryTree = None
        for num in nums:
            node = TreeNode(val=num)
            if binaryTree is None: 
                binaryTree = BinaryTree(root=node)
            else: 
                binaryTree.append(node)

        return binaryTree.root

        

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val, end=" ")
        in_order_traversal(root.right)

printList = []
nums = [3,5,8]
tree = Solution().sortedArrayToBST(nums)
in_order_traversal(root=tree)
print(printList)




