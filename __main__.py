#!/usr/bin/env python3

import subprocess

def main():
    url = "https://discord.com/api/download/stable?platform=linux&format=deb"

    subprocess.run(['wget', url, '-O', '/tmp/discord.deb'])
    subprocess.run(['sudo', 'dpkg', '-i', f'/tmp/discord.deb'])

    print("Updated Discord!")


if __name__ == "__main__":
    main()
