def zero_matrix(mat): 
    #In the case we're given an array, and it contains a zero 
    if len(mat) < 1:
        for value in mat:
            value = 0
    
    row_one_cont_zero = False
    col_one_cont_zero = False

    #check if first row contains a zero
    if 0 in mat[0]:
        row_one_cont_zero = True
    
    #check if first column contains a zero
    for row in mat:
        if row[0] == 0:
            col_one_cont_zero = True
            break

    #identify all rows with at least 1 zero, save this information in zero_col column
    #identify all columns with a least 1 zero
    for row in range(1, len(mat)):
        if 0 in mat[row]:
            mat[row][0] = 0
        for col in range(1, len(mat[row])):
            if mat[row][col] == 0:
                mat[0][col] = 0

    #go through the entire matrix to find all zeroed rows and cols minues the first ones
    for row in range (1, len(mat)):
        if mat[row][0] == 0:                #if zero in row
            for column in range(1, len(mat[row])):         #clear all columns in the row
                mat[row][column] = 0
        else:
            for col in range(1, len(mat[row])):
                if mat[0][col] == 0:        #else go find the specific columns that are zeroed in this row
                    mat[row][col] = 0

    #zero first row if it was found to contain a zero
    if row_one_cont_zero:
        for column in mat[0]:
            column = 0

    #zero first column if it was found to contain a zero
    if col_one_cont_zero:
        for row in mat:
            row[0] = 0

    return mat

#This is O(M * N) time. 
#The first for loop iterates through each row, of which there are M, so O(M) time
#The second for loop with the nested for loop is approx. O(N * M) time as we iterate through N cols for each of the M rows
#The third for loop if likewise a nested for loop iterating through the same number of items, so O(N * M) time
#The last two if statements are O(1) time
#Summing these times together, the O(N * M) time absorbs all, resulting in O(N * M) time
#This is also O(1) space complexity as regardless of matrix size, we are always saving two boolean values as stored data

matr = [[1,1],
        [0,1],
        [1,1]]

zero_matrix(matr)

print(matr[0])
print(matr[1])
print(matr[2])