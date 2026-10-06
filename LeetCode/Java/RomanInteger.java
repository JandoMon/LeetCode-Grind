import java.util.HashMap;

public class RomanInteger {
    public int romantInt(String s){
        HashMap <Character, Integer> romanVal = new HashMap<>();  
        romanVal.put('I',1); 
        romanVal.put('V',5);
        romanVal.put('X',10);
        romanVal.put('L',50);
        romanVal.put('C',100);
        romanVal.put('D',500);
        romanVal.put('M',1000);

        char prevChar = ' ';
        char currChar = ' ';
        int sum =0; 
        //if the length is 1s
        if(s.length() ==1 ) {return romanVal.get(s.charAt(0));}

        //
        for(int index=s.length()-1; index >= 0; index--)
        {
            currChar = s.charAt(index); 
            if(index != s.length()-1) {prevChar = s.charAt(index+1);}
            if(prevChar != ' '  && romanVal.get(currChar) < romanVal.get(prevChar))
            {
                sum -= romanVal.get(currChar); 
            }
            else{sum += romanVal.get(currChar);}
        }

        return sum; 
    }
    
}
