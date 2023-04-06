# Utils for interacting with keepass

from pykeepass import PyKeePass, exceptions
from os import getenv

def add_entry(keepass : PyKeePass, entry_info : dict):
    group = keepass.find_groups(name='Root', first=True)
    keepass.add_entry(group, entry_info['entry_name'], entry_info['username'], entry_info['password'])

def add_multiple_entries(filename : str, entries : list):
    try:
        kp = PyKeePass(filename, password=getenv("KEEPASS_DATABASE_PASSPHRASE"))

        for entry in entries:
            add_entry(kp, entry)

        kp.save()
    except FileNotFoundError as e:
        raise ValueError(f"[ERROR] File '{filename}' was not found. Please create it or specify an existing file in the KEEPASS_OUTPUT_FILE environment variable!")
    except exceptions.CredentialsError as e:
        raise ValueError(f"[ERROR] Credentials for unlocking password database are incorrect. Please specify a valid password in the KEEPASS_DATABASE_PASSPHRASE environment variable!")
    
