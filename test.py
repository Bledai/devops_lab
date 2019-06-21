import psutil
import time
import configparser
import status
config = configparser.ConfigParser()
config.read('config.ini')
common = config['common']
count = int(common['count'])

print(status.IoInform())



c = psutil.disk_usage('/')
print(c[0])
f = open('do_re_mi.txt', 'a+')
while count >= 0 or count == 0:
    time.sleep(1)
    contents = str(psutil.cpu_times())
    psutil.cpu_times_percent()
    psutil.disk_usage('/')
    psutil.virtual_memory()
    psutil.disk_io_counters()
    psutil.net_io_counters()
    f.write('test \n')
    count -= 1
f.close()
