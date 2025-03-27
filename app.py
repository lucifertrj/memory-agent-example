# pip install agno sqlalchemy google-genai
# uv add agno sqlalchemy google-genai

import json
from agno.agent import Agent
from agno.models.google import Gemini
from agno.storage.agent.sqlite import SqliteAgentStorage

import os
os.environ["GOOGLE_API_KEY"] = "AI***" # get it from aistudio.google.com

agent_memory = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    storage=SqliteAgentStorage(
        table_name="agent_sessions", db_file="tmp/agent_storage.db"
    ),
    add_history_to_messages=True,
    num_history_responses=3,
    description="You are a helpful assistant that always responds in a polite, upbeat and positive manner.",
)

def print_chat_history(agent):
    print(json.dumps(
        [
            m.model_dump(include={"role", "content"})
            for m in agent.memory.messages
        ]))
    
agent_memory.print_response("write a 2 sentence on CSK vs RCB", stream=True)
print_chat_history(agent_memory)
agent_memory.print_response("repeat the same 2 sentence with additional one sentence", stream=True)
print_chat_history(agent_memory)
