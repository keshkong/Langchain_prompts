from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.3
)
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Which is greater, 2 or 10?"),
]
results=model.invoke(messages)
messages.append(AIMessage(content=results.text))
print(results.text)