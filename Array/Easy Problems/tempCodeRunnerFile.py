for i in range(n):
        total+=mat[i][i]
        if i!=n-1-i:
            total+=mat[i][n-1-i] # avoid double count
    retu