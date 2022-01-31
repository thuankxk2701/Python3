numberTest=int(input());

for _ in range(numberTest):
    n=str(input());
    sum0=0;
    sum1=0;
    for i in range(len(n)):
        if(n[i]=="0"):
            sum0+=1;
        else:
            sum1+=1;
    if(sum1==0 or sum0==0 or sum1==sum0):
        print(0);
        continue;
    if(sum1<sum0):
        print(sum1)
    else:
        print(sum0)
     
