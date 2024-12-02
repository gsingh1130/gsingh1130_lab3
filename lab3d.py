#!/usr/bin/env python3
# Author ID: gsingh1130

import subprocess

def free_space():
    
    p = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
    p1 = subprocess.Popen(['grep', '/$'], stdin=p.stdout, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['awk', '{print $4}'], stdin=p1.stdout, stdout=subprocess.PIPE)
    p.stdout.close()
    p1.stdout.close()
    output = p2.communicate()[0]
    free_space = output.decode('utf-8').strip()
    
    return free_space

if __name__ == "__main__":
    print(free_space())
