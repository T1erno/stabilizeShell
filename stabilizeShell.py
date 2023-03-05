#!/bin/python3

from time import sleep
from signal import signal, SIGINT
from sys import exit

try:
    import argparse
    from rich.console import Console
    from pynput.keyboard import Key, Controller
except ImportError:
    print("[!] Error: The required packages are not installed.")
    print("[!] Please install argparse, rich and pynput using pip.")

def handler(sig, frame):
    console.print("\n\n[[red]*[default]] Stoping.")
    exit(1) 

signal(SIGINT, handler)

console = Console()

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--method", default="script", type=str, help="Specify method")
    parser.add_argument("-s", "--shell", default="bash", type=str, help="Specify shell")

    args = vars(parser.parse_args())
    METHOD = args['method']
    SHELL = args['shell']
    delay=1

    spawner = {
    "script": f"script /dev/null -c {SHELL}",
    "python": f"""python -c 'import pty; pty.spawn("{SHELL}")'""",
    "python2": f"""python2 -c 'import pty; pty.spawn("{SHELL}")'""",
    "python3": f"""python3 -c 'import pty; pty.spawn("{SHELL}")'""",
    }

    seconds_to_wait = 5
    for second in range (seconds_to_wait,0, -1):
        console.print(f"[[red]![default]] [green]Waiting for positioning: [/green]{second}", end = '\r')
        sleep(1)


    keyboard = Controller()

    with console.status("[bold green]Stabilizing shell...", spinner='bouncingBall') as status:

        string = (f"{spawner[METHOD]}")
        console.print(f"[[blue]*[default]] [green]Spawning tty with: [yellow]{string}")
        keyboard.type(string)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(delay)

        keyboard.press(Key.ctrl)
        keyboard.press('z')
        keyboard.release(Key.ctrl)
        keyboard.release('z')
        sleep(delay)

        string = "stty raw -echo ; fg"
        console.print(f"[[blue]*[default]] [green]Backgrouding with: [yellow]{string}")
        keyboard.type(string)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(delay)

        string = "reset screen"
        console.print(f"[[blue]*[default]] [green]Reseting with: [yellow]{string}")
        keyboard.type(string)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(delay)

        string = "export TERM=screen"
        console.print(f"[[blue]*[default]] [green]Seting screen at term with: [yellow]{string}")
        keyboard.type(string)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(delay)


        string = f"export SHELL={SHELL}"
        console.print(f"[[blue]*[default]] [green]Setting {SHELL} at shell with: [yellow]{string}")
        keyboard.type(string)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(delay)

        string = "stty rows 56 columns 210"
        console.print(f"[[blue]*[default]] [green]Resizing with: [yellow]{string}")
        keyboard.type(string)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(delay)

        string = "clear"
        console.print(f"[[blue]*[default]] [green]Cleaning with: [yellow]{string}")
        keyboard.type(string)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(delay)
        
        console.print(f'[[blue]![default]] [bold][blue]Done!')

if __name__ == "__main__":
    main()
