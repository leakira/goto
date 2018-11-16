#!/usr/bin/python

import io, copy, sys, json, os
from os.path import expanduser

# Command list file
FILE_NAME = expanduser('~')+'/goto.json'

# All command guide
GUIDE = {
    'run':    '[name]',
    'add':    '--add [name] [path]',
    'remove': '--remove [name]',
    'list':   '--list',
    'help':   '--help',
}


def init():
    """
    Run script
    """

    params = get_params()
    for cmd in get_commands():
        raw_cmd = '--'+cmd
        if raw_cmd == params['cmd']:
            if cmd not in globals(): sys.exit('Command not found')

            if cmd is 'help':
                sys.exit(json_format('Available commands', help()))
            elif cmd is 'list':
                sys.exit(json_format('Available list', list()))
            else:
                globals()[cmd](params)
            break


def get_params():
    """
    Format arguments as command and args params
    """

    temp = sys.argv[1:]
    cmd = temp[0] if '--' in temp[0] else '--run'
    args = temp[1:] if '--' in temp[0] else temp
    return {
        'cmd': cmd,
        'args': args,
    }


def add(params):
    """
    Add command

    :param params: get_params()
    :type params: dictionary
    """

    if len(params['args']) < 2: sys.exit('[add] Error: Invalid command arguments. Need to be: '+help('add'))

    args = params['args']
    original = list()
    data = copy.deepcopy(original)
    if os.path.isdir(args[1]):
        data[args[0]] = args[1]
    else:
        sys.exit('[add] Error: Path is invalid')

    if original != data: write(data)
    print 'Successfully added'


def remove(params):
    """
    Remove command

    :param params: get_params()
    :type params: dictionary
    """

    if len(params['args']) < 1: sys.exit('[remove] Error: Invalid command arguments. Need to be: '+help('remove'))

    name = params['args'][0]
    original = list()

    data = copy.deepcopy(original)
    if name in data: data.pop(name, None)

    if original != data: write(data)
    print 'Successfully removed'


def run(params):
    """
    Run command

    :param params: get_params()
    :type params: dictionary
    """

    name = params['args'][0]
    data = list()
    if name in data:
        sys.exit(data[name])
    else:
        sys.exit('[run] Error: Key name "'+name+'" not found in list')


def list():
    """
    List all added path
    """

    try:
        with io.open(FILE_NAME, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        data = {}

    return data


def write(content):
    """
    Write path .json file

    :param content: json content to write
    :type content: dictionary
    """

    with open(FILE_NAME, 'w') as f:
        json.dump(content, f)
        f.write("\n")


def get_commands():
    """
    Get command key names
    """

    return GUIDE.keys()


def help(name=None):
    """
    Get help guide, or of specific command

    :param name: guide name, optional, if not passed, returns all guide
    :type name: string
    """

    return GUIDE[name] if name else GUIDE


def json_format(subtitle, data):
    """
    Format json to string

    :param subtitle: description to text
    :type subtitle: string

    :param data: content to format
    :type data: dictionary
    """

    msg = subtitle+':\n'
    for name in data: msg += name+': '+data[name]+'\n'
    return msg.strip()


if __name__ == '__main__':
    init()
