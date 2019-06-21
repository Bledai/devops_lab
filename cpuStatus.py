import psutil
import configparser
import json
import ast

config = configparser.ConfigParser()
config.read('config.ini')

weight = config['common']['weight']
output = config['common']['output']
prc = config['cpu']['prc']


class CpuStatus:
    def __init__(self, a=weight, b=prc):
        self.weight = a
        self.prc = b

    def see(self):

        if self.weight == 'all':
            c = psutil.cpu_times(percpu=self.prc)
            return '{ "User": "%s", "System": "%s", "idle": "%s" , "iowait": "%s" , "irq ": "%s"}' % (c[0][0], c[0][1], c[0][2],
                                                                                      c[0][3], c[0][4])
        else:
            c = psutil.cpu_times(percpu=self.prc)
            return '{ "User": "%s", "System": "%s", "idle": "%s"}' % (c[0][1], c[0][1], c[0][2])

    def __str__(self):
        return self.see()


if __name__ == '__main__':
    print(weight, prc)
    print(CpuStatus(weight, prc))

