from langchain.chat_models import Ollama
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from constants import OLLAMA_MODEL

llm = Ollama(model=OLLAMA_MODEL)

# Define a math tool
def calculate_math(expression: str) -> str:
    import numexpr
    return str(numexpr.evaluate(expression))

tools = [Tool(name="calculate_math", func=calculate_math, description="Evaluate math expressions")]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

print(agent.run("What is 123 + 456 * 7?"))
