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
  **Be careful when you make a config file! If the header is initialized then ALL its fields should be filled.**  
  If you want to use as: 
  
      python systemSnapshot 
      
  The config must be located in the same directory where it is launched from the line (transfer of the ponfig from the command line in the development) otherwise custom settings are used. 
  
   To transfer settings as parameters, or config path as a parameter, use
   
      import systemSnapshot
   
   and work through objects.
   
   ## Methods and Parameters:
   
  if you used only **configPath** that **yes** it meens **True**
  
    import systemSnapshot
      
   #### Full system Snapshot
   
      snapshot = systemSnapshot.Snapshot(configPath = 'config.ini', output='json', count='0', interval='300')
      snapshot.do()
  
  Output file in every 300 seconds (5 minutes) in json format
  
  **count** : number of system snapshots
  
  #### CPU information
  
      cpuinfo = systemSnapshot.CpuStatus(configPath='config.ini', full=False, prc=True)
      cpuinfo.see()
      # ptint(systemSnapshot.CpuStatus())
      
  When **prc** is True return a list of named tuples for each logical CPU on the system. First element of the list refers to first CPU, second element to second CPU and so on. 
 
#### Network status information

    netinf = systemSnapshot.NetStatus(configPath='config.ini', prn=False)
    netinf.see()
    # print( systemSnapshot.NetStatus())
    
   If **prn** is True return the same information for every network interface installed on the system as a dictionary with network interface names as the keys and the named tuple described above as the values.

#### Memory status information

    meminf = systemSnapshot.MemoryStatus(configPath='config.ini', path='/', full=True)
    meminf.see()
    # print(systemSnapshot.MemoryStatus())
    
Return disk usage statistics about the partition which contains the given **path** as a named including total, used (if **full** True)  and free space expressed in bytes, plus the percentage usage.

#### IO information

    ioinf = systemSnapshot.IoInform(configPath='config.ini', full=False, prd=True)
    ioinf.see()
    # print(systemSnapshot.IoInform())
    
If **prd** is True return the same information for every physical disk installed on the system as a dictionary with partition names as the keys and the named tuple described above as the values. 

#### Virtual memory information

    virtmeminfo = systemSnapshot.VirtualMemoryStatus(configPath='config.ini', full=False)
    virtmeminfo.see()
    # print(systemSnapshot.VirtualMemoryStatus())
