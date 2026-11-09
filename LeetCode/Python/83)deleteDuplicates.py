        # """
        # :type head: Optional[ListNode]
        # :rtype: Optional[ListNode]
        # """

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteDuplicates(head):

    currNode = head
    nextNode = head.next
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