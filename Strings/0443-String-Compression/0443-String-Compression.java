class Solution {
    public int compress(char[] chars) {
        int r=0,w=0,n=chars.length,count=0;
        char curr;
        while(r<n){
            curr=chars[r];
            count=0;
            while(r<n && chars[r]==curr){
                count++;
                r++;
            }
            chars[w++]=curr;
            if(count>1){
                for(char j:String.valueOf(count).toCharArray()){
                    chars[w++]=j;
                }
            }
        }
        return w;
    }
}
