import re
import os
import platform
from colorama import Fore, Style, init

init(autoreset=True)

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def find_16_digit_hex_strings(file_path):
    clear_console()

    if not os.path.exists(file_path):
        print(f"{Fore.RED}Error: The file does not exist.")
        return

    with open(file_path, 'rb') as f:
        data = f.read()

    text = ''.join(chr(b) if 32 <= b < 127 else ' ' for b in data)

    matches = re.findall(r'\b[a-fA-F0-9]{16}\b', text)

    if matches:
        print(f"{Fore.GREEN}✅ {Style.BRIGHT}Found ID:")
        for m in matches:
            print(f"{Fore.CYAN}🆔 {Style.BRIGHT}{m}")
    else:
        print(f"{Fore.YELLOW}❌ {Style.BRIGHT}Nothing found :/")

    return matches

def main_menu():
    while True:
        clear_console()
        
        print(f"\n{Fore.MAGENTA}C1aym4re's PARAM.SFO Reader")
        print(f"{Fore.BLUE}Choose an option:")
        print("1. Read PARAM.SFO")
        print("2. Close Program")

        choice = input(f"\n{Fore.YELLOW}Enter your choice (1 or 2): ")

        if choice == "1":
            clear_console()
            file_path = input(f"{Fore.YELLOW}Enter the Path to your PARAM.SFO: ")
            find_16_digit_hex_strings(file_path)
        elif choice == "2":
            clear_console()
            print(f"{Fore.RED}Closing Program... Goodbye!")
            break 
        else:
            print(f"{Fore.RED}❌ Invalid choice, please choose 1 or 2.")

     
        input(f"\n{Fore.YELLOW}Press Enter to return to the menu...")

main_menu()
