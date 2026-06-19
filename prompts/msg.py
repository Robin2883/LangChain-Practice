from langchain_core .messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(model="qwen/qwen3-32b", reasoning_format="parsed")

messages=[
    SystemMessage(content= "You are a helpful assistant"),
    HumanMessage(content="Tell me about langchain")
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)