from typing import List
from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: str


class Conversation(BaseModel):
    messages: List[Message]


class Interaction(BaseModel):
    conversation: Conversation
    query: str

