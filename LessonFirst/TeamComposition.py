
numberTest= int(input());
for _ in range(numberTest):
    n,k=map(int,input().split());
    if(n+k==2):
        print(0);
    elif n==1 or k==1:
        print(1);
    else:
        print(2);


