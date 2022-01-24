numberTest=int(input());
for _ in range(numberTest):
    a,b,c=map(int,input().split());
    
    
    if(a+b+c)%2==0:
        print("YES");
    else:
        print("NO")