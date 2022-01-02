from datetime import datetime;
import os;

pwd= os.path.abspath('.');
print(pwd);
print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

print(os.listdir(pwd))
for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))