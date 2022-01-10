
def binarySearch(lst,value,low,high):
    if high<low:
        return -1;
    mid=(low+high)//2;
    
    if lst[mid]>value:
        return binarySearch(lst,value,low,mid-1);
    elif lst[mid]<value:
        return binarySearch(lst,value,mid+1,high);
    else:
        return mid;
def bSearch(lst,value):
    lo,hi=0,len(lst)-1;
    while lo<=hi:
        mid=(lo+hi)//2;
        if lst[mid]>value:
            hi=mid-1;
        elif lst[mid]<value:
            lo=mid+1;
        else:
            return mid;
    return -1;

from  bisect import *;

def bisectSearch(lst,x):
    i=bisect_left(lst,x);
    if i!=len(lst) and lst[i]==x:
         return i;
   

if __name__ =="__main__":
    lst=sorted([1,2,4,5,6]);
    print(lst);
    print(binarySearch(lst,5,0,4));
    print(bisectSearch(lst,5));
    print(bSearch(lst,5));
    