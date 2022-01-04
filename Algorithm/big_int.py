def arabic_multiplication(num1,num2):
      # 123->[1,2,3]，
    num_lst1 = [int(i) for i in str(num1)];
    num_lst2 = [int(i) for i in str(num2)];

    #个list
    int_martix = [[i*j for i in num_lst1] for j in num_lst2];
    
    #9-->'09'
    str_martix = [map(convert_to_str,int_martix[i]) for i in range(len(int_martix))];
    
    #：['01','29','03']-->[0,2,0],[1,9,3]
    martix = [[int(str_martix[i][j][z]) for j in range(len(str_martix[i]))] for i in range(len(str_martix)) for z in range(2)];   
    
    sum_left = summ_left(martix);    
    sum_end = summ_end(martix);    
    sum_left.extend(sum_end);
    sum_left.reverse();    
    result = take_digit(sum_left);   
    
    result.reverse();
    int_result = "".join(result);
    print ("%d*%d="%(num1,num2));
    print (int_result);
    
#9-->'09'
def convert_to_str(num):
    if num<10:
        return "0"+str(num)
    else:
        return str(num)
    
def summ_left(lst):
    summ = [];
    x = [i for i in range(len(lst))];
    y = [j for j in range(len(lst[0]))];
    sx = [i for i in x if i%2==0];
    for i in sx:
        s=0;
        j=0;
        while i>=0 and j<=y[-1]:
            s = s+ lst[i][j];
            if i%2==1:
                j = j+1;
            else:
                j = j;
            i = i-1;
        summ.append(s);
    return summ;


def summ_end(lst):
    summ=[];
    y = [j for j in range(len(lst[0]))];
    ex = len(lst)-1;
    for m in range(len(y)):
        s = 0;
        i=ex;
        j=m;
        while i>=0 and j<=y[-1]:
            s= s+lst[i][j];
            if i%2==1:
                j = j+1;
            else:
                j=j;
            i = i-1;
        summ.append(s);    
    return summ;

def take_digit(lst):
    tmp = 0;
    digit_list = [];
    for m in range(len(lst)):
        lstm = 0;
        lstm = lst[m]+tmp;
        if lstm<10:
            tmp = 0;
            digit_list.append(str(lstm));
        else:
            tmp = lstm/10;
            mm = lstm-tmp*10;
            digit_list.append(str(mm));
    return digit_list;


if __name__=="__main__":
    arabic_multiplication(469,37);