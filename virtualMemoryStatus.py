import psutil
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

weight = config['common']['weight']
output = config['common']['output']


class VirtualMemoryStatus:

    def __init__(self, a=weight):
        self.weight = a

    def see(self):

        if self.weight == 'all':
            c = psutil.virtual_memory()
            return c
        else:
            c = psutil.virtual_memory()
            return 'Total: %s ,Available: %s ' % (c[0], c[1])

    def __str__(self):
        return self.see()


if __name__ == '__main__':
    print(weight)
    print(VirtualMemoryStatus())
