import pyfiglet 
import time
from rich import print
import random   

FOLLOWERS = random.randint(100, 10000)

title = pyfiglet.figlet_format("ZixznPriv.com", font = "slant")

def QuestionsAInputs():
    user = input("Enter a username to lookup : ")
    print(f"Looking up username: [bold blue]{user}[/bold blue]")
    q1 =  input("Confirm? (y/n) : ")
    if q1 == "y":
        print("Looking up...")
        time.sleep(2)
        print(f"Username [bold blue]{user} [/bold blue]. \n Status: Found on 1 site. \n Site: [bold blue]example.com[/bold blue]y ")
        print(f"Follwers : [bold blue] {FOLLOWERS}[/bold blue].")  # Placeholder for actual lookup logic
    elif q1 == "n":
        print("Cancelled.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")



print("Note This is a demo it does not actually lookup usernames. ~S1aving up for a url called ZixznPriv.com")
time.sleep(1)

# print ("\n")
print(f"[bold blue]{title}[/bold blue]")
print(f"This is a tool made by [bold blue]ZixznPriv.com[/bold blue] to lookup usernames.")

QuestionsAInputs()
