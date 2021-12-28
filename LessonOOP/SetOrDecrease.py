numberTest=int(input());
for _ in range(numberTest):
    n,k=map(int,input().split());
    arr=list(map(int,input().split()));
    sum=0;
    arr.sort();
    for x in arr:
        sum+=x;
    result=0;
    tail=len(arr)-1;
    head=0;
    while(sum>k):
        if(tail==head):
            sum-=1;
            result+=1;
        else:
            sum = sum - arr[tail] + arr[head];
            tail -= 1;
            result+=1;
    print(result);




