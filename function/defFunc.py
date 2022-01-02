import math;

def myAbs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('Bad operand types');
    if(x>=0):
        return x;
    else:
        return -x;
def move(x,y,step,angle=0):
    nx=x+step*math.sin(angle);
    ny=y-step*math.cos(angle);
    return nx,ny;

n = myAbs(-20);
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# TypeError: bad operand type:
my_abs('123')