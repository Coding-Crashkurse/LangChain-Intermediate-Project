from fastapi import FastAPI
from app.function_definitions import functions
from app.functions import api_functions, create_pizzas
from app.handler import OpenAIHandler
from app.models import Interaction
from app.db import Base, engine
import os

app = FastAPI()
handler = OpenAIHandler(api_functions, functions)

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)
    create_pizzas()

@app.on_event("shutdown")
async def shutdown_event():
    os.remove('pizzadb.db')

@app.post("/conversation")
async def query_endpoint(interaction: Interaction):
    response = handler.send_response(interaction.query)
    return {"response": response}