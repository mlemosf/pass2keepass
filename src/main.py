# Main file
from utils.gpg import get_file_list, generate_password_list
from utils.keepass import add_multiple_entries
from dotenv import load_dotenv
from os import getenv

load_dotenv()

PASSWORD_FOLDER = getenv("PASSWORD_FOLDER")

# Get all passwords and store in a list of dictionaries 
folder_list = get_file_list(PASSWORD_FOLDER)
password_list = generate_password_list(folder_list)

# Store all passwords in a Keepass kdbx group
add_multiple_entries(getenv('KEEPASS_OUTPUT_FILE'), password_list)
