
# def hello(first_name,last_name,age) :
#     print("Hello {} {},{} years old!".format(first_name,last_name,age));
#
# hello("Nguyen",'Thuan',19)

# def multiply(number1,number2) :
#     result=number2*number1;
#     return  result;
#     # return number1*number2;
#
# x= multiply(6,11);
# print(x);

# key work argument

# def hello(first,middle,last):
#     print("hello "+first+' '+middle+' '+last);
#
# hello(last="code",first="Bro",middle="die")

# Nested functions calls

# num=input("Enter a whole positive number : ");
# num=float(num);
# num=abs(num);
# num=round(num);
# print(num);

# print(round(abs(float(input("Enter a whole positives number :")))));

# *Args

# def add(*rest):
#     sum=0;
#     rest=list(rest);
#
#     for x in rest :
#         sum+=x;
#     return sum;
#
# print(add(1,2,3,4,5))

### **Args

# def hello(**kwargs):
#     print(kwargs['title'])
#     print("hello",end=" ");
#     for key,value in kwargs.items() :
#         print(value,end=" ");
#
# hello(title="Mr. ",first="Thuan",middle="Pro",last="Code");
t = int(input())
for i in range(t):
    w, h = map(int, input().split())
    x1 = list(map(int, input().split()))
    x2 = list(map(int, input().split()))
    y1 = list(map(int, input().split()))
    y2 = list(map(int, input().split()))
    x1 = x1[1:]
    x2 = x2[1:]
    y1 = y1[1:]
    y2 = y2[1:]
    a1 = (max(x1) - min(x1)) * h
    a2 = (max(x2) - min(x2)) * h
    a3 = (max(y1) - min(y1)) * w
    a4 = (max(y2) - min(y2)) * w
    arr = [a1, a2, a3, a4]
    print(max(arr))
