import java.util.Stack;

public class ValidParentheses {

    public boolean isValid(String s)
    {
        Stack<Character> parentOrder = new Stack<>();

        for(int i = 0; i < s.length(); i++)
        {
            if(s.charAt(i) == '{')
            {
                parentOrder.push('}');
            }
            else if(s.charAt(i)== '(')
            {
                parentOrder.push(')'); 
            }
            else if(s.charAt(i)== '[')
            {
                parentOrder.push(']');
            }
            else if(parentOrder.size() == 0 || parentOrder.pop() != s.charAt(i))
            {
                return false; 
            }
        }
        return (parentOrder.size() == 0); 
    }
    
}
