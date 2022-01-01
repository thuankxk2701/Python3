numberTest=int(input());
for _ in range(numberTest):
    n=int(input());
    dict={};
    for __ in range(n):
        l,r=map(int,input().split());
        dict.update([l,r]);
    math.sort(dict);
    print(dict)
