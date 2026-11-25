# 1. Standard LeetCode TreeNode definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2. Helper function to build a binary tree from LeetCode's array format
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:

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
    while right and left:
        #Compare the values
        if (right ^ left) or (right.val != left.val): 
            return False
        #if both values are null
        elif not right and not left:
            #Go back
            right = stack.pop()
            left = stack.pop()
            #Go in the opposite direction
            left = left.right
            right = right.left 
        #if there are more things to traverse
        else:
            #Add to the stack
            stack.append(left)
            stack.append(right)
            #Go to the next node 
            left = left.left
            right = right.right
    return True 
        

p = [1,2,2,3,4,4,3]
tree_p = build_tree(p)
print(isSymmetric(tree_p))