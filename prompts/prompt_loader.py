"""
Prompt utilities for loading agent descriptions and instructions from markdown files.
"""
from pathlib import Path


def load_prompt(filename: str) -> str:
    """Load a prompt from a markdown file in the prompts directory."""
    prompts_dir = Path(__file__).parent
    prompt_path = prompts_dir / filename

    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")

    return prompt_path.read_text().strip()


def load_agent_description(agent_name: str) -> str:
    """Load agent description from markdown file."""
    return load_prompt(f"{agent_name}_description.md")


def load_agent_instruction(agent_name: str) -> str:
    """Load agent instruction from markdown file."""
    return load_prompt(f"{agent_name}_instruction.md")
