from datetime import datetime
import subprocess
import sys
import os
import re
import json
import yaml


def getInform():

    pipLocation = subprocess.run('which pip', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
    instPack = subprocess.run('pip freeze', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
    instPack = re.findall(r"[\w']+.*", instPack)
    p = {}
    d = []
    l = []
    versPy = subprocess.run('ls -dl -1 ~/.pyenv/versions/* | grep ^d', shell=True,
                            stdout=subprocess.PIPE).stdout.decode('utf-8')
    versPy = versPy.split('\n')
    for v in versPy:
        d.append(v[-5::])
    d.remove(d[-1])
    nameEnv = subprocess.run('ls -dl -1 ~/.pyenv/versions/* | grep -o envs/.* | cut -d"/" -f2', shell=True,
                             stdout=subprocess.PIPE).stdout.decode('utf-8')
    nameEnv = nameEnv.split('\n')
    for n in nameEnv:
        if n is not None:
            l.append(n)
    l.remove(l[-1])
    for i in range(len(instPack)):
        instPack[i] = instPack[i].split('==')

    try:
        user_paths = os.environ['PYTHONPATH']
    except KeyError:
        user_paths = 'PYTHONPATH doesn\'t exist'
    try:
        for iP in instPack:
            p.update({iP[0]: iP[1]})
        result = {
            'Using version Python': sys.version[:5],
            'All versions python': d,
            'All virtualenv names': l,
            'Python executable location': f'{sys.real_prefix}/bin/python{sys.version[:3]}/site-packages',
            'Name of virtualenv': f'{sys.prefix.split("/")[-1]}',
            'Site-packages location': f'{sys.real_prefix}/lib/python{sys.version[:3]}',
            'PYTHONPATH': user_paths,
            'Pip location': pipLocation[-2],
            'Installed packages': p
            }
        return result

    except AttributeError:
        for iP in instPack:
            p.update({iP[0]: iP[1]})
        result = {
            'Using version Python': sys.version[:5],
            'All versions python': d,
            'All virtualenv names': l,
            'Python executable location': f'{sys.prefix}/bin/python{sys.version[:3]}/site-packages',
            'Name of virtualenv': f'{sys.prefix.split("/")[-1]}',
            'Site-packages location': f'{sys.prefix}/lib/python{sys.version[:3]}',
            'PYTHONPATH': user_paths,
            'Pip location': pipLocation[-2],
            'Installed packages': p
            }
        return result


if __name__ == "__main__":

    f = open('status_%s.json' % datetime.strftime(datetime.now(), "%Y.%m.%d_%H:%M:%S"), 'w')
    contentJson = getInform()
    f.write(json.dumps(contentJson, indent=4))
    f.close()
    a = getInform()
    y = open("example.yaml", 'w')
    y.write(yaml.dump(a, default_flow_style=False, allow_unicode=True))
    y.close()


