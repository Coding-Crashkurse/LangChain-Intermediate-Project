from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

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

functions = [
    {
        "name": "get_pizza_info",
        "description": "Get name and price of a pizza of the restaurant",
        "parameters": {
            "type": "object",
            "properties": {
                "pizza_name": {
                    "type": "string",
                    "description": "The name of the pizza, e.g. Salami",
                },
            },
            "required": ["pizza_name"],
        },
    },
    {
        "name": "create_order",
        "description": "Create an order for a specific pizza",
        "parameters": {
            "type": "object",
            "properties": {
                "pizza_name": {
                    "type": "string",
                    "description": "The name of the pizza to order, e.g. Margherita",
                },
            },
            "required": ["pizza_name"],
        },
    },
    {
        "name": "create_review",
        "description": "Create a review for the restaurant",
        "parameters": {
            "type": "object",
            "properties": {
                "review_text": {
                    "type": "string",
                    "description": "The text of the review, e.g. Great pizza!",
                },
            },
            "required": ["review_text"],
        },
    },
]



chat = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

messages = [
    SystemMessage(
        content=system_message
    ),
    HumanMessage(
        content="I really liked the restaurant. It was awesome!"
    ),
]
result = chat.predict_messages(messages=messages,
functions=functions
)
print(result)