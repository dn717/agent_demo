# A simple agent demo
This is a simple agent demo to show how agent works, it uses one of the most common Python agent framework - `Pydantic AI`.

## File detail
 - main.py : define agent and model
 - tools.py: define functions like `read_file`,`list_files`,`rename_file`

## How it works
User input a sentence, Agent collects tools info, user's prompt and system prompt, agent pass it to model(LLM) through system prompt or function calling way, and then model can return the command to Agent, make Agent call the corresponding tool. And model will organize those info and return a output to user.

## Prerequisite
Install Pydantic AI
`pip install pydantic-ai`


## Quick start
in the terminal, run `python main.py`.


## Sample
here is the example of the input and output with communicating with agent let it invoke tools.


