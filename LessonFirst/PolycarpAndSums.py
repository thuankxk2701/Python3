numberTest= int(input());
for i in range(numberTest):
    Arr=list(map(int,input().split()));
    a=Arr[0];
    b=Arr[1];
    for i in range(len(Arr)-1):
        if (a+b+Arr[i]==Arr[len(Arr)-1]):
            c=Arr[i];
            break;
    print(a,b,c);
