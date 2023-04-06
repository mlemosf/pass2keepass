# pass2keepass

Command line application for converting UNIX password-store (pass) files to a single kbdx file, compatible with KeePass and its variants.

## Disclaimer

This program was designed as a personal project and deals with sensitive information. **Do NOT use it in a production environment**.

## Dependencies

[pykeepass](https://github.com/libkeepass/pykeepass)  
[python-gnupg](https://github.com/vsajip/python-gnupg)  

## Password store structure

This program is intended for usage on a 2 level password store. GnuPG files must be inside directories. Each directory should contain 1 or more passwords. The structure is as follows:

	/home/user/.password-store
		\_entry1
			\_username1.gpg
		\_entry2
			\_username2.gpg
			\_username3.gpg

The entries on the KeePass database file will use the directory name as the entry name and the filename as the username (without the .gpg extension). The password will be filled with the content of the file.

## Usage

Rename .env.example to .env and fill the environment variables.
After that, just run the main.py file in the src folder:

	python3 main.py

It's important to note that the KeePass output file used for the KEEPASS_OUTPUT_FILE variable must exist beforehand.
