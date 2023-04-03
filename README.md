# pass2keepass

Command line application for converting UNIX password-store (pass) files to a single kbdx file, compatible with KeePass and its variants.

## Dependencies

[pykeepass](https://github.com/libkeepass/pykeepass)  
[python-gnupg](https://github.com/vsajip/python-gnupg)  

## Usage

Rename .env.example to .env and fill the environment variables.
After that, just run the main.py file in the src folder:

	python3 main.py

It's important to note that the KeePass output file used for the KEEPASS_OUTPUT_FILE variable must exist beforehand.
