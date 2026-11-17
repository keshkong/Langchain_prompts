
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
load_dotenv()

# Connect to local Ollama model
model = ChatOllama(
    model="llama3.2:1b",
    temperature=0.3
)

# Define conversation messages
messages = [
    SystemMessage(content="You are a helpful assistant. Give short and accurate answers."),
    
]

# Send messages to Ollama
while True:
    user_input= input("User:")
    messages.append(HumanMessage(content=user_input))
    result = model.invoke(messages)
    messages.append(AIMessage(content=result.content))
    print("AI: ", result.content)

# Store AI response


print(messages)
