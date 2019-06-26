import psutil
import configparser


class MemoryStatus:

    def __init__(self, configPath='config.ini', path='/', full=True):
        config = configparser.ConfigParser()
        config.read(configPath)
        if 'memory' in config:
            full = config['memory'].getboolean('full')
            path = config['memory']['path']
        self.full = full
        self.path = path

    def see(self):

        if self.full:
            c = psutil.disk_usage(self.path)
            return '{"Total": "%s" ,"Used": "%s", "Free": "%s", ' \
                   '"Percent usage": "%s"}' % (c[0], c[1], c[2], c[3])
        else:
            c = psutil.disk_usage(self.path)
            return '{"Total": "%s" ,"Used": "%s" }' % (c[0], c[1])

    def __str__(self):
        return self.see()


if __name__ == '__main__':
    print(MemoryStatus())
