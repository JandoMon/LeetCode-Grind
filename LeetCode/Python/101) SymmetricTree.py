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
def isSymmetric(root):
    right =  root
    left = root 

    while right and left:
        #if the right and left are not the same then return false
        if (right ^ left) or (right.val != left.val): 
            return False
        #if both values are null
        elif not right and not left:
            return False
    return True 
        

p = [1,2,2,3,4,4,3]
tree_p = build_tree(p)
print(isSymmetric(tree_p))