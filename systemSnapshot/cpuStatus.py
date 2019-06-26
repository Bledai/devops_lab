import psutil
import configparser


class CpuStatus:
    def __init__(self, configPath='config.ini', full=False, prc=True):
        config = configparser.ConfigParser()
        config.read(configPath)
        if 'cpy' in config:
            full = config['cpu'].getboolean('full')
            prc = config['cpu'].getboolean('prc')
        self.full = full
        self.prc = prc

    def see(self):

        if self.full:
            c = psutil.cpu_times(percpu=self.prc)
            return '{ "User": "%s", "System": "%s", "Idle": "%s" , "iowait": "%s" ,' \
                   ' "irq ": "%s"}' % (c[0][0], c[0][1], c[0][2], c[0][3], c[0][4])
        else:
            c = psutil.cpu_times(percpu=self.prc)
            return '{ "User": "%s", "System": "%s", "idle": "%s"}' % (c[0][1], c[0][1], c[0][2])

    def __str__(self):
        return self.see()


if __name__ == '__main__':
    print(CpuStatus())
