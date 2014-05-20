from pcontrol_reader import pcontrol_read
from pas_reader import pas_read
from rec_reader import rec_read
from stop_reader import stop_read
from datetime import datetime, tzinfo
from pytz import timezone

import os

companies = {
    '1': 'Fournier',
    '2': 'Plaza',
    '4': 'Villarino',
    '7': 'Sapem',
    '8': 'San Gabriel'
}

local_tz = timezone('America/Argentina/Buenos_Aires')

def extract_date(path_data):
    for i, value in enumerate(path_data):
        try:
            path_data[i] = int(value)
        except:
            pass

    return datetime(path_data[2], path_data[3], path_data[4], path_data[5], tzinfo=local_tz)

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
    else:
        result = []

    result['filename'] = filename
    path_data  = filename.split('/')
    company_id = path_data[1]
    data_date = extract_date(path_data)


    result['company'] = companies[company_id]

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

