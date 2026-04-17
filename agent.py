from langgraph.graph import StateGraph
from groq import Groq
import os
from tools import *

client = Groq(api_key="YOUR_GROQ_API_KEY")

def llm_call(prompt):
    response = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def agent_node(state):
    user_input = state["input"]

    # simple intent detection
    if "edit" in user_input:
        return {"output": edit_interaction({"id":1,"field":"notes","new_value":"updated"})}
    
    if "suggest" in user_input:
        return {"output": suggest_action({})}

    # default → log interaction using LLM extraction
    structured = llm_call(f"Extract structured JSON from: {user_input}")
    
    try:
        import json
        data = json.loads(structured)
    except:
        data = {
            "hcp_name": "Unknown",
            "product": "Unknown",
            "notes": user_input,
            "date": "2026-04-17"
        }

    return {"output": log_interaction(data)}


def build_graph():
    graph = StateGraph(dict)
    graph.add_node("agent", agent_node)
    graph.set_entry_point("agent")
    return graph.compile()