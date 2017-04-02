''' This program connects to the vagrant virtual machine and should be
run from the root directory of the project. It assumes that Git has been
installed and uses the Git ssh executable to connect to the virtual machine
'''
import subprocess
import os
from collections import namedtuple


def here():
    return os.path.abspath(os.path.dirname(__file__))


def call_command(command):
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    return process.communicate()


def call_command_shell(command):
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               shell=True)
    return process.communicate()


def getVagrantSSH():
    vagrantCmd = ['vagrant.exe', 'ssh-config']
    output, err = call_command_shell(' '.join(vagrantCmd))
    lines = output.decode('utf8').split(os.linesep)
    paramNames = ['HostName ', 'Port ', 'User ', 'IdentityFile ']
    paramValues = [None] * len(paramNames)
    for line in lines:
        for index, param in enumerate(paramNames):
            if line.strip().startswith(param):
                paramValues[index] = line.strip()[len(param):]
                break
    ParamSSH = namedtuple('ParamSSH', ['host', 'port', 'username', 'keyFile'])
    # fix identity file location on Windows bash subsystem
    if os.name == 'posix':
        identity = paramValues[3].replace(':', '')
        identity = '/mnt/' + identity[0].lower() + identity[1:]
        paramValues[3] = identity
    return ParamSSH._make(paramValues)


def main():
    sshExe = 'ssh'
    paramSSH = getVagrantSSH()
    # print(paramSSH)
    cmd = ['"%s"' % sshExe, '-p', paramSSH.port, '-i', paramSSH.keyFile, '-t',
           '%s@%s' % (paramSSH.username, paramSSH.host)]
    subprocess.check_call(' '.join(cmd), shell=True)


if __name__ == "__main__":
    main()


