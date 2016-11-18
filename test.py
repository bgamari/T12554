import subprocess
import time

stdout='test.out'

def test(f):
    fout = open(f, 'w')
    subprocess.call([f], stdout=fout)
    print fout.read()
    fout.close()
    os.unlink(f)

test('./main')
