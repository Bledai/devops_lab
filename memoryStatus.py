import psutil

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

weight = config['common']['weight']
path = config['memory']['path']
output = config['common']['output']


class MemoryStatus:

    def __init__(self, a=weight, b=path):
        self.weight = a
        self.path = b

    def see(self):

        if self.weight == 'all':
            c = psutil.disk_usage(self.path)
            return c
        else:
            c = psutil.disk_usage(self.path)
            return 'Total: %s ,Used: %s ' % (c[0], c[1])

    def __str__(self):
        return self.see()


if __name__ == '__main__':
    print(weight, path)
    print(MemoryStatus())
