import math;
numberTest=int(input());
for test in range(numberTest) :
    n=int(input());
    c=1;
    if(n%2==1):
        a = (n - 1) // 2;
        b = (n - 1) // 2;

        while (math.gcd(a, b) > c):
            a -= 1;
            b += 1;
        print(a,b,c)
    else :
        print(n//2,n//2-1,c);



