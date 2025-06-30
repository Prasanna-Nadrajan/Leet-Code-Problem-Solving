class Solution:
    def isValid(self, s: str) -> bool:
        flag=True
        st=[]
        for i in s:
            if i == '(' or i=='{' or i=='[':
                st.append(i)
            if i == ')':
                try:
                    if st[-1]=='(':
                        st.pop()
                    else:
                        return False
                except:
                    return False
            elif i=='}':
                try:
                    if st[-1]=='{':
                        st.pop()
                    else:
                        return False
                except:
                    return False
            elif i==']':
                try:
                    if st[-1]=='[':
                        st.pop()
                    else:
                        return False
                except:
                    return False
        if st:
            return False
        return True
