from google.adk.agents import Agent
from google.genai import types
from google_maps_agent.prompts.prompt_loader import load_agent_description, load_agent_instruction
from google_maps_agent.sub_agents.google_maps_manager import agent as google_maps_manager
from google_maps_agent.sub_agents.google_search_manager import agent as google_search_manager
from google.adk.tools.agent_tool import AgentTool

from dotenv import load_dotenv
import os

load_dotenv()

MODEL = os.getenv("MODEL")  

root_agent = Agent(
    name="super_agent",
    model=MODEL,
    description=load_agent_description("main_agent"),
    instruction=load_agent_instruction("main_agent"),
    tools=[AgentTool(google_search_manager), AgentTool(google_maps_manager)]
)
