import os
import getpass
import instaloader
from time import sleep
from colorama import Fore, init
init()

cwd = os.getcwd()

username = input("Username: ")
password = getpass.getpass("Password: ")
password = str(password)

profile = instaloader.Instaloader()

try:
    print("Attempting to Login...")
    profile.login(username, password)
except instaloader.TwoFactorAuthRequiredException:
    print("2FA Required...")
    print()
    twoFactorAuthCode = input("Code: ")
    profile.two_factor_login(twoFactorAuthCode)

print()
print(Fore.GREEN + "Successfully Logged Into: " + username + Fore.WHITE)
sleep(2)
print()

profile.download_saved_posts(max_count=None, fast_update=False, post_filter=None)

print()
print(Fore.GREEN + "Completed " + Fore.WHITE + "Downloading Saved Posts.")
print()
input("Press ENTER to Exit...")
exit()