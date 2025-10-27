from google.adk.agents import Agent
from google_maps_agent.prompts.prompt_loader import load_agent_description, load_agent_instruction
from google.adk.tools.google_maps_grounding_tool import google_maps_grounding

import os

MODEL = os.getenv("MODEL")

agent = Agent(
    name="google_maps_manager",
    model=MODEL,
    description=load_agent_description("google_maps_manager"),
    instruction=load_agent_instruction("google_maps_manager"),
    tools=[google_maps_grounding]
)