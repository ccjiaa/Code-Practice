
def rotate_matrix(mat):
    #base case
    mat_length = len(mat)
    if mat_length < 2:
        return mat
    
    #reverses orders of rows in matrix
    for row in range(len(mat)//2 + 1):
        temp = mat[len(mat) - row - 1]
        mat[len(mat) - row - 1] =  mat[row]
        mat[row] = temp

    #exchange values across the diagonal from top left to bottom right
    for row in range (len(mat)):
        for col in range(row + 1, len(mat)):
            temp = mat[row][col]
            mat[row][col] = mat[col][row]
            mat[col][row] = temp

    return mat

#This is O(N^2) time, which is also the minimum time since we at least need to go over each spot in the matrix once
#The first for loop is O(N) time, since it does constant work on N rows
#The second for loop is O(N^2) time, since it iterates in a way that does n bits of constant work the first loop, n -1 on the second, etc, until 1
#The sum from N to 1 (or conversely 1 to N) is N^2, thus O(N^2) time
#The O(N^2) time absorbs the O(N) loop since it's addition, so total is O(N^2) time
#In the first loop, we keep entire rows as temp variables, so it is O(N) space complexity

matr = [[1,2,3],
        [4,5,6],
        [7,8,9]]

rotate_matrix(matr)

print(matr[0])
print(matr[1])
print(matr[2])
