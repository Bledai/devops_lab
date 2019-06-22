import psutil
import configparser


class IoInform:

    def __init__(self, configPath='config.ini', full=False, prd=True):
        config = configparser.ConfigParser()
        config.read(configPath)
        if 'cpy' in config:
            full = config['ioInform'].getboolean('full')
            prd = config['ioInform'].getboolean('prd')
        self.full = full
        self.prd = prd

    def see(self):
        if self.full and not self.prd:
            c = psutil.disk_io_counters(perdisk=self.prd)

            return '{"Read count": "%s", "Write count": "%s", "Read bytes": "%s", ' \
                   '"Write bytes": "%s", "Read time": "%s", "Write time": "%s"}' % (c[0], c[1], c[2], c[3], c[4], c[5])

        elif self.full and self.prd:
            c = psutil.disk_io_counters(perdisk=self.prd)
            l = list(
                '{"%s": {"Read count": "%s", "Write count": "%s", "Read bytes": "%s", "Write bytes": "%s", '
                '"Read time": "%s", "Write time": "%s"}}' % (k, v[0], v[1], v[2], v[3], v[4], v[5]) for
                k, v in c.items())
            return str(l)

        elif self.prd:
            c = psutil.disk_io_counters(perdisk=self.prd)
            l = list('{"%s": {"Read count": "%s", "Write count": "%s", "Read bytes": "%s", "Write bytes": "%s"}}' % (k, v[0], v[1], v[2], v[3]) for k, v in c.items())
            return str(l)

        else:
            c = psutil.disk_io_counters()
            return '{"Read count": "%s", "Write count": "%s", "Read bytes": "%s", "Write bytes": "%s"}' % (c[0], c[1], c[2], c[3])

    def __str__(self):
        return self.see()


if __name__ == '__main__':
    print(IoInform())
