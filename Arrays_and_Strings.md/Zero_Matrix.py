
# coding: utf-8

# In[36]:


import numpy as np
matrix=[[1, 4, 5, 12, 14], 
    [-5, 8, 9, 0, 17],
    [-6, 0, 11, 19, 21]]
rows=[]
cols=[]
m=len(matrix)
n=len(matrix[0])

for i in range(m):
    for j in range(n):
        if matrix[i][j]==0:
            rows.append(i)
            cols.append(j)
       

#     print(rows)
# print('----')
# print(cols)

def nullify_col(col):
    for i in range(len(matrix)):
        matrix[i][col]=0
        
def nullify_row(row):
    for i in range(len(matrix[0])):
        matrix[row][i]=0
        
for row in rows:
    nullify_row(row)
for col in cols:
    nullify_col(col)
    


matrix
    

