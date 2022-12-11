#!/usr/bin/python3

import validators
import subprocess
import sys
import os
import ipaddress


destination = os.getenv("DESTINATION_ADDRESS")
timout = os.getenv("TIMEOUT")
max_mtu = os.getenv("MAX_MTU")
if max_mtu is None:
    max_mtu = '10000'

if destination is None or \
    (timout is not None and not timout.isdigit()) or \
        (max_mtu is not None and not max_mtu.isdigit()):
    print(destination, timout)
    print("Wait run as sudo docker run -e DESTINATION_ADDRESS='destination ip / public domain name' [-e TIMEOUT='timeout in ms'] [-e MAX_MTU='max boarder of searching default 10000'] mtu_search")
    exit(0)
else:
    max_mtu = int(max_mtu)

is_valid_ip = False
is_valid_domain = False

# check ip correctness
try:
    ip = ipaddress.ip_address(destination)
    is_valid_ip = True
except Exception:
    pass

# check domain correctness:
try:
    validators.domain(destination)
    is_valid_domain = True
except Exception:
    pass

if not is_valid_domain and not is_valid_ip:
    print("check correctness of input %s" % destination)
    exit(1)


# check destination
command = ['ping', '-c', '1', '-W']
if timout is not None:
    command += [str(timout)]
else:
    command += ['1']
command.append(destination)

try:
    response = subprocess.run(command, capture_output=True)
    is_ping_work = response.returncode == 0
except Exception as ex:
    is_ping_work = False

if not is_ping_work:
    print("desitanion is unreachable for ping. Posibly impc disable or server doesn't exist on correct adress")
    exit(1)

L = -1
R = max_mtu + 1
while L + 1 < R:
    mess_sz = (L + R) // 2
    print('try mtu=%d' % mess_sz)
    command = ['ping', '-c', '1', '-s', str(mess_sz), '-M', 'do']
    if timout is not None:
        command += ['-W', str(timout)]
    command.append(destination)
    try:
        response = subprocess.run(command, capture_output=True)
        if response.returncode != 0:
            if 'too long' in response.stderr.decode():
                R = mess_sz
            elif len(response.stderr.decode()) == 0:
                print(response)
                print("Timeout occur but host may be reachable, you can add timeout as an arg")
                R = mess_sz
            else:
                print("Try to reduce size due to unknown error from ping:", response)
                R = mess_sz
        else:
            L = mess_sz
    except Exception:
        R = mess_sz
        print("Smth went wrong. Try to erase msg size:", response)

if L == -1:
    print("host is unreachable")
else:
    print('mtu size is', L)
    