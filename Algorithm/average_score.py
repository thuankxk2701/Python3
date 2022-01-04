import random;

def make_score(num):
    score=[random.randint(0,100) for i in range(num)];
    return score;

def less_average(score):
    num=len(score);
    sum_score=sum(score);
    ave_num=sum_score/float(num);
    less_average=[i for i in score if i<ave_num];
    return (ave_num,len(less_average));

if __name__=='__main__':
    score=make_score(40);
    average_num,less_num=less_average(score);
    print('the score of average is:',average_num);
    print('the number of less average is: ',less_num);
    print('the every score is[from big to mail]:',sorted(score,reverse=False));