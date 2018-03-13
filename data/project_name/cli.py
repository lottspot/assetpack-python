import os
import sys

def die(msg):
    emsg = '{}: {}'.format(
        os.path.basename(sys.argv[0]),
        msg
    )
    sys.exit(emsg)

def main():
    return 0
