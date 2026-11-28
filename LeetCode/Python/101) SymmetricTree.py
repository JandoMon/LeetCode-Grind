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


#Idea we have a left and right tree pointer and that will traverse and compare. If at any point they do not match then they will 
#     """
#     :type root: Optional[TreeNode]
#     :rtype: bool
#     """
#something is not working ?

def isSymmetric(root):
    right =  root
    left = root 
    stack = []
    stack_Val = []
    while right and left:
        #Compare the values
        if (right is None)  ^ (left is None) or (right.val != left.val): 
            return False
        #if both values are null
        elif not right and not left:
            #Go back
            right = stack.pop()
            left = stack.pop()
            right_val = stack_Val.pop()
            left_val = stack_Val.pop()
            #Go in the opposite direction
            left = left.right
            right = right.left 
            left_val =left.val
            right = right.val
        #if there are more things to traverse
        else:
            #Add to the stack
            stack.append(left)
            stack.append(right)
            stack_Val.append(left.val)
            stack_Val.append(right.val)
            #Go to the next node 
            left = left.left
            right = right.right
    return True 
        

p = [1,2,2,3,4,4,3]
p2 = [1,2,2,null,3,null,3]
tree_p = build_tree(p2)
print(isSymmetric(tree_p))

# I bought something so expensive
