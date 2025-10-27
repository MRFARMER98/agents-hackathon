from google.adk.agents import Agent
from google_maps_agent.prompts.prompt_loader import load_agent_description, load_agent_instruction
from google.adk.tools.google_search_tool import google_search
import os

MODEL = os.getenv("MODEL")

agent = Agent(
    name="google_search_manager",
    model=MODEL,
    description=load_agent_description("google_search_manager"),
    instruction=load_agent_instruction("google_search_manager"),
    tools=[google_search]
)