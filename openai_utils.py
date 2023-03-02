import openai

# Read the OpenAI API key from a hidden local file
with open('.openai_key.secret', 'r') as f:
    openai.api_key = f.read().strip()

# Define the standard prompt header
PROMPT_HEADER_GENERATE_CLI = """You are a CLI helper tool for linux. You will respond with the correct command to run based on the user's input.

Your input may be either just a question. Or a series of questions and suggested answers.
After each suggestion there may be a additional remark about a change that should be made.

Always just add a correct and executable command to the end of the prompt. No comments or additional text is allowed.

"""

def generate_cli_command(prompt):
    # Generate a response using the OpenAI GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{PROMPT_HEADER_GENERATE_CLI}{prompt}",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Return the response text as a string
    return response.choices[0].text.strip()


def explain_cli_command(command):
    prompt_header = "Explain the following command. If it has arguments then do so argument by argument formated nicely."

    # Generate an explanation using the OpenAI GPT-3 model
    explanation = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{prompt_header}:\n{command}",
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Return the explanation text as a string
    return explanation.choices[0].text.strip()