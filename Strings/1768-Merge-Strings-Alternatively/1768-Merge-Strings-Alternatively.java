class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder ans=new StringBuilder();
        int w1=word1.length();
        int w2=word2.length();
        int i=0,j=0;
        char[] wo1=word1.toCharArray();
        char[] wo2=word2.toCharArray();
        while(i<w1 && j<w2){
            ans.append(wo1[i++]);
            ans.append(wo2[j++]);
        }
        while(i<w1){
            ans.append(wo1[i++]);
        }
        while(j<w2){
            ans.append(wo2[j++]);
        }
        return ans.toString();
    }
}
