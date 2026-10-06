public class Palindrome{
    public boolean isPalindrome(int x) {
        String intString = String.valueOf(x);
        boolean isPalidrome= true;  
        char head,tail; 
        if(intString.length() ==1) {return false;}
        for(int index= 0; index < intString.length() /2; index++)
        {
            head = intString.charAt(index);
            tail = intString.charAt(intString.length()-1-index);
            if(!(head==tail))
            {
                isPalidrome = false; 
            }
        }
        return isPalidrome; 
    }
}
    /*Optimized Solution*/
    /*
    https://leetcode.com/problems/palindrome-number/solutions/6044650/video-using-remainder-by-niits-fif6
    */