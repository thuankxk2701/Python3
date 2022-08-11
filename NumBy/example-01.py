import numpy as np

### Basic
# _A = [[1, 2], [4, 5], [6, 7]]
# # _B = [[2, 3, 5], [7, 9, 11]]

# A = np.array(_A)
# # B = np.array(_B)
# # print(A)

# # print(A[0, 0])
# # print(A[:, 0])
# # print(A[0, :])

# # print('A+B: \n', A+B)
# # print('AxB: \n', A*B)

# # Nhan matrix with vector

# _vtA = [[1, 2], [3, 4]]

# vtA = np.array(_vtA)

# # print('A*vtA : \n',A.dot(vtA))

# _B = np.eye(5)

# print(_B == 1)


#Advance


_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

A = np.array(_A)

A_i = np.linalg.pinv(A)

print(A_i)
