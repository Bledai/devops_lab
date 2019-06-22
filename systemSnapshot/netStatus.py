import psutil
import configparser


class NetStatus:

    def __init__(self, configPath='config.ini', prn=False):
        config = configparser.ConfigParser()
        config.read(configPath)
        if 'network' in config:
            prn = config['network'].getboolean('prn')
        self.prn = prn

    def __str__(self):
        if self.prn:
            c = psutil.net_io_counters(self.prn)
            l = list('{"%s": {"Bytes sent": "%s", "Bytes recv": "%s", "Packages sent": "%s", "Packages recv": "%s",'
                     ' "Errin": "%s", "Error": "%s", "Dropin": "%s", "Dropout": "%s"}}' % (
            k, v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7]) for k, v in c.items())
            return str(l)

        else:
            c = psutil.net_io_counters()

            return '{"Bytes sent": "%s", "Bytes recv": "%s", "Packages sent": "%s", "Packages recv": "%s",' \
                   ' "Errin": "%s", "Error": "%s", "Dropin": "%s", "Dropout": "%s"}' % (c[0], c[1], c[2], c[3], c[4],
                                                                                        c[5], c[6], c[7])


if __name__ == '__main__':
    print(NetStatus())
