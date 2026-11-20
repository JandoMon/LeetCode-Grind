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



# """
# :type p: Optional[TreeNode]
# :type q: Optional[TreeNode]
# :rtype: bool
# """
def isSameTree(p, q):
    curr_p = p
    curr_q = q
    stack_p = []
    stack_q = []

    while (curr_p and curr_q) or (stack_p and stack_q):
        if (not curr_q) ^ (not curr_p):
            return False
        elif not curr_q and not curr_p:
            curr_p = stack_p.pop()
            curr_q = stack_q.pop()
            val_q = curr_q.val
            val_p = curr_p.val
            if val_q !=  val_p:
                return False   
            curr_p = curr_p.right
            curr_q = curr_q.right
        else:
            stack_q.append(curr_q)
            stack_p.append(curr_p)
            curr_q = curr_q.left
            curr_p = curr_p.left

    if curr_p or curr_q or stack_p or stack_q:
        return False
    return True

p = [1,2,3]
q = [1]

tree_p = build_tree(p)
tree_q = build_tree(q)
print(isSameTree(tree_p, tree_q))

# Optimal Solution:
#  Iterative BFS (Using a Queue)
#  Need to look into it
#  researching bst traversing dfs and bfs 
# i am O_o
# GTA 6 is out!!! yippie

