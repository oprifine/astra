import sys
import time

def animate_loading():
        for i in range(101):
            sys.stdout.write('\r')
            sys.stdout.write("[{0}{1}] {2}%".format("=" * i, " " * (100 - i), i))
            sys.stdout.flush()
            time.sleep(0.1)
echo = print

echo("Welcome to Nebula!")
pkg = input("Please input your package name here: ")

if pkg is "":
    print("Please input a package!")
    pass
else:
    db = print("Checking databases...")
    animate_loading()
if db == "":
    print("Sorry, we don't have that package at the moment. Please check later!")
else:
    print(f"Installing package.... \n
          {animate_loading()}""
