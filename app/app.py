from fastapi import FastAPI
from app.function_definitions import functions
from app.functions import api_functions
from app.handler import OpenAIHandler
from app.models import Interaction
from app.db import Base, engine

app = FastAPI()
handler = OpenAIHandler(api_functions, functions)

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)


@app.post("/conversation")
async def query_endpoint(interaction: Interaction):
    response = handler.send_response(interaction.query)
    return {"response": response}