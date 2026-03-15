def gridSearch(G, P):
    # Write your code here
    lr=len(G)
    lc=len(G[0])
    gr=len(P)
    gc=len(P[0])
    for i in range(lr):
        for j in range(lc):
            if (j+gc)<=lc and G[i][j:gc+j] == P[0]:
                flag=True
                if (i+gr)<=lr:
                    for r in range(i+1,i+gr):
                        if (G[r][j:gc+j]!=P[r-i]):
                            flag=False
                    if flag:
                        return "YES"
    return "NO"
