from fastapi import FastAPI
from app.function_definitions import functions
from app.functions import api_functions, create_pizzas
from app.handler import OpenAIHandler
from app.models import Interaction
from app.db import Base, engine
from app.prompts import system_message
import os
from app.store import create_store
from app.db import Session, Review, Order

app = FastAPI()
handler = OpenAIHandler(api_functions, functions, system_message)


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)
    create_pizzas()
    if not os.path.exists("vectorstore.pkl"):
        create_store()


@app.on_event("shutdown")
async def shutdown_event():
    os.remove("pizzadb.db")


@app.post("/conversation")
async def query_endpoint(interaction: Interaction):
    response = handler.send_response(interaction.query)
    return {"response": response}


@app.get("/reviews")
async def get_all_reviews():
    session = Session()
    reviews = session.query(Review).all()
    session.close()
    return reviews


@app.get("/orders")
async def get_all_orders():
    session = Session()
    orders = session.query(Order).all()
    session.close()
    return orders
