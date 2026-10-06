public class MergeTwoList {
    public ListNode mergeTwoList(ListNode list1, ListNode list2)
    {
        ListNode oneCurr = list1; 
        ListNode twoCurr = list2;
        ListNode headFinal = new ListNode(); 
        ListNode currNode = headFinal; 

        //while both list still have nodes
        while(oneCurr != null && twoCurr != null)
        {
            if(oneCurr.val < twoCurr.val)
            {
                currNode.next = new ListNode(oneCurr.val, null);
                oneCurr = oneCurr.next; 
                currNode = currNode.next; 
            }
            else
            {
                currNode.next = new ListNode(twoCurr.val, null);
                twoCurr = twoCurr.next; 
                currNode = currNode.next; 
            }

        }

        //list 1 still has nodes
        if(oneCurr != null)
        {
            currNode.next = oneCurr; 
        }//list 2 still has nodes
        else if(twoCurr != null)
        {
            currNode.next = twoCurr; 
        }

        return headFinal.next; 
    }
    
}
