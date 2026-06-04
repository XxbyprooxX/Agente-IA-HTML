from agents import Agent, Runner, OpenAIChatCompletionsModel
import asyncio
from openai import AsyncOpenAI
ollama_client = AsyncOpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

ollama_qwen = OpenAIChatCompletionsModel(model="qwen3:4b", openai_client=ollama_client)

agent = Agent (
    name= "Joke Teller",
    instructions="Your an joke teller",
    model=ollama_qwen
    )

async def main():
    result = await Runner.run(agent,"Give me short joke about a agentic AI")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())