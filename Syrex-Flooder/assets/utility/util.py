import os
from colorama import Style

# Color codes for terminal output
light_green = "\033[38;2;194;255;182m"
dark_gray = "\033[1;90m"
red = "\033[1;31m"
blue = "\033[1;34m"
white = "\033[1;37m"
reset = Style.RESET_ALL

# Function to load tokens from a file
def retrieve_tokens():
    with open("input/tokens.txt", "r") as file:
        return [token.strip() for token in file if token.strip().startswith('MT')]

# Load tokens
loaded_tokens = retrieve_tokens()

# Function to load emojis from a file
def load_emojis():
    with open('assets/get/emojis.txt', 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

# Load emojis
emojis = load_emojis()

# Function to center text in terminal
def center_text(text: str, width: int = None):
    if width is None:
        width = os.get_terminal_size().columns
    centered_lines = []
    for line in text.splitlines():
        spaces = (width - len(line)) // 2
        centered_lines.append(' ' * spaces + line)
    return '\n'.join(centered_lines)

# Function to execute a terminal command
def execute_command(command: str):
    os.system(command)

# Function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the logo
def display_logo():
    logo_text = center_text(f"""
{light_green}                                                       
//   ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
//  ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
//  ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
//   ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓██████▓▒░  ░▒▓██████▓▒░  
//         ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
//         ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
//  ░▒▓███████▓▒░   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
//                                                                     
//                                                                                                             
 {reset}
    """)
    print(logo_text)
    print(f"""
                                            {light_green}[{red}1{light_green}]{reset} {white} Dm Spam     {light_green}[{red}2{light_green}]{reset} {white} Exit
    """)

# Example usage
if __name__ == "__main__":
    display_logo()
