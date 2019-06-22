from systemSnapshot.status import Snapshot
from systemSnapshot.cpuStatus import CpuStatus
from systemSnapshot.netStatus import NetStatus
from systemSnapshot.memoryStatus import MemoryStatus
from systemSnapshot.virtualMemoryStatus import VirtualMemoryStatus
from systemSnapshot.ioInform import IoInform

if __name__ == '__main__':
    try:
        print('Start')
        print(Snapshot())
    except KeyboardInterrupt:
        print('Stopped')
        exit(0)
