import psutil
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

output = config['common']['output']
nio = config['network']['nio']
ncn = config['network']['ncn']
nio_prn = config['network']['nio_prn']


class NetStatus:

    def __init__(self, a=nio, b=ncn, c=nio_prn):
        self.nio = a
        self.ncn = b
        self.nio_prn = c

    def __str__(self):
        if self.nio == 'True' and self.ncn == 'True' and self.nio_prn == "True":
            n = psutil.net_connections()
            c = psutil.net_io_counters(self.nio_prn)
            l = list('Int %s :  %s  ' % (k, v) for k, v in c.items())
            return str(l)

        elif self.nio == 'True' and self.ncn == 'True':
            n = psutil.net_connections()
            c = psutil.net_io_counters()
            return str(n)

        elif self.nio == 'True':
            n = psutil.net_connections()
            return str(n)


if __name__ == '__main__':
    print(nio, ncn, nio_prn)
    print(NetStatus())
