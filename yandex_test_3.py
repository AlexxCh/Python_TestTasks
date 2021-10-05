import time
import datetime

file1 = open("input_3.txt", "r")
t, e = file1.readline().split()
t, e = int(t), int(e)
logs = []
flag = False
while True:
    line = file1.readline()
    if not line:
        break
    s = line.split()
    if s[2] == 'ERROR':
        logs.append(line)
        dt = datetime.datetime.strptime(s[0][1:] + ' ' + s[1][:-1], "%Y-%m-%d %H:%M:%S")
        cur_time = time.mktime(dt.timetuple())
        last_time = time.mktime(datetime.datetime.strptime(logs[0].split()[0][1:] + ' ' + logs[0].split()[1][:-1], "%Y-%m-%d %H:%M:%S").timetuple())
        if cur_time >= last_time + t:
            logs = logs[-1:]
        if len(logs) == e:
            print(logs[len(logs) - 1].split()[0][1:] + ' ' + logs[len(logs) - 1].split()[1][:-1])
            flag = True
            break
    else:
        continue

if flag == False:
    print(-1)  

file1.close