
public class TwoSum {
    public int[] twoSum(int[] nums, int target) {

        int val1, val2, sum; 
        int[] ans = {-1, -1}; 
        for(int head = 0; head <= nums.length/2; head++)
        {
            for(int tail = nums.length-1; tail > head; tail--)
            {
                val1 = nums[head];
                val2 = nums[tail];
                sum = val1 + val2;
                if(sum == target)
                {
                    ans = new int[] {head, tail};
                }
            }
        }
        return ans; 
    }
}