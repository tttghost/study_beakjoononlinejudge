#백트래킹을 생각해보자

import os


def checkRow(row,n):
    for i in range(N):
        if board[row][i] == n:
            return False
    return True

def checkCol(col,n):
    for i in range(N):
        if board[i][col] == n:
            return False
    return True

def checkRect(row,col,n):
    rowStart=row//3*3
    colStart=col//3*3
    for i in range(rowStart,rowStart+3):
        for j in range(colStart,colStart+3):
            if board[i][j] == n:
                return False
    return True

def dfs(n):
    if n==len(empty_place):
        print('=================')
        print('\n'.join(' '.join(map(str,row)) for row in board))
        for i in board:
            print(i)
        exit(0)
        # return

    row=empty_place[n][0]
    col=empty_place[n][1]
    for i in range(1,N+1):
            if checkRow(row,i) and checkCol(col,i) and checkRect(row,col,i):
                board[row][col]=i
                dfs(n+1)
                board[row][col]=0


N=9
with open( os.path.dirname(os.path.realpath(__file__))+'/6_input.txt') as file:
    input=file.readline
    board=[list(map(int, i.split())) for i in file.readlines()]

empty_place=[]
for i in range(N):
    for j in range(N):
        if board[i][j]==0:
            empty_place.append([i,j])
print(empty_place)

print('\n'.join(' '.join(map(str,row)) for row in board))
# print('=================')
# print('\n'.join(' '.join(map(str,row)) for row in board))
dfs(0)