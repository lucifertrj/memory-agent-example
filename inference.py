# pip install agno sqlalchemy google-genai
# or uv add agno sqlalchemy google-genai
# pip install -U googlesearch-python pycountry
# or uv add googlesearch-python pycountry

import json
from agno.agent import Agent
from agno.models.google import Gemini
from agno.storage.agent.sqlite import SqliteAgentStorage
from agno.tools.googlesearch import GoogleSearchTools

import os
os.environ["GOOGLE_API_KEY"] = "***" 

agent_memory = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    tools=[GoogleSearchTools()],
    storage=SqliteAgentStorage(
        table_name="agent_sessions", db_file="tmp/agent_storage.db"
    ),
    add_history_to_messages=True,
    num_history_responses=3,
    description="You are a helpful assistant that always responds in a polite, upbeat and positive manner. If search is required use Google Search",
)

def print_chat_history(agent):
    print(json.dumps(
        [
            m.model_dump(include={"role", "content"})
            for m in agent.memory.messages
        ]))
    
agent_memory.print_response("who played the IPL match on 27th March 2025", stream=True)
print_chat_history(agent_memory)
agent_memory.print_response("tell me who won for the same match", stream=True)
print_chat_history(agent_memory)
