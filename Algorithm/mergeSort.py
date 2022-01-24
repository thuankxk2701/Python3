import math

def merge(arr1,arr2):
    result=[];
    i=0;
    j=0;
    while i<len(arr1)and j<len(arr2):
        if(arr1[i] > arr2[j]):
            result.append(arr2[j]);
            j+=1;
        else:
            result.append(arr1[i]);
            i+=1;
    while (i<len(arr1)):
        result.append(arr1[i]);
        i+=1;
    while (j<len(arr2)):
        result.append(arr2[j]);
        j+=1;
    return result;
def mergeSort(arr):
    if (len(arr) <= 1):
        return arr;
    mid=math.floor(len(arr)/2);
    left=mergeSort(arr[0:mid]);
    right=mergeSort(arr[mid:]);
    return merge(left,right);

print(merge([1,4,7,3],[5,6,9,2]))

print(mergeSort([21, 23, 41, 53, 123, 41, 2, 12, 42]))

# import math

# def merge(arr1,arr2):
#     i=0;
#     j=0;
#     while i<len(arr1)and j<len(arr2):
#         if(arr1[i] > arr2[j]):
#             yield arr2[j];
#             j+=1;
#         else:
#             yield arr1[i];
#             i+=1;
#     while (i<len(arr1)):
#         yield arr1[i];
#         i+=1;
#     while (j<len(arr2)):
#         yield arr2[j];
#         j+=1;
# def mergeSort(arr):
#     if (len(arr) <= 1):
#         return arr;
#     mid=math.floor(len(arr)/2);
#     left=mergeSort(arr[0:mid]);
#     right=mergeSort(arr[mid:]);
#     return merge(left,right);

# # print(merge([1,4,7,3],[5,6,9,2]));
# # for i in merge([1,4,7,3],[5,6,9,2]):
# #     print(i)

# print(mergeSort([21, 23, 41, 53, 123, 41, 2, 12, 42]));


# # for i in mergeSort([21, 23, 41, 53, 123, 41, 2, 12, 42]):
# #     print(i)