## to give Instructions to the LLM

from langchain_core.prompts import ChatPromptTemplate

def get_prompt():
    prompt = ChatPromptTemplate.from_messages([
        # Ensure it's a string 'system' and in a list
        ("system", "You are a helpful tech AI Assistant"), 
        ("human", "{input}")
    ])
    return prompt