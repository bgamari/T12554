import subprocess
import time
import os

out = 'out'
fout = open(out, 'w')
subprocess.call(['./timeout.exe', '1', './main'], stdout=fout)
fout.close()

fin = open(out, 'r')
print(fin.read())
fin.close()
os.unlink(out)

