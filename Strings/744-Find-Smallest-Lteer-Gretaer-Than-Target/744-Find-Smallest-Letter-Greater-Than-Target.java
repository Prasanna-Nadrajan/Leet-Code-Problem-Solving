class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        char ans=letters[0];
        boolean found=false;
        for(char i:letters){
            if(i>target){ 
                ans=i;
                break;
            }
        }
        return ans;
    }
}
