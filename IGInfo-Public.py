import os
import argparse
import instaloader 
from time import sleep
from colorama import Fore, init
init()

parser = argparse.ArgumentParser(description='Instagram Account Information/Downloader')
parser.add_argument('-i', '--info', help='Provides most of the accounts information.', action='store_false')
parser.add_argument('-dP', '--downposts', help='Downloads the accounts posts.', action='store_true')
args = parser.parse_args()
infoBool = args.info
downloadBool = args.downposts

cwd = os.getcwd()
username = input("Username: ")
print()

insta = instaloader.Instaloader()
profile = instaloader.Profile.from_username(insta.context, username)

profilePic = profile.get_profile_pic_url()


def stepThrough():
    if infoBool==True:
        accountInformation()
    if downloadBool==True:
        profilePrivate = profile.is_private
        if profilePrivate==True:
            print(Fore.RED + "Error 01: " + Fore.WHITE + "Account is Privated, cannot download posts.")
            input("Press Enter to Exit...")
            exit()
        else:
            input("Press ENTER to begin post downloading.")
        downloadPosts()

    input("Press Enter to Exit...")
    exit()


def accountInformation():
    print()
    print(Fore.GREEN + "Account Information:")
    print()

    print(Fore.BLUE + "Profile Picture: " + Fore.WHITE + profilePic)
    print()

    print(Fore.BLUE + "Name: " + Fore.WHITE + str(profile.full_name))
    print(Fore.BLUE + "Business Account: " + Fore.WHITE + str(profile.is_business_account))
    print(Fore.BLUE + "Private: " + Fore.WHITE + str(profile.is_private))
    print(Fore.BLUE + "Verified: " + Fore.WHITE + str(profile.is_verified))
    print()

    print(Fore.BLUE + "Follower Count: " + Fore.WHITE + str(profile.followers))
    print(Fore.BLUE + "Following Count: " + Fore.WHITE + str(profile.followees))
    print()

    print(Fore.BLUE + "Bio: \n" + Fore.WHITE + str(profile.biography))
    print()

    print(Fore.BLUE + "IGTV Count: " + Fore.WHITE + str(profile.igtvcount))
    print(Fore.BLUE + "Post Count: " + Fore.WHITE + str(profile.mediacount))
    print()

    return


def downloadPosts():
    print()
    posts = profile.get_posts()
    for post in posts:
        insta.download_post(post, target="Posts")

    print()
    print(Fore.GREEN + "Completed " + Fore.WHITE + "Account Posts Downloading.")
    sleep(2)
    print()

    return

stepThrough()
