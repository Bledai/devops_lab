# systemSnapshot
## Installation

1. Сopy repository:

    git clone https://github.com/Bledai/devops_lab/tree/homework3
  
2. Building:

    pytnon setup.py bdist_wheel
  
The wheels are now stored in the dist directory. Install them using pip.

## Using:
### Config file

Must have name : config.ini

An example of a custom config is stored in the directory: systemSnapshot. Please copy it before building!

    [common]
    output = json
    interval = 300
    count = 0

    [cpu]
    prc = yes
    full = no

    [memory]
    path = /
    full = yes

    [ioInform]
    prd = no
    full = no

    [network]
    prn = yes

    [virtualMemory]
    full = no
    
  If you want to use as: 
  
      python systemSnapshot 
      
  The config must be located in the same directory where it is launched from the line (transfer of the ponfig from the command line in the development) otherwise custom settings are used
  
   To transfer settings as parameters, or config path as a parameter, use
   
      import systemSnapshot
   
   and work through objects.
   
   ## Methods and Parameters:
   
      import systemSnapshot
      
      snapshot = systemSnapshot.Snapshot(configPath = 'config.ini', output='json', count='0', interval='300')
      snapshot.do()
  
  **count** : number of system snapshots
  
      cpuinfo = systemSnapshot.CpuStatus(configPath='config.ini', full=False, prc=True)
      
  When **prc** is True return a list of named tuples for each logical CPU on the system. First element of the list refers to first CPU, second element to second CPU and so on. 
  
      
   
      
