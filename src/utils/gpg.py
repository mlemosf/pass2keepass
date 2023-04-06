# GPG utilities
import gnupg
import os

# Get list of folders
def get_file_list(folder : str) -> [str]:
    collection = []
    info = {}

    # Checks if folder is valid and find all files
    if os.path.isdir(folder):
        dirs = os.scandir(path=folder)
    else:
        raise ValueError("[ERROR] Selected path is not a valid directory!")
    seen_list = []

    for obj in dirs:
        key = ""
        if obj.is_dir():
            key = obj.name 

            # Find files in dir
            for f in os.scandir(obj):
                if f.is_file() and '.gpg' in f.name:

                    # Add info to dict
                    path = f.path
                    username = f.name.split('.gpg')[0]

                    # Checks if the entry name has been seen (for duplicated entries)
                    occurrences = seen_list.count(key)
                    if occurrences == 0:
                        seen_list.append(key)
                        entry_name = f'{key}'
                    else:
                        entry_name = f'{key}{occurrences + 1}'

                    info = {
                        'entry_name': entry_name,
                        'username': username,
                        'path': path,
                    }
                    collection.append(info)
    if len(collection) == 0:
        raise ValueError("[ERROR] No gpg files were found! Specify a valid password store")
    return collection
                    
            

# Read entry
def read_entry(gnupghome : str, password_file: str, passphrase : str) -> str:
    gpg = gnupg.GPG(gnupghome=gnupghome)
    data_pass = ""

    with(open(password_file, 'rb')) as f:
       data = gpg.decrypt_file(f, passphrase=passphrase) 
       data_pass = str(data).strip('\n')

    return data_pass

def generate_password_list(folder_list : list) -> list:
    # Read configuration from file
    gnupghome = os.getenv('GNUPGHOME')
    passphrase = os.getenv('GNUPG_PASSPHRASE')

    # Generate password list
    password_list = []

    for folder in folder_list:
        password = read_entry(gnupghome, folder['path'], passphrase)
        username = folder['username']
        entry_name = folder['entry_name']

        info = {
            'entry_name': entry_name,
            'username': username,
            'password': password
        }

        password_list.append(info)

    return password_list
