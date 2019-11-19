from termcolor import colored
from pyfiglet import figlet_format
import requests
from random import choice

def print_art():
    art = figlet_format("Dad Joke 3000", font='standard')
    color_art = colored(art, color='magenta')
    print(color_art)

print_art()

user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term":user_input}
).json()

# num_jokes = len(res["results"])
num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} {user_input} jokes! Here's one: ")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print(f"There is one {user_input} joke. Here it is: ")
    print(results[0]["joke"])
else:
    print(f"Sorry, couldn't find any {user_input} jokes!")
