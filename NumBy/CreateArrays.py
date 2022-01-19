import numpy as np;

arr= np.array([1,2,3,4,5]);

print(arr[2]);

print(arr[2] + arr[3])
print(type(arr))
# Access 2-D arrays 

arr2_D=np.array([[1,2,3,4,5],[6,7,8,9,10]]);


print("Arrays 2_D",arr2_D );
print("Arrays 2_D element",arr2_D[1,1] );
print('5th element on 2nd row: ', arr2_D[1, 4])
# Access 3-D arrays

arr3_D= np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]);
#Vector

print("Arrays 3_D",arr3_D );

print(arr3_D[0, 1, 2]);

# Negative Indexing

print('Last element from 2nd dim: ', arr2_D[1, -1]);
