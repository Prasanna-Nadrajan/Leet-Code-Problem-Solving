import java.util.*;
class Solution {
    public int repeatedNTimes(int[] nums) {
        Map<Integer,Integer> map=new HashMap<>();
        for(int i:nums){
            if(map.containsKey(i)){
                return i;
            }
            else{
                map.put(i,1);
            }
        }
        return -1;
    }
}
