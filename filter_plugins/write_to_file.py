#!/usr/bin/python
import json

def write_to_file(data, filepath):
    fd = open(filepath, "w")
    # if its json string
    if type(data) == str:
        fd.write(data)
    else:
        fd.write(json.dumps(data))
    fd.close()
    return data

class FilterModule(object):
    ''' A filter to write variables to file '''
    def filters(self):
        return {
            'write_to_file': write_to_file
        }
