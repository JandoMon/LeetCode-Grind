        # """
        # :type head: Optional[ListNode]
        # :rtype: Optional[ListNode]
        # """

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteDuplicates(head):
    #base case if the list is empty
    if not head: 
        return head
    #currentNode keeps tracks of the current Node. 
    #nextNode will look ahead for nodes that are duplicates.
    currNode = head
    nextNode = head.next

    #Loop/Main Logic
    #While there is still space to see the nextNode:
    #Do the following:
    #Compare the nextNode with the currentNode
    #If they are the same then we will iterate and keep looking ahead until they are not the same. 
    #Then set the currentNode.next to the next instance the node is different. 
    while nextNode:
        if currNode.val == nextNode.val:
            while nextNode and currNode.val == nextNode.val:
                nextNode = nextNode.next
            currNode.next = nextNode
        currNode = currNode.next
    return head

head1 = ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(3)))))
header = deleteDuplicates(head1)
current = header
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")


#Need to google the optimal solution if one exists 