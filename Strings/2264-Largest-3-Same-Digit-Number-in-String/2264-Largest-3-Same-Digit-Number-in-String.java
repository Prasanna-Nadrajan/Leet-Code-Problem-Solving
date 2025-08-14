class Solution {
    static boolean check(String s){
        Set<Character> c=new HashSet<>();
        for(int i=0;i<s.length();i++){
            c.add(s.charAt(i));
        }
        return (c.size()==1);
    }

    public String largestGoodInteger(String num) {
        String res="";
        int l=0;
        int r=3;
        while(r<=num.length()){
            String ts=num.substring(l,r);
            if(check(ts)){
                if(res.equals("")||(Integer.parseInt(res)<Integer.parseInt(ts))){
                    res=num.substring(l,r);
                }
            }
            l++;
            r++;
        }
        return res;
    }
}
