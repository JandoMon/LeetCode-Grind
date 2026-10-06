import java.util.HashSet;

public class RemoveDuplicates{
    public int removeDuplicates(int[] nums)
    {
        int uniqueValues = 0;  
        int pointer = 0; 
        HashSet<Integer> values = new HashSet<Integer>();
        for(int index=0; index< nums.length; index++)
        {
            if(!(values.contains(nums[index])))
            {
                uniqueValues++;
                values.add(nums[index]); 
                nums[pointer] = nums[index]; 
                pointer++; 
            }
            
        }

        for (int num : nums) {
            System.out.print(num + " "); 
        }

        System.out.println(""); 
        return uniqueValues;
    }
}
