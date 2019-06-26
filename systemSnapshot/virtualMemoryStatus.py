import psutil
import configparser


class VirtualMemoryStatus:

    def __init__(self, configPath='config.ini', full=False):
        config = configparser.ConfigParser()
        config.read(configPath)
        if 'virtualMemory' in config:
            full = config['virtualMemory'].getboolean('full')
        self.full = full

    def see(self):

        if self.full:
            c = psutil.virtual_memory()
            return '{"Total": "%s", "Available": "%s", "Percent": "%s", "Used": "%s",' \
                   '"Free": "%s"} ' % (c[0], c[1], c[2], c[3], c[4])
        else:
            c = psutil.virtual_memory()
            return '{"Total": "%s", "Available": "%s"} ' % (c[0], c[1])

    def __str__(self):
        return self.see()


if __name__ == '__main__':
    print(VirtualMemoryStatus())
