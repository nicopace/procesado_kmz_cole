from pcontrol_reader import pcontrol_read
from pas_reader import pas_read
from rec_reader import rec_read
from stop_reader import stop_read

import os

def process(root, name):
    filename = os.path.join(root, name)
    result = None
    if 'pas' in name:
        result = pas_read(filename)
        result['type'] = 'pas'
    elif 'stop' in name:
        result = stop_read(filename)
        result['type'] = 'stop'
    elif 'rec' in name:
        result = rec_read(filename)
        result['type'] = 'rec'
    elif 'pcontrol' in name:
        result = pcontrol_read(filename)
        result['type'] = 'pcontrol'

    result['filename'] = filename

    return result

if __name__ == '__main__':
    import sys
    try:
        ruta = sys.argv[1]
    except:
        ruta = './'
    for root, dirs, files in os.walk(ruta):
        for name in files:
            if 'kmz' in name:
                result = process(root, name)
                print result

