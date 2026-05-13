from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai import Agent
from dotenv import load_dotenv
import tools

load_dotenv()

model = OpenAIChatModel("gpt-4o")
agent = Agent(model, system_prompt="You are an experienced programmer",
              tools=[tools.read_file, tools.list_files, tools.rename_file])

def main():
    while True:
        user_input = input("Input:")
        resp = agent.run_sync(user_input)
        print(resp.output)


if __name__ == "__main__":
    main()


