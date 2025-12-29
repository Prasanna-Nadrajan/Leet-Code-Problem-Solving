class Solution:
    def removeStars(self, s: str) -> str:
        st=[]
        for i in s:
            if i=='*' and st:
                st.pop()
            else:
                st.append(i)
        return "".join(st)
        
