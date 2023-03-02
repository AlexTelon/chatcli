import subprocess
from openai_utils import generate_cli_command, explain_cli_command

prompt = input("What do you to do:").strip()
command = generate_cli_command(prompt)

while True:
    print(f"> {command}")

    action = input("Do you want to run this command or edit it? [y/n/e] ")
    
    if action.lower() == "y":
        print(command)
        subprocess.run(['bash', '-c', command])
        quit()
    elif action.lower() == "n":
        new_prompt = input("Please provide a new command prompt to add to the previous one: ")
        
        new_command = generate_cli_command(f"{prompt}\n\Suggestion: {command}\n\nAdditional remark: {new_prompt}")
        
        print(f"prompt: {prompt}\n\nSuggestion: {command}\n\nAdditional remark: {new_prompt}\n\nNew suggestion: {new_command}")
        
        command = new_command
        prompt = f"{prompt}\n\nAdditional remark: {new_prompt}"
    elif action.lower() == "e":
        # explain the code.
        print()
        print()
        print(explain_cli_command(command))
        print()
        print()
    else:
        print("Invalid action. Please enter 'r' or 'e'.")
