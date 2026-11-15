from collections import deque
from typing import List, Optional

# 1. Standard LeetCode TreeNode definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2. Helper function to build a binary tree from LeetCode's array format
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        current = queue.popleft()
        
        # Assign left child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        
        # Assign right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
        
    return root



def inorderTraversal(root):
    curr = root
    stack = []
    stackVal = []
    inOrder = []
    while curr or stack:
        if not curr: 
            curr = stack.pop()
            recordedVal = stackVal.pop()
            inOrder.append(curr.val)
            curr = curr.right 
        else:
            stack.append(curr)
            stackVal.append(curr.val)
            curr = curr.left 
    return inOrder

tree1 = build_tree([1, None, 2, 3])
print(inorderTraversal(tree1))

