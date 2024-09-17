import os
from colorama import Style
import discord
import asyncio
from datetime import datetime
import random
from gradientify import Colors
from assets import *
from assets.utility.util import *

# Color definitions
red = "\033[38;2;255;0;0m"       
orange = "\033[38;2;255;165;0m"   
yellow = "\033[38;2;255;255;0m" 
green = "\033[38;2;0;255;0m"  
blue = "\033[38;2;0;0;255m"       
purple = "\033[38;2;128;0;128m"   
reset = Style.RESET_ALL           

# Function to load tokens from a file
def load_tokens():
    try:
        with open("input/tokens.txt", "r") as f:
            return [token.strip() for token in f.readlines() if token.strip()]
    except FileNotFoundError:
        print(f"{red}Error: tokens.txt not found!{reset}")
        exit()

# Sample set_t function definition
def set_t(message):
    print(message)  # Just print the message for now; modify as needed

# Function to clear the console
def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    print(f"""{blue}
                         ███████╗██╗   ██╗██████╗ ███████╗██╗  ██╗
                         ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝╚██╗██╔╝
                         ███████╗ ╚████╔╝ ██████╔╝█████╗   ╚███╔╝    
                         ╚════██║  ╚██╔╝  ██╔══██╗██╔══╝   ██╔██╗  
                         ███████║   ██║   ██║  ██║███████╗██╔╝ ██╗
                         ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                                                             
      |═══════════════════════════════════════════════════════════════════════════════|
                                             ║
                                             ║
                                ╔═════════════════════════╗
                                ║       [1] DMs Flood     ║
                                ╚═════════════════════════╝
                                             ║
                                             ║
                                ╔═════════════════════════╗
                                ║       [2] Exit          ║
                                ╚═════════════════════════╝
                                             ║
                                             ║
                                             ║
                                            ~~~

                  {reset}""")

async def spam(token, uid, message, count, rs, rm, em):
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        await asyncio.sleep(0.5)
        
        print(f"{blue}[✔️]{reset} {green}Successfully connected as: {reset}({client.user.name})")
        await asyncio.sleep(1)
        target_user = await client.fetch_user(int(uid))

        for _ in range(count):
            try:
                msg = message
                if rs:
                    msg += " # " + ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=25))

                if rm:
                    msg += " # " + ' '.join(random.choices(emojis, k=em))

                await target_user.send(msg)
                await asyncio.sleep(0.5)
                print(f"{blue}[✓]{reset} {green}Message sent: {reset}{msg} to {target_user.name} ({client.user.name})")

            except discord.Forbidden:
                print(f"{red}➡️{reset} {red}Unable to send message to {target_user.name}. DMs are closed or the user is unavailable on the server!{reset} ({client.user.name})")
                continue

    await client.start(token)

async def countdown():
    for i in range(5, 0, -1):
        print(f"Returning to the main menu in {i} seconds...")
        await asyncio.sleep(1)

async def main():
    tokens = load_tokens()  # Call the load_tokens function
    set_t(f'Syrex Flooder has been [~] Loaded {len(tokens)} tokens')
    clr()  # Clear the console
    logo()  # Display the logo
    option = input(f'            {red}[💀] Sʏʀᴇx.ᴘʏ$~ → Choose [1] or [2]: {reset} ')

    if option == "1":
        print()
        uid = input(Colors.mint("Sʏʀᴇx.ᴘʏ$~ → Paste The User Id Here ~ "))
        if uid == '':
            await main()
        message = input(Colors.mint("Sʏʀᴇx.ᴘʏ$~  → What Message Do You Want Them To Receive ~ "))
        if message == '':
            await main()
        count = int(input(Colors.mint("Sʏʀᴇx.ᴘʏ$~ → Amount Of The Message ~ ")))
        if count <= 0:
            print(Colors.red_to_white("Count must be greater than 0."))
            await main()
        rs = input(Colors.mint("Sʏʀᴇx.ᴘʏ$~ → Do you want Random String? (y/n) ~ ")).strip().lower() == 'y'
        rm = input(Colors.mint("Sʏʀᴇx.ᴘʏ$~ → Hm, Do you want Random Emojis? (y/n) ~ ")).strip().lower() == 'y'
        em = 5
        if rm:
            em = int(input(Colors.mint("Sʏʀᴇx.ᴘʏ$~ → :) Emoji Amount ~ ")))
            if em <= 0:
                print(Colors.red_to_white("Emoji amount must be greater than 0."))
                await main()

        tasks = [spam(token, uid, message, count, rs, rm, em) for token in tokens]
        await asyncio.gather(*tasks)

        # Display success message after flooding
        print(f"\n{yellow}Sent Messages Successfully!{reset}")
        
        # Start countdown
        await countdown()
        
        # Clear screen, display logo, and re-display main menu
        clr()
        logo()
        await main()

    elif option == "2":
        print('Exiting the program..')
        exit()

if __name__ == "__main__":
    asyncio.run(main())
