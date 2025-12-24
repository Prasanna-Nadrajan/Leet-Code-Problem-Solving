class Solution {
    public boolean isSubsequence(String s, String t) {
        int i=0,j=0;
        int sl=s.length(),tl=t.length();
        while(i<sl && j<tl){
            while(j<tl && t.charAt(j)!=s.charAt(i)){
                j++;
            }
            if(j==tl) return false;
            i++;
            j++;
        }
        if(i==sl) return true;
        else return false;
    }
}
