import psutil
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

weight = config['common']['weight']
prd = config['ioInform']['prd']
output = config['common']['output']


class IoInform:

    def __init__(self, a=weight, b=prd):
        self.weight = a
        self.prd = b

    def __str__(self):
        if self.weight == 'all' and self.prd == 'False':
            c = psutil.disk_io_counters(perdisk=self.prd)
            return c

        elif self.weight == 'all' and self.prd == 'True':
            c = psutil.disk_io_counters(perdisk=self.prd)
            l = list(
                '%s : Read count: %s  Write count: %s Read bytes: %s  Write bytes: %s' % (k, v[0], v[1], v[2], v[3]) for
                k, v in c.items())
            return str(l)

        elif self.prd == 'True':
            c = psutil.disk_io_counters(perdisk=self.prd)
            l = list('%s : Read count: %s  Write count: %s Read bytes: %s  Write bytes: %s' % (k, v[0], v[1], v[2], v[3]) for k, v in c.items())
            return str(l)

        else:
            c = psutil.disk_io_counters()
            return 'Read count: %s  Write count: %s Read bytes: %s  Write bytes: %s' % (c[0], c[1], c[2], c[3])


if __name__ == '__main__':
    print(weight, prd)
    print(IoInform())
