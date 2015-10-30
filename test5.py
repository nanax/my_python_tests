"""input is a square list of lists representing an n x n sudoku puzzle and returns True if the input is a valid sudoku square and returns False otherwise."""
def check_sudoku(inli):
    n=len(inli)
    for j in range(n):
        for i in range(1,n+1):
            if i not in inli[j]:
                return False
    new=[]
    for a in range(n):
        new.append([inli[0][a]])
    for x in range(1,n):
        for b in range(n):
            new[b].append(inli[x][b])
    for j in range(n):
        for i in range(1,n+1):
            if i not in new[j]:
                return False
    return True