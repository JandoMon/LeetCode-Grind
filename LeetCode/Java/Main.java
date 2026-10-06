public class Main {
    public static void main(String[] args) {
       /* // Example: Two Sum problem
        TwoSum twoSum = new TwoSum();
        int[] nums = {2, 15, 11, 7};
        int target = 9;
        int[] result = twoSum.twoSum(nums, target);
        //System.out.println("Two Sum result: " + java.util.Arrays.toString(result)); // Print indices
        
        // Example: Palindrome check
        int intPalindrome = 123454321;
        Palindrome palindrome = new Palindrome();
        boolean isPalindrome = palindrome.isPalindrome(intPalindrome); // Pass intPalindrome, not target
        //System.out.println("Is " + intPalindrome + " a palindrome? " + isPalindrome); // Print result

        // Example: RomanInteger 
        RomanInteger romanInteger = new RomanInteger();
        String romanString = "D";
        int romanInt = romanInteger.romantInt(romanString);
        //System.out.println("The value of the roman integer is:" + romanInt); 

        //Example: LongestCommonPrefix
        LongestCommonPrefix longestCommonPrefix = new LongestCommonPrefix();
        String[] strs = {"flower","flow","flight"};
        String LongCommonPre = longestCommonPrefix.longestCommonPrefix(strs);
        //System.out.println("The longest common prefix is: " + LongCommonPre); 

        //Example: isValidParentheses
        ValidParentheses validParentheses = new ValidParentheses();
        String isValidParent = "((";
        boolean isValidParenteses = validParentheses.isValid(isValidParent);
        //System.out.println("The string is: " + (isValidParenteses? "Valid": "not Valid")); 

        //Example MergeTwoList
        MergeTwoList mergeTwoList = new MergeTwoList();
        //First ListNode List
        ListNode head1 = new ListNode(1, new ListNode(2, new ListNode(4)));

        //Second ListNode List
        ListNode head2 = new ListNode(1, new ListNode(3, new ListNode(4)));

        System.out.println("\nThe new Merge List is: " );
        MergeTwoList mergetwolist = new MergeTwoList(); 
        ListNode answer = mergeTwoList.mergeTwoList(head1, head2);
        
        //print Linked List
        ListNode currNode = answer ; 
        while(currNode != null)
        {
            currNode.printNode();
            currNode = currNode.next; 
        } 
            */
        
        //Example: removeDuplicates
        RemoveDuplicates removeduplicates = new RemoveDuplicates(); 
        int[] array = new int[]{1,1,2}; 
        int unique = removeduplicates.removeDuplicates(array);
        System.out.println("Number of Unique Values: " + unique ); 

    }
}