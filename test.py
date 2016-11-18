import subprocess
import time
import os

stdout='test.out'

def test(f):
    out = 'out'
    fout = open(out, 'w')
    subprocess.call([f], stdout=fout)
    fout.close()

    fin = open(out, 'r')
    print(fin.read())
    fin.close()
    os.unlink(out)

test('./main')
