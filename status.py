from cpuStatus import CpuStatus
from netStatus import NetStatus
from memoryStatus import MemoryStatus
from virtualMemoryStatus import VirtualMemoryStatus
from ioInform import IoInform
import json
import ast
import configparser
import time

config = configparser.ConfigParser()
config.read('config.ini')

output = config['common']['output']
count = config['common']['count']
interval = config['common']['interval']


class Status:
    def __init__(self, a='config.ini', b=output):
        self.configPath = a
        self.output = b

    def st(self):
        if count == '0':
            i = 0
            while True:
                time.sleep(int(interval))
                i += 1
                if self.output == 'json':
                    cpuSt = ast.literal_eval(str(CpuStatus()))
                    netSt = str(NetStatus())
                    print(NetStatus())
                    memSt = str(MemoryStatus())
                    print(MemoryStatus())
                    virtMemSt = str(VirtualMemoryStatus())
                    print(VirtualMemoryStatus())
                    ioSt = str(IoInform())
                    print(IoInform())
                    contentJson = {"Snapchoot": [{
                        'Cpu Status':  [cpuSt],
                        'Network Status':  [netSt],
                        'Memory Status': [memSt],
                        'Virtual Memory Status': [virtMemSt],
                        'IO Status': [ioSt]}]
                    }
                    f = open('status%s.json' % i, 'a')
                    f.write(json.dumps(contentJson, indent=4))
                    f.close()

                elif self.output == 'txt':
                    f = open('status.txt', 'a+')
                    f.write('Snapshot%s' % i)
                    f.write(str(CpuStatus()))
                    f.write(str(NetStatus()))
                    f.write(str(MemoryStatus()))
                    f.write(str(VirtualMemoryStatus()))
                    f.write(str(IoInform()))
                    f.close()




if __name__ == '__main__':
    a = Status()
    a.st()

