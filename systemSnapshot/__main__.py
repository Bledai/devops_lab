from systemSnapshot.cpuStatus import CpuStatus
from systemSnapshot.netStatus import NetStatus
from systemSnapshot.memoryStatus import MemoryStatus
from systemSnapshot.virtualMemoryStatus import VirtualMemoryStatus
from systemSnapshot.ioInform import IoInform
from datetime import datetime
import json
import ast
import configparser
import time


class Snapshot:
    def __init__(self, configPath = 'config.ini', output='json', count='0', interval='300'):
        config = configparser.ConfigParser()
        config.read(configPath)
        if 'common' in config:
            output = config['common']['output']
            count = config['common']['count']
            interval = config['common']['interval']
        self.configPath = configPath
        self.output = output
        self.count = count
        self.interval = int(interval)

    def _get_inform(self):
        if self.output == 'json':
            cpuSt = ast.literal_eval(str(CpuStatus()))
            netSt = ast.literal_eval(str(NetStatus()))
            memSt = ast.literal_eval(str(MemoryStatus()))
            virtMemSt = ast.literal_eval(str(VirtualMemoryStatus()))
            ioSt = ast.literal_eval(str(IoInform()))

            if type(ioSt) is not dict:
                for i in range(len(ioSt)):
                    ioSt[i] = ast.literal_eval(ioSt[i])
            if type(netSt) is not dict:
                for i in range(len(netSt)):
                    netSt[i] = ast.literal_eval(netSt[i])
            contentJson = {"Status": [{
                'Cpu Status': [cpuSt],
                'Network Status': [netSt],
                'Memory Status': [memSt],
                'Virtual Memory Status': [virtMemSt],
                'IO Status': [ioSt]
            }]}
            f = open('status_%s.json' % datetime.strftime(datetime.now(), "%Y.%m.%d_%H:%M:%S"), 'w')
            f.write(json.dumps(contentJson, indent=4))
            f.close()

        elif self.output == 'txt':
            f = open('Snapshot.log', 'a')
            f.write('Snapshot %s: \n' % datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"))
            f.write('CPU Status: %s \n' % str(CpuStatus()))
            f.write('Network Status: %s \n' % str(NetStatus()))
            f.write('Memory Status: %s \n' % str(MemoryStatus()))
            f.write('Virtual Memory status: %s \n' % str(VirtualMemoryStatus()))
            f.write('IO status: %s \n' % str(IoInform()))
            f.close()

    def do(self):
        try:
            print('start')
            if self.count == '0':
                while True:
                    self._get_inform()
                    time.sleep(self.interval)
            else:
                for i in range(self.count):
                    self._get_inform()
        except KeyboardInterrupt:
            print('Stopped')
            exit(0)


if __name__ == '__main__':
        snapshots = Snapshot()
        snapshots.do()

