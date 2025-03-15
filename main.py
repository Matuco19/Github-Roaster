import requests
import rich
import json
from rich.console import Console
from rich.markdown import Markdown

console = Console()

console.print(Markdown("# Github Roaster CLI"), style="bold white")
md = Markdown(f"""
Welcome to the **Github Roaster**! This program will roast any github user of your choice.  
Created by [Matuco19](https://matuco19.com)  
[Discord Server](https://discord.gg/hp7yCxHJBw) | [Github](https://github.com/Matuco19/GithubRoaster) | [License](https://matuco19.com/licenses/MATCO-Open-Source)  
""")
console.print(md)

language = input("Enter the language you want to use: ")
username = input("Enter the github username you want to roast: ")

# get the user info
try:
    response = requests.get('https://api.github.com/users/'+username)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    console.print(f"Error: {e}", style="red")
    exit(1)


prompt = f"give a short and harsh roasting for the following github profile (make in the {language} language): {username}. Here are the details: \"{response.json()}\""

def generate(prompt):
    response = requests.post('https://text.pollinations.ai/openai', json={
        "messages": [
            {
                "role": "system",
                "content": prompt,
            }
        ],
        "model": "openai-large"
    })
    return response.json()


result = generate(prompt)
print(result['choices'][0]['message']['content'])
