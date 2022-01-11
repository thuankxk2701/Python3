check=[True]*(1000000+1); 
def sieve(n):            
    can_n=int(n**0.5)+1 ;    
    for i in range(2,can_n+1): 
        if check[i]:            
            for j in range(i*i,n+1,i):
                check[j]=False        
    primes=[]
    for i in range(2,n+1):
        if check[i]: primes.append(i); 
    return primes

lSieve=sieve(1000000);
n=int(input());
if n< 10000000:
    vt=0;result=1;
    sm=0;
    while True:               
        if lSieve[vt]>n or vt >=len(lSieve) or n==1:
            if sm!=0:
                result*=(sm+1);
            break;
        if n%lSieve[vt]==0:
            sm+=1;
            n=n//lSieve[vt];            
        else:            
            
            vt+=1;
            result=result*(sm+1);            
            sm=0;
    if n!=1:
        result*=2;
    print((result-1)//2);              
        
else:
    vt=len(lSieve)-1;result=1;    
    sm=0;
    while True:        
        if n==1 or vt<0 or lSieve[vt]>n:
            if sm!=0:
                result*=(sm+1);
            break;
        if n%lSieve[vt]==0:                       
            sm+=1;
            n=n//lSieve[vt];
        else:
            vt-=1;
            result*=(sm+1);
            sm=0;
    if n!=1:
        result*=2;
    print((result-1)//2);  