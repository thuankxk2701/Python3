import math;
numberTest=int(input());
for T in range(numberTest):
    x1,x2=map(int,input().split());
    isCheck=True;
    if(x1+x2)%2==1 :
        print(-1,-1);
    else:
        if (x1 > x2):
            mid=(x1+x2)//2;
            if(x2%2==0):
                print(x1//2,x2//2);
            else:

                print(mid-x2,x2);
        else:
            mid=(x1+x2)//2;
            if(x2%2==0):
                print(x1//2,x2//2);
            else:
                print(x1,mid-x1);




