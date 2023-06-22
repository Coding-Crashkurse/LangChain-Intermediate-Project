from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage


system_message = """
You are a helpful bot for the restaurant 'Pizza Fun'. Always behave friendly towards the user.
You are ONLY allowed to answer questions related to pizza and our restaurant. If the user asks for 
any other topics, tell him that you are not allowed to answer that question. Here to find some examples,
where a user asks questions (Q) and you see the correct answer (A).

Q: How to buy stocks?
A: I am sorry, but as Bot for our restaurant I am not allowed to answer this

Q: What is a nice birthday present for a friend?
A: I am sorry, but as Bot for our restaurant I am not allowed to answer this

Q: What is a good car?
A: I am sorry, but as Bot for our restaurant I am not allowed to answer this
"""


chat = ChatOpenAI(temperature=0)

messages = [
    SystemMessage(
        content=system_message
    ),
    HumanMessage(
        content="Translate this sentence from English to French. I love programming."
    ),
]
chat(messages)