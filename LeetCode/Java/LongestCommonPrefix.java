public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) 
    {
        String ans = "";
        //Find the smallest word in the array
        String smallWord = strs[0];
        for(int index = 0; index < strs.length; index++)
        {
            if(smallWord.length()>strs[index].length())
            {
                smallWord = strs[index];
            }
        }

        //Compares the smallest word with the list ß
        for(int i = 0; i < smallWord.length(); i++)
        {
            for(int j =0; j < strs.length; j++)
            {
               if(!(smallWord.charAt(i) == strs[j].charAt(i)))
                {
                    return ans;  
                }  
                   
            }  
            ans += smallWord.charAt(i);  
            
        }
        return ans;
    }
    
}
/*Optimized Solution */
/*https://leetcode.com/problems/longest-common-prefix/solutions/3273176/python3-c-java-19-ms-beats-9991-by-abdul-h6yc */