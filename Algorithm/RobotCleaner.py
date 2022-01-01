numberTest=int(input());
for _ in range(numberTest):
    n,m,a,b,c,d=map(int,input().split());
    re1=0;
    res2=0;
    if (a<=c):
        res1=c-a;
    else :
        res1=2*n-a-c;
    if(b<=d):
        res2=d-b;
    else:
        res2=2*m-b-d;

    print(min(res1,res2))


