# Main file
from utils.gpg import get_file_list, generate_password_list
from utils.keepass import add_multiple_entries
from dotenv import load_dotenv
from os import getenv
from colorama import Fore, Style
import sys, traceback

load_dotenv()

def main():

    try:
        PASSWORD_FOLDER = getenv("PASSWORD_FOLDER")
        
        # Get all passwords and store in a list of dictionaries 
        print("==> Generating file list...", end=" ")
        folder_list = get_file_list(PASSWORD_FOLDER)
        print(Fore.GREEN + "OK" + Style.RESET_ALL)

        print("==> Loading passwords...", end=" ")
        password_list = generate_password_list(folder_list)
        print(Fore.GREEN + "OK" + Style.RESET_ALL)
        print(f"[INFO] Found {len(password_list)} passwords")
        
        # Store all passwords in a Keepass kdbx group
        print("==> Storing passwords in kdbx file...", end=' ')
        add_multiple_entries(getenv('KEEPASS_OUTPUT_FILE'), password_list)
        print(Fore.GREEN + "OK" + Style.RESET_ALL)

        # Fim da execução
        print(Fore.GREEN + "DONE" + Style.RESET_ALL)
    except Exception:
        print(Fore.RED + "ERROR" + Style.RESET_ALL)
        traceback.print_exc(file=sys.stdout)

if __name__ == '__main__':
    main()
