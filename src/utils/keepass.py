# Utils for interacting with keepass

from pykeepass import PyKeePass

def add_entry(keepass : PyKeePass, entry_info : dict):
    group = keepass.find_groups(name='Root', first=True)
    keepass.add_entry(group, entry_info['entry_name'], entry_info['username'], entry_info['password'])

def add_multiple_entries(filename : str, entries : list):
    kp = PyKeePass(filename, password="password")

    for entry in entries:
        add_entry(kp, entry)

    kp.save()
    
